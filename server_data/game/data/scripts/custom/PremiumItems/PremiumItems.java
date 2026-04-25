package custom.PremiumItems;

import java.util.concurrent.TimeUnit;

import org.l2jmobius.gameserver.handler.IItemHandler;
import org.l2jmobius.gameserver.handler.ItemHandler;
import org.l2jmobius.gameserver.managers.PremiumManager;
import org.l2jmobius.gameserver.model.actor.Playable;
import org.l2jmobius.gameserver.model.actor.Player;
import org.l2jmobius.gameserver.model.item.enums.ItemProcessType;
import org.l2jmobius.gameserver.model.item.instance.Item;
import org.l2jmobius.gameserver.model.script.Script;

/**
 * Custom Item Handler to activate Premium status using VIP Meraki items.
 * @author Antigravity
 */
public class PremiumItems extends Script implements IItemHandler
{
	public PremiumItems()
	{
		ItemHandler.getInstance().registerHandler(this);
	}
	
	@Override
	public boolean onItemUse(Playable playable, Item item, boolean forceUse)
	{
		if (!playable.isPlayer())
		{
			return false;
		}
		
		final Player player = playable.asPlayer();
		if (player == null)
		{
			return false;
		}
		
		int days = 0;
		switch (item.getId())
		{
			case 9500: // VIP Meraki - 7 Days
				days = 7;
				break;
			case 9501: // VIP Meraki - 15 Days
				days = 15;
				break;
			case 9502: // VIP Meraki - 30 Days
				days = 30;
				break;
		}
		
		if (days > 0)
		{
			PremiumManager.getInstance().addPremiumTime(player.getAccountName(), days, TimeUnit.DAYS);
			player.setPremiumStatus(true);
			player.destroyItem(ItemProcessType.DESTROY, item, player, true);
			player.sendMessage("¡Felicidades! Tu cuenta ahora tiene estado Premium por " + days + " días.");
			player.sendMessage("Usa el comando .premium para ver los detalles de tu suscripción.");
			
			player.broadcastUserInfo();
			return true;
		}
		
		return false;
	}
	
	public static void main(String[] args)
	{
		new PremiumItems();
	}
}
