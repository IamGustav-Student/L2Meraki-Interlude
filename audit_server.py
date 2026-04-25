import os
import configparser

def check_exploit(condition, name, severity, suggestion):
    status = "X DANGER" if condition else "OK SAFE"
    print(f"[{status}] {name}")
    if condition:
        print(f"    Severity: {severity}")
        print(f"    Fix: {suggestion}\n")
    return condition

def main():
    print("========================================")
    print(" L2 MERAKI: SERVER EXPLOIT & BUG AUDIT  ")
    print("========================================")
    
    # Check General.ini
    general_path = "server_data/game/config/General.ini"
    rates_path = "server_data/game/config/Rates.ini"
    
    with open(general_path, 'r', encoding='utf-8') as f:
        general_content = f.read()
    with open(rates_path, 'r', encoding='utf-8') as f:
        rates_content = f.read()

    # Parse configs manually since INI can have duplicate sections in L2J
    def get_val(content, key):
        for line in content.split('\n'):
            line = line.split('#')[0].strip()
            if line.startswith(key + ' '):
                return line.split('=')[1].strip()
            elif line.startswith(key + '='):
                return line.split('=')[1].strip()
        return None

    # Check 1: Admin rights
    admin_rights = get_val(general_content, 'EverybodyHasAdminRights')
    check_exploit(admin_rights == 'True', 
                 "EverybodyHasAdminRights", 
                 "CRITICAL", 
                 "Set 'EverybodyHasAdminRights = False' in General.ini")

    # Check 2: Correct Prices (Multisell exploit)
    correct_prices = get_val(general_content, 'CorrectPrices')
    check_exploit(correct_prices == 'False', 
                 "CorrectPrices (Multisell Exploit)", 
                 "HIGH", 
                 "Set 'CorrectPrices = True' in General.ini")

    # Check 3: Multiple Item Drop (The bag explosion bug)
    multi_drop = get_val(general_content, 'MultipleItemDrop')
    death_amount = float(get_val(rates_content, 'DeathDropAmountMultiplier') or 1)
    
    bag_explosion = multi_drop == 'True' and death_amount >= 5
    check_exploit(bag_explosion, 
                 "Drop Bag Explosion (Visual Bug/Lag)", 
                 "MEDIUM", 
                 f"You have DeathDropAmountMultiplier={death_amount}. If a monster drops 1 armor, it will drop {int(death_amount)} separate armors (bags) on the floor. Set 'MultipleItemDrop = False' in General.ini to prevent non-stackable items from dropping multiple physical copies, OR lower the Amount Multiplier.")

    # Check 4: Rate Overlap Exploit
    death_chance = float(get_val(rates_content, 'DeathDropChanceMultiplier') or 1)
    overlap = death_amount > 5 and death_chance > 5
    check_exploit(overlap, 
                 "Rate Overlap Exploit (Economy Crash)", 
                 "HIGH", 
                 f"You have Chance x{death_chance} AND Amount x{death_amount}. This means a 10% drop chance becomes 100%, AND it drops {int(death_amount)} items instead of 1. Total multiplier is effectively x{death_chance * death_amount}! Consider lowering Amount and keeping Chance high.")

    # Check 5: AutoLoot
    auto_loot = get_val(general_content, 'AutoLoot')
    check_exploit(auto_loot == 'False' and bag_explosion,
                  "No AutoLoot with High Drops (Server Lag)",
                  "MEDIUM",
                  "If players kill mobs that drop 20 bags each and don't pick them up, the server will lag due to entity overload. Set 'AutoLoot = True' or reduce drop amounts.")
                  
    print("========================================")
    print(" AUDIT COMPLETE ")
    print("========================================")

if __name__ == "__main__":
    main()
