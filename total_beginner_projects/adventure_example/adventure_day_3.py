def look_around(game_state):
    if game_state["player_position"] == "cave entrance":
        print("The cave is dank and there's a treasure chest.")
        print("There's also a door.")
        if not "torch" in game_state["player_inventory"]:
            print("There's also a torch.")
        else:
            print("There's an empty spot where the torch was.")
    elif game_state["player_position"] == "dark room":
        if not "torch" in game_state["player_inventory"]:
            print("It's too dark to see.")
        else:
            print("Strangely, you find that you're in a comfortable living room.")
            print("You see an old record-player in the corner.")
            print("You see a staircase to the basement.")
    elif game_state["player_position"] == "basement":
        print("The basement is moldy and smells ancient.")
        if not "record" in game_state["player_inventory"]:
            print("You see a shelf with a vinyl record on it.")
        else:
            print("You see an empty shelf.")


def do_a_dance(game_state):
    print("You perform a break-dance. What style!")


def open_the_chest(game_state):
    if not game_state["chest_is_open"]:
        print("You open the chest. There's a key inside.")
        game_state["chest_is_open"] = True
    elif not "key" in game_state["player_inventory"]:
        print("The chest is already open. There's a key inside.")
    else:
        print("The chest is already open. It's empty.")


def get_the_key(game_state):
    if game_state["chest_is_open"] and "key" not in game_state["player_inventory"]:
        print("You picked up the key!")
        game_state["player_inventory"].append("key")
    elif game_state["chest_is_open"] and "key" in game_state["player_inventory"]:
        print("You already got the key!")
    else:
        print("You don't see a key.")


def leave_the_cave(game_state):
    if "key" in game_state["player_inventory"]:
        print("You walked out of the cave.")
        game_state["adventure_is_ongoing"] = False
    else:
        print("Aren't you forgetting something?")


def get_the_torch(game_state):
    if "torch" not in game_state["player_inventory"]:
        print("You picked up the torch.")
        game_state["player_inventory"].append("torch")
    else:
        print("You already have the torch, dumb-dumb.")


def open_the_door(game_state):
    if not game_state["door_is_unlocked"]:
        print("The door's locked, dang it!")
    elif not game_state["door_is_open"]:
        print("You open the door.")
        game_state["door_is_open"] = True
    else:
        print("It's already open.")


def unlock_the_door(game_state):
    if game_state["door_is_unlocked"]:
        print("The door's already unlocked.")
    elif "key" not in game_state["player_inventory"]:
        print("You don't have a key.")
    else:
        print("You use the key to unlock the door.")
        game_state["door_is_unlocked"] = True


def enter_the_door(game_state):
    if game_state["door_is_open"]:
        print("You walk through the door.")
        if game_state["player_position"] == "cave entrance":
            game_state["player_position"] = "dark room"
        else:
            game_state["player_position"] = "cave entrance"
    else:
        print("You can't enter the door. It's closed.")


def descend_the_staircase(game_state):
    if "torch" in game_state["player_inventory"]:
        print("You descend the staircase.")
        game_state["player_position"] = "basement"
    else:
        print("You walk over to one side of the dark room.")
        print("You find a staircase and tumble to your demise.")
        print("You Died.")
        game_state["adventure_is_ongoing"] = False


def get_the_record(game_state):
    if "record" in game_state["player_inventory"]:
        print("You've already picked up the record.")
    else:
        print("You pick up the vinyl record.")
        game_state["player_inventory"].append("record")


def ascend_the_staircase(game_state):
    print("You ascend the staircase.")
    game_state["player_position"] = "dark room"


def listen_to_the_record(game_state):
    if "record" in game_state["player_inventory"]:
        print("Mellow music fills the room.")
    else:
        print("You don't have a record to play.")


game_state = {
        "chest_is_open": False, "door_is_unlocked": False,
        "door_is_open": False, "player_inventory": [],
        "adventure_is_ongoing": True, "player_position": "cave entrance"}

cave_entrance_command_map = {
        "look around": look_around, "do a dance": do_a_dance,
        "open the chest": open_the_chest, "get the key": get_the_key,
        "leave the cave": leave_the_cave, "get the torch": get_the_torch,
        "open the door": open_the_door,
        "unlock the door": unlock_the_door,
        "enter the door": enter_the_door}

dark_room_command_map = {
        "look around": look_around, "do a dance": do_a_dance,
        "enter the door": enter_the_door,
        "descend the staircase": descend_the_staircase,
        "listen to the record": listen_to_the_record}

basement_command_map = {
        "look around": look_around, "get the record": get_the_record,
        "ascend the staircase": ascend_the_staircase}

position_map = {
        "cave entrance": cave_entrance_command_map,
        "dark room": dark_room_command_map,
        "basement": basement_command_map}

print("You are in a cave.")

while game_state["adventure_is_ongoing"]:
    player_command = input("Whachu wanna do? ")

    current_position = game_state["player_position"]
    command_map = position_map[current_position]

    if player_command == "help":
        print("You have these commands available to you:")
        for command_str in command_map.keys():
            print("    " + command_str)
    else:
        try:
            command_function = command_map[player_command]
            command_function(game_state)
        except KeyError:
            print("You can't do that.")
    print()

print("Game over.")
