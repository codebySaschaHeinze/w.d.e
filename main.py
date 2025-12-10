from models import Character
from weapons import FISTS, SHORT_STICK, LONG_STICK, KNIFE, CLUB, SWORD, BOW, WHIP
from game_logic import exploration_menu, fight, fight_result, show_inventory, choose_weapon
from scene_north import north_scene
from scene_east import east_scene
from scene_south import south_scene
from scene_west import west_scene


# _________________________ INTRO _________________________
def intro():
    print(
        'Du wachst leicht benebelt auf einer Kreuzung im Wald auf.\n'
        'Alles um dich herum wird nur von schwachem Mondlicht beleuchtet.\n'
        'Du weißt nicht wer du bist und wie du hierher gekommen bist.\n'
        'In deiner Tasche findest du einen Kompass und einen Zettel, auf dem steht:\n\n'
        '"Finde den Schatz oder gehe als Feigling nachhause."\n'
    )


# _________________________ SPIELERNAME-AUSWAHL _________________________
def get_player_name():
    name = input("Wie denkst du, ist dein Name? ")

    while not name.isalpha():
        print("Der Name darf nur aus Buchstaben bestehen!")
        name = input("Versuch's nochmal: ")

    print(f"{name}? Ein ungewöhnlicher Name. Nun gut. Deine Reise beginnt!\n")
    return name


# _________________________ WEG-AUSWAHL _________________________
def choose_way():
    valid_ways = ["Norden", "Osten", "Süden", "Westen"]
    way = input("Welchen Weg wirst du gehen? Norden/Osten/Süden/Westen:\n")

    while way not in valid_ways:
        print(
            "Sehr witzig! Entscheide dich für einen der vier Wege und "
            "dich erwartet unermesslicher Reichtum (wahrscheinlich)."
        )
        way = input("Norden/Osten/Süden/Westen:\n")

    if way == "Norden":
        print(f"Nach {way}? Du hast anscheinend vor nichts Angst!\n")
    elif way == "Osten":
        print(f"Nach {way}? Mut hast du, das muss man dir lassen!\n")
    elif way == "Süden":
        print(f"Nach {way}? Scheint so, als würdest du jedem Weg trotzen!\n")
    elif way == "Westen":
        print(f"Nach {way}? Du stürzt dich echt ohne Zögern ins Abenteuer!\n")

    return way


# _________________________ SPIELABLAUF _________________________
def main():

    intro()
    char_name = get_player_name()
    player = Character(
        name=char_name,
        current_health=100,
        current_weapon=FISTS
    )

    player.inventory["Fäuste"] = FISTS

    way = choose_way()

    if way == "Norden":
        north_scene(player)
    elif way == "Osten":
        east_scene(player)
    elif way == "Süden":
        south_scene(player)
    elif way == "Westen":
        west_scene(player)
     


if __name__ == "__main__":
    main()
