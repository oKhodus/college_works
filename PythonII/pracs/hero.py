class Hero:
    def __init__(self, name, damage, hp=100, max_hp=100):
        """Initialize name, damage, hp and max_hp

        Args:
            name (str): Name of hero for example - "Warrior"
            damage (int): Damage of hero for example - 12 
            hp (int, optional): Health Points of hero. Defaults to 100.
            max_hp (int, optional): Max of Health Points. Defaults to 100.
        """
        self.name = name
        self.damage = damage
        self.hp = hp
        self.max_hp = max_hp

    def hit(self, target: str):
        """Hitting another hero (target) for example - Mage hits Warrior and Warrior loses 8 HP

        Args:
            target (str): Target of Hero, which he will hit

        Returns:
            str: Returns string if hero killed and string how much damage hero made to target 
        """
        target.hp -= self.damage
        if target.hp <= 0:
            return f"{target.name} loses {self.damage} hp\n{self.name} killed {target.name}"
        return f"{target.name} loses {self.damage} hp"

    def set_damage(self, value: int):
        """Setting damage to specific hero

        Args:
            value (int): how much damage will setted for hero
        """
        if value > 0:
            self.damage = value
        else:
            print(f"Value should be a positive")

    def heal(self, value: int):
        """Healing the specific hero (adding helth points)

        Args:
            value (int): Value of health points, which hero get

        Returns:
            str: Returns string how much HP hero will get
        """
        self.hp += value
        if self.hp > self.max_hp:
            self.hp = self.max_hp
            return f"{self.name} gains {value} hp and reached maximum of hp (100 HP)"
        return f"{self.name} gains {value} hp"


hero1 = Hero("Warrior", 10)
hero2 = Hero("Mage", 8)

currentHP = "HP of all charachters:\n--- {}: {}HP\n--- {}: {}HP\n"

print(currentHP.format(hero1.name, hero1.hp, hero2.name, hero2.hp))

print(
    f"Move 1:\n*{hero1.hit(hero2)}, \n*{hero2.name}'s used potion to increase his damage to (12 dmg)\n",
)

hero2.set_damage(12)

print(currentHP.format(hero1.name, hero1.hp, hero2.name, hero2.hp))
print(f"*{hero2.hit(hero1)}")
print(f'*{hero1.name}\'s used item "Holy Bible" to heal himself')

print(f"*{hero1.heal(32)}\n")

print(currentHP.format(hero1.name, hero1.hp, hero2.name, hero2.hp))
