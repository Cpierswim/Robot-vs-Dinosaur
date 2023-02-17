from weapon import Weapon

class Robot:
    def __init__(self, name: str) -> None:
        self.name = name
        self.health = 100
        self.weapon_list = [Weapon("Knife", 4), 
                            Weapon("Spear", 9),
                            Weapon("Harpoon", 20)]
        self.active_weapon_index = 0

    def attack(self, dinosaur) -> None:
        print(f"{self.name} is attacking {dinosaur.name}")
        self.choose_weapon()
        print("")
        print(f"The Robot {self.name} is attacked the Dinosaur {dinosaur.name} with {self.weapon_list[self.active_weapon_index].name} which has {self.weapon_list[self.active_weapon_index].attack_power} attack points")
        dinosaur.health -= self.weapon_list[self.active_weapon_index].attack_power
        if dinosaur.health > 0:
            print(f"The Dinosaur {dinosaur.name} has {dinosaur.health} HP remaining")
        else:
            dinosaur.health = 0
            print(f"The Dinosaur {dinosaur.name} has died")
        print("")

    def choose_weapon(self) -> None:
        name_found = False
        weapon_choice = ""
        while not name_found:
            weapon_choice = input(self.create_weapon_choice_input_string())
            weapon_choice = weapon_choice.lower()
            for index in range(0, len(self.weapon_list)):
                if weapon_choice == self.weapon_list[index].name.lower():
                    name_found = True
                    self.active_weapon_index = index
                    break
            if not name_found:
                print("Weapon not found. Try again")      

    def create_weapon_choice_input_string(self) -> str:
        input_string = "Which weapon would you like to use the "
        for i in range(0, len(self.weapon_list)):
            if i == len(self.weapon_list) - 1 and len(self.weapon_list) > 1:
                input_string += f", or {self.weapon_list[i].name}"
            else:
                if i == 0:
                    input_string += self.weapon_list[i].name
                else:
                    input_string += f", {self.weapon_list[i].name}"
        input_string += "? "
        return input_string