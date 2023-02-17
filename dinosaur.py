from robot import Robot

class Dinosaur:
    def __init__(self, name: str, attack_power: int) -> None:
        self.name = name
        self.attack_power = attack_power
        self.health = 0
    
    def attack(self, robot: Robot) -> None:
        pass