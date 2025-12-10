from models import Character, Enemy
from weapons import FISTS, SHORT_STICK, LONG_STICK, KNIFE, CLUB, SWORD, BOW, WHIP
from enemies import WILD_CAT, FOX, SNAKE, BOAR, ANGRY_SQUIRREL, WOLF, BADGER
from game_logic import exploration_menu, fight, fight_result, show_inventory, choose_weapon

def west_scene(player):
    print("Du gehst nach Westen.")
    print("Der Weg führt dich in die Berge. Du kommst an einer kleinen Quelle vorbei und folgst dem kleinen Bach, der aus ihr entsteht.")
    print("Der kühle Bergwind fühlt sich gut an und du läufst einfach weiter.")
    print("Du findest einen langen Stock am Wegesrand.")
    print("Du hebst ihn auf und bist froh, so etwas wie eine Waffe zu haben.")

    player.inventory["langer Stock"] = LONG_STICK
    player.current_weapon = LONG_STICK

    exploration_menu(player)

    print("Ein leises Rascheln ertönt aus einer kleinen Höhle.")

    enemy = Enemy(
        name=FOX.name,
        damage=FOX.damage,
        max_health=FOX.max_health,
        current_health=FOX.max_health,
    )

    print(f"Ein {enemy.name} steht nun vor dir auf dem Weg. Ihr schaut euch beide ungläubig an.\n")

    result = fight(player, enemy)
    fight_result(result, player, "Westen")
