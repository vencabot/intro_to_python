def look_around(player_inventory):
    print("The cave is dank and there's a treasure chest.")
    print("There's also a door.")
    if not "torch" in player_inventory:
        print("There's also a torch.")
    else:
        print("There's an empty spot where the torch was.")

def do_a_dance():
    print("You perform a break-dance. What style!")

def open_the_chest(chest_is_open, player_inventory):
    if not chest_is_open:
        print("You open the chest. There's a key inside.")
        chest_is_open = True
    elif not "key" in player_inventory:
        print("The chest is already open. There's a key inside.")
    else:
        print("The chest is already open. It's empty.")
    return chest_is_open

def get_the_key(chest_is_open, player_inventory):
    if chest_is_open and "key" not in player_inventory:
        print("You picked up the key!")
        player_inventory.append("key")
    elif chest_is_open and "key" in player_inventory:
        print("You already got the key!")
    else:
        print("You don't see a key.")

def leave_the_cave(player_inventory):
    if "key" in player_inventory:
        print("You walked out of the cave.")
        adventure_is_ongoing = False
    else:
        print("Aren't you forgetting something?")
        adventure_is_ongoing = True
    return adventure_is_ongoing

def get_the_torch(player_inventory):
    if "torch" not in player_inventory:
        print("You picked up the torch.")
        player_inventory.append("torch")
    else:
        print("You already have the torch, dumb-dumb.")

def open_the_door(door_is_unlocked, door_is_open):
    if not door_is_unlocked:
        print("The door's locked, dang it!")
    elif not door_is_open:
        print("You open the door.")
        door_is_open = True
    else:
        print("It's already open.")
    return door_is_open

def unlock_the_door(door_is_unlocked, player_inventory):
    if door_is_unlocked:
        print("The door's already unlocked.")
    elif "key" not in player_inventory:
        print("You don't have a key.")
    else:
        print("You use the key to unlock the door.")
        door_is_unlocked = True
    return door_is_unlocked

chest_is_open = False
door_is_unlocked = False
door_is_open = False
player_inventory = []
adventure_is_ongoing = True

print("You are in a cave.")

while adventure_is_ongoing:
    player_command = input("Whachu wanna do? ")

    if player_command == "look around":
        look_around(player_inventory)
    elif player_command == "do a dance":
        do_a_dance()
    elif player_command == "open the chest":
        chest_is_open = open_the_chest(chest_is_open, player_inventory)
    elif player_command == "get the key":
        get_the_key(chest_is_open, player_inventory)
    elif player_command == "leave the cave":
        adventure_is_ongoing = leave_the_cave(player_inventory)
    elif player_command == "get the torch":
        get_the_torch(player_inventory)
    elif player_command == "open the door":
        door_is_open = open_the_door(door_is_unlocked, door_is_open)
    elif player_command == "unlock the door":
        door_is_unlocked = unlock_the_door(door_is_unlocked, player_inventory)
    else:
        print("You can't do that.")
    print()

print("Game over.")
