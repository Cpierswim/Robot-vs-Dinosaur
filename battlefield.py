from robot import Robot
from dinosaur import Dinosaur
from herd import Herd
from fleet import fleet


class Battlefield:
    def __init__(self) -> None:
        self.robot = Robot("Wall-E")
        self.dinosaur = Dinosaur("T-Rex", 10)
        self.herd = Herd()
        self.fleet = fleet()

    def run_game(self) -> None:
        self.display_welcome()
        round = 1
        while not (self.robots_dead() or self.dinosaurs_dead()):
            print(f"-----------ROUND {round}: BEGIN-----------")
            self.display_everyone_status()
            self.battle_phase()
            round += 1
        self.display_winner()

    def display_everyone_status(self) -> None:
        for robot in self.fleet.robots:
            print(f"Robot {robot.name} has {robot.health}HP")
        for dinosaur in self.herd.dinosaurs:
            print(f"Dinosaur {dinosaur.name} has {dinosaur.health}HP")
        print("")

    def display_welcome(self) -> None:
        print("The battle has begun between:")
        fleet_string = "The Robot Fleet of: "
        for i in range(0, len(self.fleet.robots)):
            if i == len(self.fleet.robots) - 1 and len(self.fleet.robots) > 1:
                fleet_string += f", and {self.fleet.robots[i].name}"
            else:
                if i == 0:
                    fleet_string += self.fleet.robots[i].name
                else:
                    fleet_string += f", {self.fleet.robots[i].name}"
        print(fleet_string)

        herd_string = "The Dinosaur Herd of :"
        for i in range(0, len(self.herd.dinosaurs)):
            if i == len(self.herd.dinosaurs) - 1 and len(self.herd.dinosaurs) > 1:
                herd_string += f", and {self.herd.dinosaurs[i].name}" + f" (attack:{self.herd.dinosaurs[i].attack_power})"
            else:
                if i == 0:
                    herd_string += self.herd.dinosaurs[i].name + f" (attack:{self.herd.dinosaurs[i].attack_power})"
                else:
                    herd_string += f", {self.herd.dinosaurs[i].name}" + f" (attack:{self.herd.dinosaurs[i].attack_power})"
        print(herd_string)
        '''print(f"The Robot {self.robot.name} has {self.robot.health} Health Points and you will pick which weapons to use")
        print(f"The Dinosaur {self.dinosaur.name} has {self.dinosaur.health} Health Points and will attack with {self.dinosaur.attack_power} Attack Points")
        '''
        print("")
    
    def battle_phase(self) -> None:
        '''if self.robot.health > 0:
            self.robot.attack(self.dinosaur)
        if self.dinosaur.health > 0:
            self.dinosaur.attack(self.robot)'''
        self.robots_turn()
        self.dinosaurs_turn()

    def robots_dead(self) -> bool:
        for robot in self.fleet.robots:
            if robot.health > 0:
                return False
        return True

    def dinosaurs_dead(self) -> bool:
        for dinosaur in self.herd.dinosaurs:
            if dinosaur.health > 0:
                return False
        return True

    def display_winner(self) -> None:
        '''if self.robot.health == 0 and self.dinosaur.health == 0:
            print("There is no winner, everyone has died")
        elif self.robot.health == 0:
            print(f"The Dinosaur {self.dinosaur.name} has won")
        elif self.dinosaur.health == 0:
            print(f"The Robot {self.robot.name} has won")'''
        if self.robots_dead():
            print("")
            print("THE DINOSAUR HERD WINS!")
        if self.dinosaurs_dead():
            print("")
            print("THE ROBOT FLEET WINS!")

    def robots_turn(self) -> None:
        for robot in self.fleet.robots:
            for dinosaur in self.herd.dinosaurs:
                if robot.health > 0 and dinosaur.health > 0:
                    robot.attack(dinosaur)

    def dinosaurs_turn(self) -> None:
        for dinosaur in self.herd.dinosaurs:
            for robot in self.fleet.robots:
                if dinosaur.health > 0 and robot.health > 0:
                    dinosaur.attack(robot)
