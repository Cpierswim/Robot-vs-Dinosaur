from weapon import Weapon

class Robot:
    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Knife", 4)

    def attack(self, dinosaur) -> None:
        print(f"The Robot {self.name} is attacking the Dinosaur {dinosaur.name} with {self.active_weapon.name} which has {self.active_weapon.attack_power} attack points")
        dinosaur.health -= self.active_weapon.attack_power
        if dinosaur.health > 0:
            print(f"The Dinosaur {dinosaur.name} has {dinosaur.health} HP remaining")
        else:
            dinosaur.health = 0
            print(f"The Dinosaur {dinosaur.name} has died")
        print("")