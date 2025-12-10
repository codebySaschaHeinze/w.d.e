from models import Character, Enemy
from weapons import FISTS, SHORT_STICK, LONG_STICK, KNIFE, CLUB, SWORD, BOW, WHIP
from enemies import WILD_CAT, FOX, SNAKE, BOAR, ANGRY_SQUIRREL, WOLF, BADGER
from game_logic import exploration_menu, fight, fight_result, show_inventory, choose_weapon

def south_scene(player):
    print("Du gehst nach Süden.")
    print("Der Weg wird breiter und die Bäume weniger. Der Vollmond schaut auf dich und die Felder um dich herum hinab.")
    print("Du hast das Gefühl, als wärst du schonmal hier gewesen und schaust dich neugierig um.")
    print("Du findest einen kurzen Stock am Wegesrand.")
    print("Du hebst ihn auf, fuchtelst mit ihm herum und fühlst dich ein wenig sicherer.")

    player.inventory["kurzer Stock"] = SHORT_STICK
    player.current_weapon = SHORT_STICK

    exploration_menu(player)

    print("Ein leises Rascheln ertönt aus einem Gebüsch in deiner Nähe.")

    enemy = Enemy(
        name=WILD_CAT.name,
        damage=WILD_CAT.damage,
        max_health=WILD_CAT.max_health,
        current_health=WILD_CAT.max_health,
    )

    print(f"Eine {enemy.name} steht nun vor dir auf dem Weg. Sie ist ebenso flauschig wie agressiv.\n")

    result = fight(player, enemy)
    fight_result(result, player, "Süden")
