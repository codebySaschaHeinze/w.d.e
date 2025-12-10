from models import Weapon

FISTS = Weapon(
    name="Fäuste",
    damage=(1,3),
    weapon_range=5,
    weapon_type="Nahkampf"
)

SHORT_STICK = Weapon(
    name="kurzer Stock",
    damage=(3, 8),
    weapon_range=10,
    weapon_type="Schlag"
)

LONG_STICK = Weapon(
    name="langer Stock",
    damage=(8, 12),
    weapon_range=15,
    weapon_type="Schlag"
)

KNIFE = Weapon(
    name="Messer",
    damage=(8, 12),
    weapon_range=5,
    weapon_type="Stich"
)

CLUB = Weapon(
    name="Keule",
    damage=(13, 17),
    weapon_range=10,
    weapon_type="Wucht"
)

SWORD = Weapon(
    name="Schwert",
    damage=(18, 22),
    weapon_range=10,
    weapon_type="Klinge"
)

BOW = Weapon(
    name="Bogen",
    damage=(18, 22),
    weapon_range=35,
    weapon_type="Fernkampf"
)

WHIP = Weapon(
    name="Peitsche",
    damage=(25, 35),
    weapon_range=25,
    weapon_type="Fernkampf"
)