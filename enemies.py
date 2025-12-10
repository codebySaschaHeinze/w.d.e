from models import Enemy

WILD_CAT = Enemy(
    name="wilde Katze",
    damage=(10, 14),
    max_health=25,
    current_health=25
)

FOX = Enemy(
    name="Fuchs",
    damage=(13, 17),
    max_health=30,
    current_health=30
)

SNAKE = Enemy(
    name="Schlange",
    damage=(13, 17),
    max_health=35,
    current_health=35
)

BOAR = Enemy(
    name="Wildschwein",
    damage=(36, 44),
    max_health=80,
    current_health=80
)

ANGRY_SQUIRREL = Enemy(
    name="wütendes Eichhörnchen",
    damage=(5, 9),
    max_health=15,
    current_health=15
)

WOLF = Enemy(
    name="Wolf",
    damage=(32, 38),
    max_health=70,
    current_health=70
)

BADGER = Enemy(
    name="Dachs",
    damage=(17, 23),
    max_health=30,
    current_health=30
)