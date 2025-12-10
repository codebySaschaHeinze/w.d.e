import random
from models import Character


# _________________________ INVENTAR ANZEIGEN LASSEN _________________________
def show_inventory(player: Character):
    if not player.inventory:
        print("Dein Inventar ist leer.\n")
        return

    print("Dein Inventar:")

    for name, weapon in player.inventory.items():
        marker = ""
        if weapon is player.current_weapon:
            marker = " (ausgerüstet)"
        min_dmg, max_dmg = weapon.damage
        base_dmg = (min_dmg + max_dmg) // 2 

        print(f"- {name}{marker} -> Schaden: +/-{base_dmg}, Reichweite: {weapon.weapon_range}")


    print()


# _________________________ WAFFEN-AUSWAHL _________________________
def choose_weapon(player: Character):
    if not player.inventory:
        print("Dein Inventar ist leer.\n")
        return

    print("Welche Waffe möchtest du ausrüsten?")

    weapons = list(player.inventory.values())

    for i, weapon in enumerate(weapons, start=1):
        marker = ""
        if weapon is player.current_weapon:
            marker = "(ausgerüstet)"
        min_dmg, max_dmg = weapon.damage
        base_dmg = (min_dmg + max_dmg) // 2

        print(f"{i}) {weapon.name} {marker} | Schaden: +/-{base_dmg}, Reichweite: {weapon.weapon_range}")


    choice = input("> ")

    while not choice.isdigit() or not (1 <= int(choice) <= len(weapons)):
        print("Ungültige Eingabe.")
        choice = input("Bitte die entsprechende Zahl eingeben:\n> ")

    selected_weapon = weapons[int(choice) - 1]
    player.current_weapon = selected_weapon

    print(f"\nDu hast nun {selected_weapon.name} ausgerüstet.\n")


# _________________________ AUßERHALB DES KAMPFES _________________________
def exploration_menu(player: Character):
    while True:
        print("Was möchtest du tun?")
        print("1) Weiterlaufen")
        print("2) Inventar ansehen")
        print("3) Waffe wechseln")

        choice = input("> ")

        if choice == "1":
            print("Du läufst weiter...\n")
            return "continue"

        elif choice == "2":
            show_inventory(player)

        elif choice == "3":
            choose_weapon(player)

        else:
            print("Ungültige Eingabe. Bitte wähle 1, 2 oder 3.\n")


# _________________________ KAMPF _________________________

def fight(player, enemy):

    while player.current_health > 0 and enemy.current_health > 0:

        print(f"Deine HP: {player.current_health}\nDeine ausgerüstete Waffe: {player.current_weapon.name}\n{enemy.name} HP: {enemy.current_health}")
        print("Was möchtest du tun?")
        print("1) Inventar ansehen")
        print("2) Kämpfen")
        print("3) Flüchten")

        choice = input("> ")

        if choice == "1":
            show_inventory(player)
            choose_weapon(player)
            
        elif choice == "2":
            print(f"\nDu greifst {enemy.name} an!")

            min_dmg, max_dmg = player.current_weapon.damage
            player_damage = random.randint(min_dmg, max_dmg)
            enemy.current_health -= player_damage

            print(f"{enemy.name} verliert {player_damage} HP!")

            if enemy.current_health <= 0:
                print(f"\nDu hast {enemy.name} besiegt!\n")
                return "won"
            
            print(f"{enemy.name} greift dich an!")

            min_dmg, max_dmg = enemy.damage
            enemy_damage = random.randint(min_dmg, max_dmg)
            player.current_health -= enemy_damage

            print(f"Du verlierst {enemy_damage} HP!\n")

            if player.current_health <= 0:
                print("\nDu wurdest besiegt...\n")
                return "lost"
            

        elif choice == "3":
            print(f"\nDu flüchtest vor {enemy.name}!\n")
            return "escaped"

        else:
            print("\nUngültige Eingabe. Bitte wähle 1, 2 oder 3.\n")
            continue


# _________________________ KAMPF-ERGEBNIS _________________________

def fight_result(result, player, direction_name):
    if result == "won":
        print(f"Du atmest schwer, aber du lebst noch. Der Weg nach {direction_name} liegt wieder ruhig vor dir.\n")
        exploration_menu(player)

    elif result == "escaped":
        print("Du rennst zurück, bis du wieder an der Kreuzung bist und schläfst erschöpft ein.\n")

    elif result == "lost":
        print("Deine Reise endet hier...\n")

