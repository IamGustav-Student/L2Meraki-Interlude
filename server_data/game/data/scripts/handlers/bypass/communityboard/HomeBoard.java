/*
 * Copyright (c) 2013 L2jMobius
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be
 * included in all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 * WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
 * IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
 */
package handlers.bypass.communityboard;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.Objects;
import java.util.concurrent.TimeUnit;
import java.util.function.BiPredicate;
import java.util.function.Predicate;
import java.util.logging.Logger;

import org.l2jmobius.commons.database.DatabaseFactory;
import org.l2jmobius.commons.threads.ThreadPool;
import org.l2jmobius.gameserver.cache.HtmCache;
import org.l2jmobius.gameserver.config.custom.CommunityBoardConfig;
import org.l2jmobius.gameserver.config.custom.PremiumSystemConfig;
import org.l2jmobius.gameserver.data.sql.ClanTable;
import org.l2jmobius.gameserver.data.SchemeBufferTable;
import org.l2jmobius.gameserver.data.xml.ExperienceData;
import org.l2jmobius.gameserver.data.xml.MultisellData;
import org.l2jmobius.gameserver.data.xml.SkillData;
import org.l2jmobius.gameserver.handler.CommunityBoardHandler;
import org.l2jmobius.gameserver.handler.IParseBoardHandler;
import org.l2jmobius.gameserver.managers.PcCafePointsManager;
import org.l2jmobius.gameserver.managers.PremiumManager;
import org.l2jmobius.gameserver.model.actor.Creature;
import org.l2jmobius.gameserver.model.actor.Player;
import org.l2jmobius.gameserver.model.actor.Summon;
import org.l2jmobius.gameserver.model.item.enums.ItemProcessType;
import org.l2jmobius.gameserver.model.item.instance.Item;
import org.l2jmobius.gameserver.model.item.type.CrystalType;
import org.l2jmobius.gameserver.model.skill.Skill;
import org.l2jmobius.gameserver.model.zone.ZoneId;
import org.l2jmobius.gameserver.network.serverpackets.MagicSkillUse;
import org.l2jmobius.gameserver.network.serverpackets.SellList;
import org.l2jmobius.gameserver.network.serverpackets.ShowBoard;


/**
 * Home board.
 * @author Zoey76, Mobius
 */
public class HomeBoard implements IParseBoardHandler
{
	private static final Logger LOGGER = Logger.getLogger(HomeBoard.class.getName());
	
	// SQL Queries
	private static final String COUNT_FAVORITES = "SELECT COUNT(*) AS favorites FROM `bbs_favorites` WHERE `playerId`=?";
	private static final String NAVIGATION_PATH = "data/html/CommunityBoard/Custom/navigation.html";
	
	private static final String[] COMMANDS =
	{
		"_bbshome",
		"_bbstop",
	};
	
	private static final String[] CUSTOM_COMMANDS =
	{
		"_bbspremium",
		CommunityBoardConfig.COMMUNITYBOARD_ENABLE_MULTISELLS ? "_bbsexcmultisell" : null,
		CommunityBoardConfig.COMMUNITYBOARD_ENABLE_MULTISELLS ? "_bbsmultisell" : null,
		CommunityBoardConfig.COMMUNITYBOARD_ENABLE_MULTISELLS ? "_bbssell" : null,
		CommunityBoardConfig.COMMUNITYBOARD_ENABLE_TELEPORTS ? "_bbsteleport" : null,
		CommunityBoardConfig.COMMUNITYBOARD_ENABLE_BUFFS ? "_bbsbuff" : null,
		CommunityBoardConfig.COMMUNITYBOARD_ENABLE_HEAL ? "_bbsheal" : null,
		CommunityBoardConfig.COMMUNITYBOARD_ENABLE_DELEVEL ? "_bbsdelevel" : null
	};
	
	private static final BiPredicate<String, Player> COMBAT_CHECK = (command, player) ->
	{
		boolean commandCheck = false;
		for (String c : CUSTOM_COMMANDS)
		{
			if ((c != null) && command.startsWith(c))
			{
				commandCheck = true;
				break;
			}
		}
		
		return commandCheck && (player.isCastingNow() || player.isCastingSimultaneouslyNow() || player.isInCombat() || player.isInDuel() || player.isInOlympiadMode() || player.isInsideZone(ZoneId.SIEGE) || player.isInsideZone(ZoneId.PVP) || (player.getPvpFlag() > 0) || player.isAlikeDead() || player.isOnEvent() || player.isInStoreMode());
	};
	
	private static final Predicate<Player> KARMA_CHECK = player -> CommunityBoardConfig.COMMUNITYBOARD_KARMA_DISABLED && (player.getKarma() > 0);
	
	@Override
	public String[] getCommandList()
	{
		final List<String> commands = new ArrayList<>();
		commands.addAll(Arrays.asList(COMMANDS));
		commands.addAll(Arrays.asList(CUSTOM_COMMANDS));
		return commands.stream().filter(Objects::nonNull).toArray(String[]::new);
	}
	
	@Override
	public boolean onCommand(String command, Player player)
	{
		// Old custom conditions check move to here
		if (CommunityBoardConfig.COMMUNITYBOARD_COMBAT_DISABLED && COMBAT_CHECK.test(command, player))
		{
			player.sendMessage("You can't use the Community Board right now.");
			return false;
		}
		
		if (KARMA_CHECK.test(player))
		{
			player.sendMessage("Players with Karma cannot use the Community Board.");
			return false;
		}
		
		if (CommunityBoardConfig.COMMUNITYBOARD_PEACE_ONLY && !player.isInsideZone(ZoneId.PEACE))
		{
			player.sendMessage("Community Board cannot be used out of peace zone.");
			return false;
		}
		
		String returnHtml = null;
		String navigation = null;
		
		if (CommunityBoardConfig.CUSTOM_CB_ENABLED)
		{
			navigation = HtmCache.getInstance().getHtm(player, NAVIGATION_PATH);
		}
		
		if (command.equals("_bbshome") || command.equals("_bbstop"))
		{
			final String customPath = CommunityBoardConfig.CUSTOM_CB_ENABLED ? "Custom/" : "";
			CommunityBoardHandler.getInstance().addBypass(player, "Home", command);
			returnHtml = HtmCache.getInstance().getHtm(player, "data/html/CommunityBoard/" + customPath + "home.html");
			if (!CommunityBoardConfig.CUSTOM_CB_ENABLED)
			{
				returnHtml = returnHtml.replace("%fav_count%", Integer.toString(getFavoriteCount(player)));
				returnHtml = returnHtml.replace("%region_count%", Integer.toString(getRegionCount(player)));
				returnHtml = returnHtml.replace("%clan_count%", Integer.toString(ClanTable.getInstance().getClanCount()));
			}
		}
		else if (command.startsWith("_bbstop;"))
		{
			final String customPath = CommunityBoardConfig.CUSTOM_CB_ENABLED ? "Custom/" : "";
			final String path = command.replace("_bbstop;", "");
			if ((path.length() > 0) && path.endsWith(".html"))
			{
				returnHtml = HtmCache.getInstance().getHtm(player, "data/html/CommunityBoard/" + customPath + path);
			}
		}
		else if (command.startsWith("_bbsmultisell"))
		{
			final String fullBypass = command.replace("_bbsmultisell;", "");
			final String[] buypassOptions = fullBypass.split(",");
			final int multisellId = Integer.parseInt(buypassOptions[0]);
			final String page = buypassOptions[1];
			returnHtml = HtmCache.getInstance().getHtm(player, "data/html/CommunityBoard/Custom/" + page + ".html");
			ThreadPool.schedule(() -> MultisellData.getInstance().separateAndSend(multisellId, player, null, false), 100);
		}
		else if (command.startsWith("_bbsexcmultisell"))
		{
			final String fullBypass = command.replace("_bbsexcmultisell;", "");
			final String[] buypassOptions = fullBypass.split(",");
			final int multisellId = Integer.parseInt(buypassOptions[0]);
			final String page = buypassOptions[1];
			returnHtml = HtmCache.getInstance().getHtm(player, "data/html/CommunityBoard/Custom/" + page + ".html");
			ThreadPool.schedule(() -> MultisellData.getInstance().separateAndSend(multisellId, player, null, true), 100);
		}
		else if (command.startsWith("_bbssell"))
		{
			final String[] args = command.split(";");
			final String page = args[1];
			
			// Si hay un tercer argumento, es el objectId de un item para reciclar
			if (args.length > 2)
			{
				try
				{
					int objectId = Integer.parseInt(args[2]);
					Item item = player.getInventory().getItemByObjectId(objectId);
					if (item != null && !item.isEquipped() && item.isSellable() && !item.isQuestItem())
					{
						CrystalType crystalType = item.getTemplate().getCrystalType();
						if (crystalType != CrystalType.NONE)
						{
							// Devolvemos cristales si es equipamiento con grado
							int crystalId = crystalType.getCrystalId();
							int crystalCount = item.getTemplate().getCrystalCount(item.getEnchantLevel());
							player.destroyItem(ItemProcessType.FEE, item, player, true);
							player.addItem(ItemProcessType.FEE, crystalId, crystalCount, player, true);
							player.sendMessage("Has reciclado " + item.getTemplate().getName() + " y recibiste " + crystalCount + " cristales.");
						}
						else
						{
							// Devolvemos Adena (50% del precio de referencia)
							long price = item.getTemplate().getReferencePrice() / 2;
							if (price <= 0) price = 1; // Precio minimo
							long totalAdena = price * item.getCount();
							player.destroyItem(ItemProcessType.FEE, item, player, true);
							player.addAdena(ItemProcessType.FEE, (int) totalAdena, player, true);
							player.sendMessage("Has vendido " + item.getTemplate().getName() + " por " + totalAdena + " Adena.");
						}
					}
				}
				catch (Exception e)
				{
					// Error silencioso o log
				}
			}

			// Generamos el HTML del listado de reciclaje
			String html = HtmCache.getInstance().getHtm(player, "data/html/CommunityBoard/Custom/merchant/recycle.html");
			StringBuilder itemsHtml = new StringBuilder();
			int count = 0;
			for (Item item : player.getInventory().getItems())
			{
				if (item.isEquipped() || item.isQuestItem() || !item.isSellable() || item.getTemplate().getReferencePrice() <= 0)
				{
					continue;
				}
				
				String icon = item.getTemplate().getIcon();
				if (icon == null || icon.isEmpty()) icon = "icon.etc_question_mark_i00";
				
				long price = item.getTemplate().getReferencePrice() / 2;
				if (price <= 0) price = 1;
				
				String valueStr = (item.getTemplate().getCrystalType() != CrystalType.NONE) ? "Cristales" : (price * item.getCount()) + " A.";
				
				itemsHtml.append("<tr>");
				itemsHtml.append("<td width=40><img src=\"").append(icon).append("\" width=32 height=32></td>");
				itemsHtml.append("<td width=300><font color=\"FFFFFF\">").append(item.getTemplate().getName()).append(item.getEnchantLevel() > 0 ? " +"+item.getEnchantLevel() : "").append("</font></td>");
				itemsHtml.append("<td width=80><center>").append(valueStr).append("</center></td>");
				itemsHtml.append("<td width=80><center><button value=\"Reciclar\" action=\"bypass _bbssell;").append(page).append(";").append(item.getObjectId()).append("\" width=75 height=21 back=\"L2UI_CH3.Btn_BF_Down\" fore=\"L2UI_CH3.Btn_BF\"></center></td>");
				itemsHtml.append("</tr>");
				count++;
			}
			
			if (count == 0)
			{
				itemsHtml.append("<tr><td colspan=4><center><br><br><font color=\"AAAAAA\">No tienes items para reciclar en tu inventario.</font></center></td></tr>");
			}
			
			returnHtml = html.replace("%recycle_items%", itemsHtml.toString());
		}
		else if (command.startsWith("_bbsteleport"))
		{
			final String teleBuypass = command.replace("_bbsteleport;", "");
			if (player.getInventory().getInventoryItemCount(CommunityBoardConfig.COMMUNITYBOARD_CURRENCY, -1) < CommunityBoardConfig.COMMUNITYBOARD_TELEPORT_PRICE)
			{
				player.sendMessage("Not enough currency!");
			}
			else if (CommunityBoardConfig.COMMUNITY_AVAILABLE_TELEPORTS.get(teleBuypass) != null)
			{
				player.disableAllSkills();
				player.sendPacket(new ShowBoard());
				player.destroyItemByItemId(ItemProcessType.FEE, CommunityBoardConfig.COMMUNITYBOARD_CURRENCY, CommunityBoardConfig.COMMUNITYBOARD_TELEPORT_PRICE, player, true);
				player.setIn7sDungeon(false);
				player.setInstanceId(0);
				player.teleToLocation(CommunityBoardConfig.COMMUNITY_AVAILABLE_TELEPORTS.get(teleBuypass), 0);
				ThreadPool.schedule(player::enableAllSkills, 3000);
			}
		}
		else if (command.startsWith("_bbsbuff"))
		{
			final String fullBypass = command.replace("_bbsbuff;", "");
			final String[] buypassOptions = fullBypass.split(";");
			final int buffCount = buypassOptions.length - 1;
			final String page = buypassOptions[buffCount];
			if (player.getInventory().getInventoryItemCount(CommunityBoardConfig.COMMUNITYBOARD_CURRENCY, -1) < (CommunityBoardConfig.COMMUNITYBOARD_BUFF_PRICE * buffCount))
			{
				player.sendMessage("Not enough currency!");
			}
			else
			{
				player.destroyItemByItemId(ItemProcessType.FEE, CommunityBoardConfig.COMMUNITYBOARD_CURRENCY, CommunityBoardConfig.COMMUNITYBOARD_BUFF_PRICE * buffCount, player, true);
				final Summon pet = player.getSummon();
				final List<Creature> targets = new ArrayList<>(4);
				targets.add(player);
				if (pet != null)
				{
					targets.add(pet);
				}
				
				if (buypassOptions[0].equalsIgnoreCase("category"))
				{
					String category = buypassOptions[1];
					// Normalización de categorías
					if (category.equalsIgnoreCase("Danza") || category.equalsIgnoreCase("Danzas")) category = "Dances";
					if (category.equalsIgnoreCase("Canto") || category.equalsIgnoreCase("Cantos")) category = "Songs";
					
					final List<Integer> skillIds = SchemeBufferTable.getInstance().getSkillsIdsByType(category);
					if (!skillIds.isEmpty())
					{
						for (int skillId : skillIds)
						{
							int maxLevel = SkillData.getInstance().getMaxLevel(skillId);
							int skillLevel = player.hasPremiumStatus() ? maxLevel : 1;
							
							if (maxLevel < 1)
							{
								continue;
							}
							
							final Skill skill = SkillData.getInstance().getSkill(skillId, Math.min(skillLevel, maxLevel));
							if ((skill != null) && CommunityBoardConfig.COMMUNITY_AVAILABLE_BUFFS.contains(skill.getId()))
							{
								for (Creature target : targets)
								{
									skill.applyEffects(player, target);
								}
							}
						}
						player.sendMessage("Has recibido los buffs de la categoria: " + category);
					}
					returnHtml = HtmCache.getInstance().getHtm(player, "data/html/CommunityBoard/Custom/" + buypassOptions[2] + ".html");
				}
				else if (buypassOptions[0].equalsIgnoreCase("category_view"))
				{
					String category = buypassOptions[1];
					// Normalización de categorías
					if (category.equalsIgnoreCase("Danza") || category.equalsIgnoreCase("Danzas")) category = "Dances";
					if (category.equalsIgnoreCase("Canto") || category.equalsIgnoreCase("Cantos")) category = "Songs";
					
					returnHtml = HtmCache.getInstance().getHtm(player, "data/html/CommunityBoard/Custom/buffer/category.html");
					
					final List<Integer> skillIds = SchemeBufferTable.getInstance().getSkillsIdsByType(category);
					final StringBuilder sb = new StringBuilder();
					sb.append("<table width=450>");
					int count = 0;
					for (int skillId : skillIds)
					{
						if (count % 6 == 0) sb.append("<tr>");
						
						String iconId = String.format("%04d", skillId);
						
						sb.append("<td align=center width=75 height=45>");
						sb.append("<table border=0 cellspacing=0 cellpadding=0 bgcolor=333333><tr><td>");
						sb.append("<button value=\" \" action=\"bypass _bbsbuff;" + skillId + ",2;buffer/category;category_view;" + category + "\" width=32 height=32 back=\"icon.skill" + iconId + "\" fore=\"icon.skill" + iconId + "\">");
						sb.append("</td></tr></table>");
						sb.append("</td>");
						
						count++;
						if (count % 6 == 0) sb.append("</tr>");
					}
					if (count % 6 != 0) sb.append("</tr>");
					sb.append("</table>");
					
					returnHtml = returnHtml.replace("%buffer_skills%", sb.toString());
					returnHtml = returnHtml.replace("%category_name%", category);
					
					// Soporte para edición de esquemas
					if (buypassOptions.length > 4 && buypassOptions[2].equalsIgnoreCase("scheme") && buypassOptions[3].equalsIgnoreCase("edit"))
					{
						final String schemeName = buypassOptions[4];
						returnHtml = returnHtml.replace("bypass _bbsbuff;", "bypass _bbsbuff;scheme;add;" + schemeName + ";");
					}
				}
				else if (buypassOptions[0].equalsIgnoreCase("scheme"))
				{
					final String action = buypassOptions[1];
					final String schemeName = buypassOptions.length > 2 ? buypassOptions[2] : "";
					final String returnPage = buypassOptions.length > 3 ? buypassOptions[3] : "buffer/main";
					
					if (schemeName.isEmpty() || schemeName.equalsIgnoreCase("$s_name"))
					{
						if (!action.equalsIgnoreCase("save")) // Solo ignoramos si no es save, ya que save tiene su propio mensaje
						{
							return onCommand("_bbsbuff;buffer/main", player);
						}
					}
					
					if (action.equalsIgnoreCase("load"))
					{
						final List<Integer> skillIds = SchemeBufferTable.getInstance().getScheme(player.getObjectId(), schemeName);
						if (!skillIds.isEmpty())
						{
							for (int skillId : skillIds)
							{
								int maxLevel = SkillData.getInstance().getMaxLevel(skillId);
								int skillLevel = player.hasPremiumStatus() ? maxLevel : 1;
								final Skill skill = SkillData.getInstance().getSkill(skillId, Math.min(skillLevel, maxLevel));
								if (skill != null)
								{
									for (Creature target : targets)
									{
										skill.applyEffects(player, target);
									}
								}
							}
							player.sendMessage("Perfil '" + schemeName + "' cargado correctamente.");
						}
						else
						{
							player.sendMessage("El perfil '" + schemeName + "' no existe o esta vacio.");
						}
					}
					else if (action.equalsIgnoreCase("save"))
					{
						final List<Integer> skillIds = new ArrayList<>();
						player.getEffectList().getEffects().forEach(effect ->
						{
							int id = effect.getSkill().getId();
							if (CommunityBoardConfig.COMMUNITY_AVAILABLE_BUFFS.contains(id))
							{
								if (!skillIds.contains(id))
								{
									skillIds.add(id);
								}
							}
						});
						
						if (skillIds.isEmpty())
						{
							player.sendMessage("No tienes buffs activos para guardar.");
						}
						else if (schemeName.isEmpty() || schemeName.equalsIgnoreCase("$s_name"))
						{
							player.sendMessage("Debes introducir un nombre valido para el perfil.");
						}
						else
						{
							SchemeBufferTable.getInstance().setScheme(player.getObjectId(), schemeName, skillIds);
							player.sendMessage("Perfil '" + schemeName + "' guardado con tus buffs actuales.");
						}
					}
					else if (action.equalsIgnoreCase("delete"))
					{
						if (!schemeName.isEmpty())
						{
							SchemeBufferTable.getInstance().setScheme(player.getObjectId(), schemeName, Collections.emptyList());
							player.sendMessage("Perfil '" + schemeName + "' borrado correctamente.");
						}
					}
					else if (action.equalsIgnoreCase("edit"))
					{
						returnHtml = HtmCache.getInstance().getHtm(player, "data/html/CommunityBoard/Custom/buffer/edit_scheme.html");
						final List<Integer> skillIds = SchemeBufferTable.getInstance().getScheme(player.getObjectId(), schemeName);
						final StringBuilder sb = new StringBuilder();
						if (skillIds.isEmpty())
						{
							sb.append("<tr><td colspan=3 align=center><font color=\"888888\">Este perfil no tiene habilidades.</font></td></tr>");
						}
						else
						{
							for (int skillId : skillIds)
							{
								final Skill skill = SkillData.getInstance().getSkill(skillId, 1);
								if (skill != null)
								{
									String icon = skill.getIcon();
									if (icon == null || icon.isEmpty()) icon = "icon.skill0000";
									sb.append("<tr>");
									sb.append("<td width=40><img src=\"" + icon + "\" width=32 height=32></td>");
									sb.append("<td width=200><font color=\"CDB67F\">" + skill.getName() + "</font></td>");
									sb.append("<td width=80 align=center><button value=\"Quitar\" action=\"bypass _bbsbuff;scheme;remove;" + schemeName + ";" + skillId + "\" width=65 height=20 back=\"L2UI_CH3.Btn_BF_Down\" fore=\"L2UI_CH3.Btn_BF\"></td>");
									sb.append("</tr>");
									sb.append("<tr><td height=5></td></tr>");
								}
							}
						}
						returnHtml = returnHtml.replace("%scheme_name%", schemeName);
						returnHtml = returnHtml.replace("%scheme_skills%", sb.toString());
					}
					else if (action.equalsIgnoreCase("add"))
					{
						String skillData = buypassOptions[3];
						if (skillData.contains(","))
						{
							skillData = skillData.split(",")[0];
						}
						final int skillId = Integer.parseInt(skillData);
						final List<Integer> skillIds = new ArrayList<>(SchemeBufferTable.getInstance().getScheme(player.getObjectId(), schemeName));
						if (!skillIds.contains(skillId))
						{
							if (skillIds.size() >= 40)
							{
								player.sendMessage("Has alcanzado el limite de buffs para este perfil.");
							}
							else
							{
								skillIds.add(skillId);
								SchemeBufferTable.getInstance().setScheme(player.getObjectId(), schemeName, skillIds);
								player.sendMessage("Habilidad añadida al perfil " + schemeName);
							}
						}
						// Volvemos a la edicion
						return onCommand("_bbsbuff;scheme;edit;" + schemeName, player);
					}
					else if (action.equalsIgnoreCase("remove"))
					{
						String skillData = buypassOptions[3];
						if (skillData.contains(","))
						{
							skillData = skillData.split(",")[0];
						}
						final int skillId = Integer.parseInt(skillData);
						final List<Integer> skillIds = new ArrayList<>(SchemeBufferTable.getInstance().getScheme(player.getObjectId(), schemeName));
						if (skillIds.remove(Integer.valueOf(skillId)))
						{
							SchemeBufferTable.getInstance().setScheme(player.getObjectId(), schemeName, skillIds);
							player.sendMessage("Habilidad quitada del perfil " + schemeName);
						}
						return onCommand("_bbsbuff;scheme;edit;" + schemeName, player);
					}
					
					if (returnHtml == null)
					{
						returnHtml = HtmCache.getInstance().getHtm(player, "data/html/CommunityBoard/Custom/" + returnPage + ".html");
					}
				}
				else
				{
					for (int i = 0; i < buffCount; i++)
					{
						final String opt = buypassOptions[i];
						if (!opt.contains(","))
						{
							continue;
						}
						
						final String[] skillOptions = opt.split(",");
						final int skillId;
						try
						{
							skillId = Integer.parseInt(skillOptions[0]);
						}
						catch (Exception e)
						{
							continue;
						}
						
						int maxLevel = SkillData.getInstance().getMaxLevel(skillId);
						int skillLevel = Integer.parseInt(skillOptions[1]);
						
						if (!player.hasPremiumStatus())
						{
							skillLevel = 1;
						}
						
						final Skill skill = SkillData.getInstance().getSkill(skillId, Math.min(skillLevel, maxLevel));
						if ((skill != null) && CommunityBoardConfig.COMMUNITY_AVAILABLE_BUFFS.contains(skill.getId()))
						{
							for (Creature target : targets)
							{
								skill.applyEffects(player, target);
								if (CommunityBoardConfig.COMMUNITYBOARD_CAST_ANIMATIONS)
								{
									player.sendPacket(new MagicSkillUse(player, target, skill.getId(), skill.getLevel(), skill.getHitTime(), skill.getReuseDelay()));
								}
							}
						}
					}
					returnHtml = HtmCache.getInstance().getHtm(player, "data/html/CommunityBoard/Custom/" + page + ".html");
				}
			}
		}
		else if (command.startsWith("_bbsheal"))
		{
			final String page = command.replace("_bbsheal;", "");
			if (player.getInventory().getInventoryItemCount(CommunityBoardConfig.COMMUNITYBOARD_CURRENCY, -1) < (CommunityBoardConfig.COMMUNITYBOARD_HEAL_PRICE))
			{
				player.sendMessage("Not enough currency!");
			}
			else
			{
				player.destroyItemByItemId(ItemProcessType.FEE, CommunityBoardConfig.COMMUNITYBOARD_CURRENCY, CommunityBoardConfig.COMMUNITYBOARD_HEAL_PRICE, player, true);
				player.setCurrentHp(player.getMaxHp());
				player.setCurrentMp(player.getMaxMp());
				player.setCurrentCp(player.getMaxCp());
				if (player.hasSummon())
				{
					player.getSummon().setCurrentHp(player.getSummon().getMaxHp());
					player.getSummon().setCurrentMp(player.getSummon().getMaxMp());
					player.getSummon().setCurrentCp(player.getSummon().getMaxCp());
				}
				
				player.updateUserInfo();
				player.sendMessage("You used heal!");
			}
			
			returnHtml = HtmCache.getInstance().getHtm(player, "data/html/CommunityBoard/Custom/" + page + ".html");
		}
		else if (command.equals("_bbsdelevel"))
		{
			if (player.getInventory().getInventoryItemCount(CommunityBoardConfig.COMMUNITYBOARD_CURRENCY, -1) < CommunityBoardConfig.COMMUNITYBOARD_DELEVEL_PRICE)
			{
				player.sendMessage("Not enough currency!");
			}
			else if (player.getLevel() == 1)
			{
				player.sendMessage("You are at minimum level!");
			}
			else
			{
				player.destroyItemByItemId(ItemProcessType.FEE, CommunityBoardConfig.COMMUNITYBOARD_CURRENCY, CommunityBoardConfig.COMMUNITYBOARD_DELEVEL_PRICE, player, true);
				final int newLevel = player.getLevel() - 1;
				player.setExp(ExperienceData.getInstance().getExpForLevel(newLevel));
				player.getStat().setLevel((byte) newLevel);
				player.setCurrentHpMp(player.getMaxHp(), player.getMaxMp());
				player.setCurrentCp(player.getMaxCp());
				player.broadcastUserInfo();
				player.checkPlayerSkills(); // Adjust skills according to new level.
				returnHtml = HtmCache.getInstance().getHtm(player, "data/html/CommunityBoard/Custom/delevel/complete.html");
			}
		}
		else if (command.startsWith("_bbspremium"))
		{
			final String fullBypass = command.replace("_bbspremium;", "");
			final String[] buypassOptions = fullBypass.split(",");
			final int premiumDays = Integer.parseInt(buypassOptions[0]);
			int price = 0;
			switch (premiumDays)
			{
				case 1:
				{
					price = 100;
					break;
				}
				case 15:
				{
					price = 650;
					break;
				}
				case 30:
				{
					price = 1000;
					break;
				}
				default:
				{
					price = CommunityBoardConfig.COMMUNITY_PREMIUM_PRICE_PER_DAY * premiumDays;
					break;
				}
			}
			
			if ((premiumDays < 1) || (premiumDays > 30) || (player.getInventory().getInventoryItemCount(CommunityBoardConfig.COMMUNITY_PREMIUM_COIN_ID, -1) < price))
			{
				player.sendMessage("Not enough currency!");
			}
			else
			{
				player.destroyItemByItemId(ItemProcessType.FEE, CommunityBoardConfig.COMMUNITY_PREMIUM_COIN_ID, price, player, true);
				PremiumManager.getInstance().addPremiumTime(player.getAccountName(), premiumDays, TimeUnit.DAYS);
				player.sendMessage("Your account will now have premium status until " + new SimpleDateFormat("dd.MM.yyyy HH:mm").format(PremiumManager.getInstance().getPremiumExpiration(player.getAccountName())) + ".");
				if (PremiumSystemConfig.PC_CAFE_RETAIL_LIKE)
				{
					PcCafePointsManager.getInstance().run(player);
				}
				
				returnHtml = HtmCache.getInstance().getHtm(player, "data/html/CommunityBoard/Custom/premium/thankyou.html");
			}
		}
		
		if (returnHtml != null)
		{
			if (CommunityBoardConfig.CUSTOM_CB_ENABLED)
			{
				returnHtml = returnHtml.replace("%navigation%", navigation);
			}
			
			if (returnHtml.contains("%buffer_schemes%"))
			{
				final StringBuilder sb = new StringBuilder();
				final Map<String, List<Integer>> schemes = SchemeBufferTable.getInstance().getPlayerSchemes(player.getObjectId());
				if ((schemes != null) && !schemes.isEmpty())
				{
					for (String schemeName : schemes.keySet())
					{
						if (schemeName == null || schemeName.isEmpty() || schemeName.equalsIgnoreCase("$s_name"))
						{
							continue;
						}
						sb.append("<tr>");
						sb.append("<td width=180 align=left><font color=\"CDB67F\">" + schemeName + "</font></td>");
						sb.append("<td width=70 align=center><button value=\"Cargar\" action=\"bypass _bbsbuff;scheme;load;" + schemeName + ";buffer/main\" width=65 height=20 back=\"L2UI_CH3.Btn_BF_Down\" fore=\"L2UI_CH3.Btn_BF\"></td>");
						sb.append("<td width=70 align=center><button value=\"Editar\" action=\"bypass _bbsbuff;scheme;edit;" + schemeName + ";buffer/main\" width=65 height=20 back=\"L2UI_CT1.Button_DF_Down\" fore=\"L2UI_CT1.Button_DF\"></td>");
						sb.append("<td width=70 align=center><button value=\"Borrar\" action=\"bypass _bbsbuff;scheme;delete;" + schemeName + ";buffer/main\" width=65 height=20 back=\"L2UI_CH3.Btn_BF_Down\" fore=\"L2UI_CH3.Btn_BF\"></td>");
						sb.append("</tr>");
						sb.append("<tr><td height=5></td></tr>");
					}
				}
				
				if (sb.length() == 0)
				{
					sb.append("<tr><td colspan=3 align=center><font color=\"888888\">No tienes perfiles guardados.</font></td></tr>");
				}
				
				returnHtml = returnHtml.replace("%buffer_schemes%", sb.toString());
			}
			
			CommunityBoardHandler.separateAndSend(returnHtml, player);
		}
		
		return false;
	}
	
	/**
	 * Gets the Favorite links for the given player.
	 * @param player the player
	 * @return the favorite links count
	 */
	private static int getFavoriteCount(Player player)
	{
		int count = 0;
		try (Connection con = DatabaseFactory.getConnection();
			PreparedStatement ps = con.prepareStatement(COUNT_FAVORITES))
		{
			ps.setInt(1, player.getObjectId());
			try (ResultSet rs = ps.executeQuery())
			{
				if (rs.next())
				{
					count = rs.getInt("favorites");
				}
			}
		}
		catch (Exception e)
		{
			LOGGER.warning(FavoriteBoard.class.getSimpleName() + ": Coudn't load favorites count for " + player);
		}
		
		return count;
	}
	
	/**
	 * Gets the registered regions count for the given player.
	 * @param player the player
	 * @return the registered regions count
	 */
	private static int getRegionCount(Player player)
	{
		return 0; // TODO: Implement.
	}
}
