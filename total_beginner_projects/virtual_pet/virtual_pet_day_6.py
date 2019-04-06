class PetFood:
    def __init__(self, food_name, tastiness, fillingness):
        self.food_name = food_name
        self.tastiness = tastiness
        self.fillingness = fillingness

class OurPet:
    def __init__(self, pet_name, starting_happiness, starting_hunger):
        self.pet_name = pet_name
        self.happiness = starting_happiness
        self.hunger = starting_hunger

    def eat(self, pet_food):
        if pet_food.tastiness > 70:
            self.dance()
            self.happiness += 30
        elif pet_food.tastiness > 40:
            self.happiness += 15
        elif pet_food.tastiness > 20:
            self.happiness -= 10
        else:
            self.happiness -= 30
        print(f"{self.pet_name} eats the {pet_food.food_name}.")
        self.hunger -= pet_food.fillingness
        self.report_happiness()

    def report_happiness(self):
        if self.happiness >= 80:
            print(f"{self.pet_name} seems ecstatic!!")
        elif self.happiness >= 50:
            print(f"{self.pet_name} seems in high spirits.")
        elif self.happiness >= 25:
            print(f"{self.pet_name} seems kind of down.")
        else:
            print(f"{self.pet_name} seems mad depressed.")

    def play_with(self, toy):
        if self.happiness < 50:
            print(f"{self.pet_name} isn't in the mood to play...")
            return
        if self.hunger > 60:
            print(f"{self.pet_name} is too hungry to play!")
            self.happiness -= 20
            return
        print(f"You throw the {toy}.")
        if self.happiness >= 80:
            print(
                    f"{self.pet_name} retrieves the {toy} with "
                    "lightning speed!")
        elif self.happiness >= 70:
            print(
                    f"{self.pet_name} takes their time retrieving the "
                    f"{toy} while waggging their tail(?).")
        else:
            print(
                    f"{self.pet_name} watches the {toy} fall and looks "
                    "at you dumbly.")
        self.hunger += 20

    def dance(self):
        print(f"{self.pet_name} does a dance.")


class GameState:
    def __init__(self):
        self.game_over = False
        self.poop_on_floor = False
        self.pets = {}
        self.foods = {}
        self.command_map = {
                "feed": self.feed_pet, "play": self.play_with_pet,
                "quit": self.put_pet_to_bed, "clean": self.clean_up_poop,
                "dagger": self.cheat}

    def prompt_for_activity(self):
        if not self.poop_on_floor:
            return input("Do you want to 'feed' or 'play'? ")
        else:
            return input("Do you want to 'feed', 'play', or 'clean'? ")

    def run_command_with_pet(self, player_command, pet):
        try:
            command_callable = self.command_map[player_command]
        except KeyError:
            print(
                    "Please type either 'feed', 'play', 'quit', or "
                    "'clean'.")
        command_callable(pet)

    def feed_pet(self, pet):
        print("You can feed the pet:")
        for pet_food in self.foods.values():
            print(pet_food.food_name)
        print()
        chosen_food_name = input(
                f"What do you want to feed {pet.pet_name}? ")
        try:
            chosen_food = self.foods[chosen_food_name]
        except KeyError:
            print("You don't have that food.")
            return
        print()
        pet.eat(chosen_food)
        if pet.hunger <= 0:
            print(f"{pet.pet_name} takes a massive DUMP.")
            self.poop_on_floor = True
            pet.hunger = 100

    def play_with_pet(self, pet):
        toy_str = input("What do you want to fetch with? ")
        print()
        pet.play_with(toy_str)

    def put_pet_to_bed(self, pet):
        print(f"{pet.pet_name} goes back to bed. :D")
        del self.pets[pet.pet_name]
        if len(self.pets) == 0:
            self.game_over = True

    def clean_up_poop(self, pet):
        if self.poop_on_floor:
            print("You clean up the poop")
            print()
            self.poop_on_floor = False
            return
        print("There's nothing to clean.")

    def cheat(game_state, pet):
        print(
                f"Dagger's da dude! How could {pet.pet_name} not love "
                "'im?")
        pet.happiness = 100

    def take_turn(self):
        print("Your pets are:")
        for pet_name in self.pets:
            print(pet_name)
        print()
        chosen_pet_name = input("Take care of which pet? ")
        try:
            chosen_pet = self.pets[chosen_pet_name]
        except KeyError:
            print("You don't have a pet by that name.")
            print()
            return
        player_command = self.prompt_for_activity()
        print()
        self.run_command_with_pet(player_command, chosen_pet)
        for pet in self.pets.values():
            if pet.hunger > 70:
                print(pet.pet_name + " seems kind of hungry...")
                pet.happiness -= 10

            if self.poop_on_floor:
                pet.happiness -= 10

            if pet.happiness <= 0:
                print(
                    f"{pet.pet_name} bites you! And then poops on the "
                    "dang carpet!")
                print("You faint from embarrassment...")
                self.game_over = True
        print()


game_state = GameState()

game_state.pets["dixxucker"] = OurPet("dixxucker", 100, 100)
game_state.pets["Zanzhu"] = OurPet("Zanzhu", 40, 40)
game_state.pets["KD_Alpha"] = OurPet("KD_Alpha", 50, 100)
game_state.pets["tf_dagger"] = OurPet("tf_dagger", 50, 30)
game_state.pets["Vencabot"] = OurPet("Vencabot", 60, 100)

game_state.foods["banana"] = PetFood("banana", 70, 20)
game_state.foods["pie"] = PetFood("pie", 100, 40)
game_state.foods["mushroom"] = PetFood("mushroom", 10, 10)
game_state.foods["cheeseburger"] = PetFood("cheeseburger", 80, 30)
game_state.foods["dick"] = PetFood("dick", 100, 100)

while not game_state.game_over:
    game_state.take_turn()
print("Game Over")
