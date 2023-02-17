from robot import Robot
from dinosaur import Dinosaur


class Battlefield:
    def __init__(self) -> None:
        self.robot = Robot("Wall-E")
        self.dinosaur = Dinosaur("T-Rex", 10)

    def run_game(self) -> None:
        pass

    def display_welcome(self) -> None:
        print(f"The battle has begun versus the Robot {self.robot.name} and Dinosaur {self.dinosaur.name}")
    
    def battle_phase(self) -> None:
        pass

    def display_winner(self) -> None:
        pass