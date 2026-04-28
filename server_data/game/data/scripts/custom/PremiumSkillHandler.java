package custom;

import org.l2jmobius.gameserver.model.actor.Player;
import org.l2jmobius.gameserver.model.events.Containers;
import org.l2jmobius.gameserver.model.events.EventType;
import org.l2jmobius.gameserver.model.events.holders.actor.player.OnPlayerLogin;
import org.l2jmobius.gameserver.model.events.listeners.ConsumerEventListener;
import org.l2jmobius.gameserver.model.skill.holders.SkillHolder;

/**
 * L2 Meraki: Automatizacion de Skill Spirit of Meraki (ID 9000) para usuarios VIP.
 * Corregido para version especifica de Mobius.
 * @author Antigravity
 */
public class PremiumSkillHandler
{
	private static final int PREMIUM_SKILL_ID = 9000;
	private static final int PREMIUM_SKILL_LEVEL = 2; // Nivel acordado del 50% peso
	
	protected PremiumSkillHandler()
	{
		Containers.Players().addListener(new ConsumerEventListener(Containers.Players(), EventType.ON_PLAYER_LOGIN, (OnPlayerLogin event) -> onPlayerLogin(event), this));
	}
	
	private void onPlayerLogin(OnPlayerLogin event)
	{
		final Player player = event.getPlayer();
		if (player == null)
		{
			return;
		}
		
		final SkillHolder premiumSkill = new SkillHolder(PREMIUM_SKILL_ID, PREMIUM_SKILL_LEVEL);
		
		if (player.hasPremiumStatus())
		{
			// Si es VIP y no tiene la skill de nivel correcto, se la damos.
			if (player.getSkillLevel(PREMIUM_SKILL_ID) != PREMIUM_SKILL_LEVEL)
			{
				player.addSkill(premiumSkill.getSkill(), true);
				player.sendSkillList();
				player.sendMessage("¡Bienvenido Meraki! Tu bendicion VIP (Spirit of Meraki) ha sido activada.");
			}
		}
		else
		{
			// Si no es VIP y tiene la skill, se la quitamos.
			if (player.getSkillLevel(PREMIUM_SKILL_ID) > 0)
			{
				player.removeSkill(PREMIUM_SKILL_ID, true);
				player.sendSkillList();
				player.sendMessage("Tu suscripcion VIP ha expirado. Spirit of Meraki ha sido desactivado.");
			}
		}
	}
	
	public static void main(String[] args)
	{
		new PremiumSkillHandler();
	}
}
