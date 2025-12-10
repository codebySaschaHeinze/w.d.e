class Character:
    def __init__(self, name, current_health, current_weapon):
        self.name = name
        self.max_health = 100
        self.current_health = current_health
        self.current_weapon = current_weapon
        self.inventory = {}


class Enemy:
    def __init__(self, name, damage, max_health, current_health):
        self.name = name
        self.damage = damage
        self.max_health = max_health
        self.current_health = current_health


class Weapon:
    def __init__(self, name, damage, weapon_range, weapon_type):
        self.name = name
        self.damage = damage
        self.weapon_range = weapon_range
        self.weapon_type = weapon_type