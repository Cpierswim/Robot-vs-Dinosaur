from robot import Robot
from dinosaur import Dinosaur


class Battlefield:
    def __init__(self) -> None:
        self.robot = Robot("Wall-E")
        self.dinosaur = Dinosaur("T-Rex", 10)

    def run_game(self) -> None:
        self.display_welcome()
        while self.robot.health > 0 and self.dinosaur.health > 0:
            self.battle_phase()
        self.display_winner()

    def display_welcome(self) -> None:
        print(f"The battle has begun versus the Robot {self.robot.name} and Dinosaur {self.dinosaur.name}")
        print(f"The Robot {self.robot.name} has {self.robot.health} Health Points and you will pick which weapons to use")
        print(f"The Dinosaur {self.dinosaur.name} has {self.dinosaur.health} Health Points and will attack with {self.dinosaur.attack_power} Attack Points")
        print("")
    
    def battle_phase(self) -> None:
        if self.robot.health > 0:
            self.robot.attack(self.dinosaur)
        if self.dinosaur.health > 0:
            self.dinosaur.attack(self.robot)

    def display_winner(self) -> None:
        if self.robot.health == 0 and self.dinosaur.health == 0:
            print("There is no winner, everyone has died")
        elif self.robot.health == 0:
            print(f"The Dinosaur {self.dinosaur.name} has won")
        elif self.dinosaur.health == 0:
            print(f"The Robot {self.robot.name} has won")