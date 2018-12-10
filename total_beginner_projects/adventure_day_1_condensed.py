def look_around():
    print("The cave is dank and there's a treasure chest.")

def do_a_dance():
    print("You perform a break-dance. What style!")

def open_the_chest(chest_is_open, player_has_key):
    if not chest_is_open:
        print("You open the chest. There's a key inside.")
        chest_is_open = True
    elif not player_has_key:
        print("The chest is already open. There's a key inside.")
    else:
        print("The chest is already open. It's empty.")
    return chest_is_open

def get_the_key(chest_is_open, player_has_key):
    if chest_is_open and not player_has_key:
        print("You picked up the key!")
        player_has_key = True
    elif chest_is_open and player_has_key:
        print("You already got the key!")
    else:
        print("You don't see a key.")
    return player_has_key

def leave_the_cave(player_has_key):
    if player_has_key:
        print("You walked out of the cave.")
        adventure_is_ongoing = False
    else:
        print("Aren't you forgetting something?")
        adventure_is_ongoing = True
    return adventure_is_ongoing

chest_is_open = False
player_has_key = False
adventure_is_ongoing = True

print("You are in a cave.")

while adventure_is_ongoing:
    player_command = input("Whachu wanna do? ")

    if player_command == "look around":
        look_around()
    elif player_command == "do a dance":
        do_a_dance()
    elif player_command == "open the chest":
        chest_is_open = open_the_chest(chest_is_open, player_has_key)
    elif player_command == "get the key":
        player_has_key = get_the_key(chest_is_open, player_has_key)
    elif player_command == "leave the cave":
        adventure_is_ongoing = leave_the_cave(player_has_key)
    else:
        print("You can't do that.")
    print()

print("Game over.")
