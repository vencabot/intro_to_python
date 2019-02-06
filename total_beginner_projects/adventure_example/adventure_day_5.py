class GameArea:
    description = "You are in an area."
    is_lit = True

    def get_description(self, game_state):
        if self.is_lit or game_state["torch"] in game_state["player"].inventory:
            print(self.description)
            for inv_item in self.inventory:
                print("There is a(n) " + inv_item.description + " here.")
        else:
            print("It's too dark to see.")


class TreasureChest:
    inventory = []
    is_open = False
    description = "treasure chest"

    def open_lid(self, game_state):
        # BUG: 'game_state' is included for compatibility.
        # Remove this unused argument.
        if self not in game_state["player"].position.inventory:
            print("You don't see a chest.")
            return
        if not self.is_open:
            print("You open the chest.")
            self.is_open = True
        else:
            print("It's already open.")
        for an_item in self.inventory:
            print("There is a(n) " + an_item.description + " inside.")

    def take_item(self, item_str, player):
        if self not in game_state["player"].position.inventory:
            print("You don't see a chest.")
            return
        if item_str in self.inventory:
            print("You took a(n) " + item_str + " from the chest.")
            self.inventory.remove(item_str)
            player.inventory.append(item_str)


class Door:
    is_locked = False
    is_open = False
    location_a = GameArea()
    location_b = GameArea()
    description = "door"

    def unlock(self, game_state):
        if self not in game_state["player"].position.inventory:
            print("You don't see a door here.")
            return
        if self.is_locked:
            if game_state["key"] in game_state["player"].inventory:
                print("You used the key to unlock the door.")
                self.is_locked = False
            else:
                print("You don't have a key.")
        else:
            print("The door isn't locked!")

    def open_up(self, game_state):
        if self not in game_state["player"].position.inventory:
            print("You don't see a door here.")
            return
        if not self.is_open:
            if self.is_locked:
                print("You can't open the door. It's locked.")
            else:
                print("You open the door.")
                self.is_open = True
        else:
            print("It's already open.")

    def enter(self, game_state):
        if self not in game_state["player"].position.inventory:
            print("You don't see a door here.")
            return
        if self.is_open:
            print("You walk through the door.")
            if game_state["player"].position == self.location_a:
                game_state["player"].position = self.location_b
            else:
                game_state["player"].position = self.location_a
        else:
            print("You can't enter the door. It's closed.")


class Stairs:
    location_a = GameArea()
    location_b = GameArea()
    description = "staircase"

    def enter(self, game_state):
        if self not in game_state["player"].position.inventory:
            print("You don't see stairs here.")
            return
        if game_state["player"].position == self.location_a:
            if not game_state["torch"] in game_state["player"].inventory:
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

    def do_a_dance(self, game_state):
        print("You perform a break-dance. What style!")

    def look_around(self, game_state):
        self.position.get_description(game_state)


class GameItem:
    description = "item"


def get_the_key(game_state):
    if game_state["chest"] not in game_state["player"].position.inventory:
        print("You don't see a chest here.")
        return
    if game_state["chest"].is_open:
        if game_state["key"] in game_state["chest"].inventory:
            print("You picked up the key!")
            game_state["player"].inventory.append(game_state["key"])
            game_state["chest"].inventory.remove(game_state["key"])
    elif "key" in game_state["player"].inventory:
        print("You already got the key!")
    else:
        print("You don't see a key.")


def leave_the_cave(game_state):
    # You can now leave the cave from anywhere.
    if game_state["key"] in game_state["player"].inventory:
        print("You walked out of the cave.")
        game_state["adventure_is_ongoing"] = False
    else:
        print("Aren't you forgetting something?")


def get_the_torch(game_state):
    if game_state["torch"] in game_state["player"].position.inventory:
        print("You picked up a torch.")
        game_state["player"].inventory.append(game_state["torch"])
        game_state["player"].position.inventory.remove(game_state["torch"])
    else:
        print("You don't see a torch.")


def get_the_record(game_state):
    if game_state["record"] in game_state["player"].position.inventory:
        print("You picked up the vinyl record.")
        game_state["player"].inventory.append(game_state["record"])
        game_state["player"].position.inventory.remove(game_state["record"])
    else:
        print("You don't see a record.")


def listen_to_the_record(game_state):
    if game_state["record_player"] in game_state["player"].position.inventory:
        if game_state["record"] in game_state["player"].inventory:
            print("Mellow music fills the room.")
        else:
            print("You don't have a record to play.")
    else:
        print("You need a record-player for that.")


key = GameItem()
key.description = "key"

torch = GameItem()
torch.description = "torch"

record = GameItem()
record.description = "vinyl record"

calzone = GameItem()
calzone.description = "delicious calzone"

screwdriver = GameItem()
screwdriver.description = "screwdriver"

record_player = GameItem()
record_player.description = "old record-player"

chest = TreasureChest()
chest.inventory.append(key)
chest.inventory.append(calzone)
chest.inventory.append(screwdriver)

door = Door()
door.is_locked = True

stairs = Stairs()

cave_entrance = GameArea()
cave_entrance.description = "You are in a dank cave."
cave_entrance.inventory = []
cave_entrance.inventory.append(torch)
cave_entrance.inventory.append(door)
cave_entrance.inventory.append(chest)

dark_room = GameArea()
dark_room.description = "Surprisingly, you find yourself in a cozy room."
dark_room.inventory = []
dark_room.inventory.append(door)
dark_room.inventory.append(stairs)
dark_room.inventory.append(record_player)
dark_room.is_lit = False

basement = GameArea()
basement.description = "You are in a slimy basement."
basement.inventory = []
basement.inventory.append(stairs)
basement.inventory.append(record)

door.location_a = cave_entrance
door.location_b = dark_room

stairs.location_a = dark_room
stairs.location_b = basement

player = Player()
player.position = cave_entrance

game_state = {
        "chest": chest, "door": door, "player": player, "key": key,
        "torch": torch, "record": record, "record_player": record_player,
        "adventure_is_ongoing": True}

command_map = {
        "look around": player.look_around,
        "do a dance": player.do_a_dance,
        "open the chest": chest.open_lid, "get the key": get_the_key,
        "leave the cave": leave_the_cave, "get the torch": get_the_torch,
        "open the door": door.open_up, "unlock the door": door.unlock,
        "enter the door": door.enter,
        "descend the staircase": stairs.enter,
        "ascend the staircase": stairs.enter,
        "get the record": get_the_record,
        "listen to the record": listen_to_the_record}

print("You are in a cave.")

while game_state["adventure_is_ongoing"]:
    player_command = input("Whachu wanna do? ")

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
