class TreasureChest:
    inventory = []
    is_open = False

    def open_lid(self, game_state):
        # BUG: 'game_state' is included for compatibility.
        # Remove this unused argument.
        if not self.is_open:
            print("You open the chest.")
            self.is_open = True
        else:
            print("It's already open.")
        for an_item in self.inventory:
            print("There is a(n) " + an_item + " inside.")

    def take_item(self, item_str, player):
        if item_str in self.inventory:
            print("You took a(n) " + item_str + " from the chest.")
            self.inventory.remove(item_str)
            player.inventory.append(item_str)


class Door:
    is_locked = False
    is_open = False
    location_a = "place_a"
    location_b = "place_b"

    def unlock(self, game_state):
        if self.is_locked:
            if "key" in game_state["player"].inventory:
                print("You used the key to unlock the door.")
                self.is_locked = False
            else:
                print("You don't have a key.")
        else:
            print("The door isn't locked!")

    def open_up(self, game_state):
        if not self.is_open:
            if self.is_locked:
                print("You can't open the door. It's locked.")
            else:
                print("You open the door.")
                self.is_open = True
        else:
            print("It's already open.")

    def enter(self, game_state):
        if self.is_open:
            print("You walk through the door.")
            if game_state["player"].position == self.location_a:
                game_state["player"].position = self.location_b
            else:
                game_state["player"].position = self.location_a
        else:
            print("You can't enter the door. It's closed.")


class Stairs:
    location_a = "place_a"
    location_b = "place_b"

    def enter(self, game_state):
        if game_state["player"].position == self.location_a:
            if not "torch" in game_state["player"].inventory:
                print("You tripped over some stairs in the dark and died.")
                game_state["adventure_is_ongoing"] = False
            else:
                print("You descend the stairs.")
                game_state["player"].position = self.location_b
        else:
            print("You ascend the stairs.")
            game_state["player"].position = self.location_a


class Player:
    inventory = []
    position = "nowhere"


def look_around(game_state):
    if game_state["player"].position == "cave entrance":
        print("The cave is dank and there's a treasure chest.")
        print("There's also a door.")
        if not "torch" in game_state["player"].inventory:
            print("There's also a torch.")
        else:
            print("There's an empty spot where the torch was.")
    elif game_state["player"].position == "dark room":
        if not "torch" in game_state["player"].inventory:
            print("It's too dark to see.")
        else:
            print("Strangely, you find that you're in a comfortable living room.")
            print("You see an old record-player in the corner.")
            print("You see a staircase to the basement.")
    elif game_state["player"].position == "basement":
        print("The basement is moldy and smells ancient.")
        if not "record" in game_state["player"].inventory:
            print("You see a shelf with a vinyl record on it.")
        else:
            print("You see an empty shelf.")


def do_a_dance(game_state):
    print("You perform a break-dance. What style!")


def get_the_key(game_state):
    if game_state["chest"].is_open and "key" in game_state["chest"].inventory:
        print("You picked up the key!")
        game_state["player"].inventory.append("key")
        game_state["chest"].inventory.remove("key")
    elif "key" in game_state["player"].inventory:
        print("You already got the key!")
    else:
        print("You don't see a key.")


def leave_the_cave(game_state):
    if "key" in game_state["player"].inventory:
        print("You walked out of the cave.")
        game_state["adventure_is_ongoing"] = False
    else:
        print("Aren't you forgetting something?")


def get_the_torch(game_state):
    if "torch" not in game_state["player"].inventory:
        print("You picked up the torch.")
        game_state["player"].inventory.append("torch")
    else:
        print("You already have the torch, dumb-dumb.")


def get_the_record(game_state):
    if "record" in game_state["player"].inventory:
        print("You've already picked up the record.")
    else:
        print("You pick up the vinyl record.")
        game_state["player"].inventory.append("record")


def listen_to_the_record(game_state):
    if "record" in game_state["player"].inventory:
        print("Mellow music fills the room.")
    else:
        print("You don't have a record to play.")


player = Player()
player.position = "cave entrance"

chest = TreasureChest()
chest.inventory.append("key")
chest.inventory.append("calzone")
chest.inventory.append("screwdriver")

door = Door()
door.is_locked = True
door.location_a = "cave entrance"
door.location_b = "dark room"

stairs = Stairs()
stairs.location_a = "dark room"
stairs.location_b = "basement"

game_state = {
        "chest": chest, "door": door, "player": player,
        "adventure_is_ongoing": True}

cave_entrance_command_map = {
        "look around": look_around, "do a dance": do_a_dance,
        "open the chest": chest.open_lid, "get the key": get_the_key,
        "leave the cave": leave_the_cave, "get the torch": get_the_torch,
        "open the door": door.open_up, "unlock the door": door.unlock,
        "enter the door": door.enter}

dark_room_command_map = {
        "look around": look_around, "do a dance": do_a_dance,
        "enter the door": door.enter,
        "descend the staircase": stairs.enter,
        "listen to the record": listen_to_the_record}

basement_command_map = {
        "look around": look_around, "get the record": get_the_record,
        "ascend the staircase": stairs.enter}

position_map = {
        "cave entrance": cave_entrance_command_map,
        "dark room": dark_room_command_map,
        "basement": basement_command_map}

print("You are in a cave.")

while game_state["adventure_is_ongoing"]:
    player_command = input("Whachu wanna do? ")

    command_map = position_map[player.position]

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
