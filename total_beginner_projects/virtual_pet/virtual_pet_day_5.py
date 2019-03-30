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
        print(self.pet_name + " eats the " + pet_food.food_name + ".")
        if self.happiness >= 80:
            print(self.pet_name + " seems ecstatic!!")
        elif self.happiness >= 50:
            print(self.pet_name + " seems in high spirits.")
        elif self.happiness >= 25:
            print(self.pet_name + " seems kind of down.")
        else:
            print(self.pet_name + " seems mad depressed.")
        print()
        self.hunger -= pet_food.fillingness

    def play_with(self, toy):
        if self.happiness < 50:
            print(self.pet_name + " isn't in the mood to play...")
            print()
            return
        if self.hunger > 60:
            print(self.pet_name + " is too hungry to play!")
            self.happiness -= 20
            return
        print(f"You throw the {toy}.")
        print()
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
        print()
        self.hunger += 20

    def dance(self):
        print(self.pet_name + " does a dance.")


def input_pet_activity(game_state):
    if not game_state["poop_on_floor"]:
        pet_activity = input("Do you want to 'feed' or 'play'?")
    else:
        pet_activity = input(
                "Do you want to 'feed', 'play', or 'clean'? ")
    return pet_activity


def run_player_command(game_state, command_map, pet, player_command):
    try:
        command_callable = command_map[player_command]
    except KeyError:
        print("Please type either 'feed', 'play', 'quit', or 'clean'.")
    command_callable(game_state, pet)


def feed_pet(game_state, pet):
    food_dict = {}
    for pet_food in game_state["food_inventory"]:
        food_dict[pet_food.food_name] = pet_food
    print("You can feed the pet:")
    for pet_food in game_state["food_inventory"]:
        print(pet_food.food_name)
    print()
    chosen_food_name = input(
            f"What do you want to feed {pet.pet_name}? ")
    try:
        chosen_food = food_dict[chosen_food_name]
    except KeyError:
        print("You don't have that.")
        return
    print()
    pet.eat(chosen_food)
    if pet.hunger <= 0:
            print(pet.pet_name + " takes a massive DUMP.")
            print()
            game_state["poop_on_floor"] = True
            pet.hunger = 100


def play_with_pet(game_state, pet):
    thrown_object = input("What do you want to fetch with? ")
    pet.play_with(thrown_object)


def put_pet_to_bed(game_state, pet):
    print(pet.pet_name + " goes back to bed. :D")
    game_state["pets"].remove(pet)
    if len(game_state["pets"]) == 0:
        game_state["taking_care_of_pet"] = False


def clean_up_poop(game_state, pet):
    if game_state["poop_on_floor"]:
        print("You clean up the poop.")
        print()
        game_state["poop_on_floor"] = False
    else:
        print("There's nothing to clean.")


def cheat(game_state, pet):
    print(
            f"Dagger's da dude! How could {pet.pet_namea} not love 'im?")
    game_state["pet"].happiness = 100


def end_turn(game_state):
    for pet in game_state["pets"]:
        if pet.hunger > 70:
            print(pet.pet_name + " seems kind of hungry...")
            pet.happiness -= 10

        if game_state["poop_on_floor"]:
            pet.happiness -= 10

        if pet.happiness <= 0:
            print(
                f"{pet.pet_name} bites you! And then poops on the dang "
                "carpet!")
            print("You faint from embarrassment...")
            game_state["taking_care_of_pet"] = False
    print()


dixxucker = OurPet("dixxucker", 100, 100)
zanzhu = OurPet("Zanzhu", 40, 40)
kd_alpha = OurPet("KD_Alpha", 50, 100)
tf_dagger = OurPet("tf_dagger", 50, 30)
vencabot = OurPet("Vencabot", 60, 100)
game_state = {}
game_state["pets"] = [dixxucker, zanzhu, kd_alpha]
game_state["poop_on_floor"] = False
game_state["taking_care_of_pet"] = True

banana = PetFood("banana", 70, 20)
pie = PetFood("pie", 100, 40)
mushroom = PetFood("mushroom", 10, 10)
cheeseburger = PetFood("cheeseburger", 80, 30)
dick = PetFood("dick", 100, 100)

game_state["food_inventory"] = [
        banana, pie, mushroom, cheeseburger, dick]

commands = {
        "feed": feed_pet, "play": play_with_pet, "quit": put_pet_to_bed,
        "clean": clean_up_poop, "dagger": cheat}
print()

pet_map = {}
for pet in game_state["pets"]:
    pet_map[pet.pet_name] = pet

while game_state["taking_care_of_pet"]:
    print("Your pets are:")
    for pet in game_state["pets"]:
        print(pet.pet_name)
    print()
    chosen_pet_name = input("Which pet do you want to take care of? ")
    try:
        chosen_pet = pet_map[chosen_pet_name]
    except KeyError:
        print("You don't have a pet by that name.")
        print()
        continue
    pet_activity = input_pet_activity(game_state)
    print()
    run_player_command(game_state, commands, chosen_pet, pet_activity)
    end_turn(game_state)

print("Game Over")
