class Hero:
    def __init__(self, name, damage, hp=100, max_hp=100):
        self.name = name
        self.damage = damage
        self.hp = hp
        self.max_hp = max_hp

    def hit(self, target):
        target.hp -= self.damage
        if target.hp <= 0:
            return f"{self.name} killed {target.name}"
        return f"{target.name} loses {self.damage} hp"

    def set_damage(self, value):
        if value > 0:
            self.damage = value
        else:
            print(f"Value should be a positive")

    def heal(self, value):
        self.hp += value
        if self.hp > self.max_hp:
            self.hp = self.max_hp
            return f"{self.name} gains {value} hp"
        return f"{self.name} gains {value} hp"


hero1 = Hero("Warrior", 10)
hero2 = Hero("Mage", 8)

currentHP = "HP of all charachters:\n--- {}: {}HP\n--- {}: {}HP\n"

print(currentHP.format(hero1.name, hero1.hp, hero2.name, hero2.hp))

print(
    f"Move 1:\n*{hero1.hit(hero2)}, \n*{hero2.name}'s used special item to increase own damage",
)

hero2.set_damage(12)

print(currentHP.format(hero1.name, hero1.hp, hero2.name, hero2.hp))
print(hero2.hit(hero1))
print(hero1.heal(32))
