package custom.GlobalGK;

import org.l2jmobius.gameserver.model.actor.Npc;
import org.l2jmobius.gameserver.model.actor.Player;
import org.l2jmobius.gameserver.model.script.Script;

/**
 * Global Gatekeeper Script for L2 Meraki
 * @author Antigravity
 */
public class GlobalGK extends Script
{
	// NPCs registrados (Bella y Fiorella para la prueba)
	private static final int[] GK_IDS = {50009};
	
	public GlobalGK()
	{
		for (int id : GK_IDS)
		{
			addStartNpc(id);
			addTalkId(id);
			addFirstTalkId(id);
		}
	}
	
	@Override
	public String onEvent(String event, Npc npc, Player player)
	{
		if (event.equalsIgnoreCase("test_teleport"))
		{
			// Teletransportar al centro de Giran
			player.teleToLocation(83336, 147972, -3404);
			player.sendMessage("¡Sistema de Teleport por Script FUNCIONAL!");
			return null;
		}
		return null;
	}
	
	@Override
	public String onFirstTalk(Npc npc, Player player)
	{
		// Esto sobreescribe el diálogo inicial del NPC
		return npc.getId() + ".htm";
	}
	
	public static void main(String[] args)
	{
		new GlobalGK();
	}
}
