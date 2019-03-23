def feed_pet(game_state):
    pets_food = input(
            "What do you want to feed " + game_state["pets_name"] + "? ")
    print()

    if pets_food in game_state["pets_favorite_foods"]:
        game_state["pets_happiness"] += 20
    elif pets_food in game_state["pets_hated_foods"]:
        game_state["pets_happiness"] -= 40
    elif pets_food == "rocks":
        print("Don't do that, you meanie!")
        print()
        return
    elif pets_food == "pear":
        print("shout out to all the pear")
        game_state["pets_happiness"] += 10
    else:
        game_state["pets_happiness"] -= 10

    print(game_state["pets_name"] + " eats the " + pets_food + ".")

    if game_state["pets_happiness"] >= 80:
        print(game_state["pets_name"] + " seems ecstatic!!")
    elif game_state["pets_happiness"] >= 50:
        print(game_state["pets_name"] + " seems in high spirits.")
    elif game_state["pets_happiness"] >= 25:
        print(game_state["pets_name"] + " seems kind of down.")
    else:
        print(game_state["pets_name"] + " seems mad depressed.")
    print()

    game_state["pets_hunger"] -= 20

    if game_state["pets_hunger"] <= 0:
            print(game_state["pets_name"] + " takes a massive DUMP.")
            print()
            game_state["poop_on_floor"] = True
            game_state["pets_hunger"] = 100


def play_with_pet(game_state):
    if game_state["pets_happiness"] < 50:
        print(game_state["pets_name"] + " isn't in the mood to play...")
        print()
        return

    if game_state["pets_hunger"] > 60:
        print(game_state["pets_name"] + " is too hungry to play!")
        game_state["pets_happiness"] -= 20
        return

    thrown_object = input("What do you want to fetch with? ")
    print()
    print("You throw the " + thrown_object + ".")
    print()

    if game_state["pets_happiness"] >= 80:
        print(
                game_state["pets_name"] + " retrieves the "
                + thrown_object + " with lightning speed!")
    elif game_state["pets_happiness"] >= 70:
        print(
                game_state["pets_name"] + " takes their time retrieving "
                + "the " + thrown_object + " while wagging their "
                + "tail(?).")
    else:
        print(
                game_state["pets_name"] + " watches the "
                + thrown_object + " fall and looks at you dumbly.")

    print()
    game_state["pets_hunger"] += 20


def put_pet_to_bed(game_state):
    print(game_state["pets_name"] + " goes back to bed. :D")
    game_state["taking_care_of_pet"] = False


def clean_up_poop(game_state):
    if game_state["poop_on_floor"]:
        print("You clean up " + game_state["pets_name"] + "'s poop.")
        print()
        game_state["poop_on_floor"] = False
    else:
        print("There's nothing to clean.")


def cheat(game_state):
    print(
            "Dagger's dat dude! How could " + game_state["pets_name"]
            + " not love 'im?!")
    game_state["pets_happiness"] = 100


game_state = {}
game_state["pets_favorite_foods"] = ["lasagna", "pie"]
game_state["pets_hated_foods"] = [
        "tofu", "brussel sprouts", "black-eyed peas", "okra"]
game_state["pets_happiness"] = 50
game_state["pets_hunger"] = 100
game_state["poop_on_floor"] = False
game_state["pets_name"] = input("What is your pet's name? ")
game_state["taking_care_of_pet"] = True

commands = {
        "feed": feed_pet, "play": play_with_pet, "quit": put_pet_to_bed,
        "clean": clean_up_poop, "dagger": cheat}
print()

while game_state["taking_care_of_pet"]:
    if not game_state["poop_on_floor"]:
        pet_activity = input(
                "Do you want to 'feed' or 'play' with "
                + game_state["pets_name"] + "? ")
    else:
        pet_activity = input(
                "Do you want to 'feed' or 'play' with "
                + game_state["pets_name"] + ", or do you want to "
                + "'clean' the room? ")
    print()

    try:
        command_callable = commands[pet_activity]
    except KeyError:
        print("Please type either 'feed', 'play', 'quit', or 'clean'.")
    command_callable(game_state)

    if game_state["pets_hunger"] > 70:
        print(game_state["pets_name"] + " seems kind of hungry...")
        print()
        game_state["pets_happiness"] -= 10

    if game_state["poop_on_floor"]:
        game_state["pets_happiness"] -= 10

    if game_state["pets_happiness"] <= 0:
        print(
                game_state["pets_name"] + " bites you! And then poops "
                + "on the dang carpet!")
        print("You faint from embarrassment...")
        game_state["taking_care_of_pet"] = False

print("Game Over")
