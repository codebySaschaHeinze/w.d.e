from models import Character, Enemy
from weapons import FISTS, SHORT_STICK, LONG_STICK, KNIFE, CLUB, SWORD, BOW, WHIP
from enemies import WILD_CAT, FOX, SNAKE, BOAR, ANGRY_SQUIRREL, WOLF, BADGER
from game_logic import exploration_menu, fight, fight_result, show_inventory, choose_weapon

def east_scene(player):
    print("Du gehst nach Osten.")
    print("Die Bäume werden nach und nach weniger und in der Ferne hörst du ein fast schon beruhigendes Rauschen.")
    print("Du läufst bedächtig weiter und siehst irgendwann das Meer. Der Vollmond spiegelt sich mystisch auf der Wasseroberfläche.")
    print("Neugierig erkundest du deine Umgebung.")
    print("Du findest einen langen Stock im Sand.")
    print("Du hebst ihn auf und prüfst sein Gewicht.")

    player.inventory["langer Stock"] = LONG_STICK
    player.current_weapon = LONG_STICK

    exploration_menu(player)

    print("Du hörst zwischen den Strandpflanzen ein Rascheln.")
    print("Plötzlich schießt etwas in deine Richtung und liegt vor dir.\n")

    enemy = Enemy(
        name=SNAKE.name,
        damage=SNAKE.damage,
        max_health=SNAKE.max_health,
        current_health=SNAKE.max_health,
    )

    print(f"Eine {enemy.name} springt aus dem Gebüsch und faucht dich an!\n")

    result = fight(player, enemy)
    fight_result(result, player, "Osten")