from robot import Robot

class Dinosaur:
    def __init__(self, name: str, attack_power: int) -> None:
        self.name = name
        self.attack_power = attack_power
        self.health = 0
    
    def attack(self, robot: Robot) -> None:
        print(f"The Dinosaur {self.name} is attacking the Robot {robot.name} with  {self.attack_power} attack points")
        robot.health -= self.attack_power
        if robot.health > 0:
            print(f"The Robot {robot.name} has {robot.health} HP remaining")
        else:
            robot.health = 0
            print(f"The Robot {robot.name} has deactivated")