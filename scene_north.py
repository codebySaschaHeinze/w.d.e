from models import Character, Enemy
from weapons import FISTS, SHORT_STICK, LONG_STICK, KNIFE, CLUB, SWORD, BOW, WHIP
from enemies import WILD_CAT, FOX, SNAKE, BOAR, ANGRY_SQUIRREL, WOLF, BADGER
from game_logic import exploration_menu, fight, fight_result, show_inventory, choose_weapon

def north_scene(player):
    print("Du gehst nach Norden.")
    print("Der Pfad wird schmaler, die Bäume stehen dichter beieinander und der Wind wird kälter.")
    print("Mitten im dunklen Wald findest du einen kurzen Stock am Wegesrand.")
    print("Du hebst ihn auf und prüfst sein Gewicht.")

    player.inventory["kurzer Stock"] = SHORT_STICK
    player.current_weapon = SHORT_STICK

    print("Du nimmst den kurzen Stock in die Hand und setzt deinen Weg fort.\n")

    exploration_menu(player)

    print("Ein leises Rascheln ertönt aus dem Geäst neben dir.")
    print("Zwei funkelnde Augen starren dich an...\n")

    enemy = Enemy(
        name=ANGRY_SQUIRREL.name,
        damage=ANGRY_SQUIRREL.damage,
        max_health=ANGRY_SQUIRREL.max_health,
        current_health=ANGRY_SQUIRREL.max_health,
    )

    print(f"Ein {enemy.name} springt aus dem Gebüsch und faucht dich an!\n")

    result = fight(player, enemy)
    fight_result(result, player, "Norden")
