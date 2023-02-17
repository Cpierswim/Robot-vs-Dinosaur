from robot import Robot
from dinosaur import Dinosaur


class Battlefield:
    def __init__(self) -> None:
        self.robot = Robot("Wall-E")
        self.dinosaur = Dinosaur("T-Rex", 10)

    def run_game() -> None:
        pass

    def display_welcome() -> None:
        pass
    
    def battle_phase() -> None:
        pass

    def display_winner() -> None:
        pass