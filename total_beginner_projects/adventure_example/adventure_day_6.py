class GameArea:
    is_lit = True

    def __init__(self, description):
        self.description = description
        self.inventory = []

    def get_description(self, player):
        player_has_torch = False
        for game_item in player.inventory:
            if game_item.description == "torch":
                player_has_torch = True
                break
        if self.is_lit or player_has_torch:
            print(self.description)
            for inv_item in self.inventory:
                print("There is a(n) " + inv_item.description + " here.")
        else:
            print("It's too dark to see.")


class TreasureChest:
    inventory = []
    is_open = False
    description = "treasure chest"

    def __init__(self, description):
        self.description = description
        self.command_map = {"open": self.open_lid}

    def open_lid(self, player):
        if self not in player.position.inventory:
            print("You don't see a chest.")
            return
        if not self.is_open:
            print("You open the chest.")
            self.is_open = True
        else:
            print("It's already open.")
        for an_item in self.inventory:
            print("There is a(n) " + an_item.description + " inside.")

class Door:
    is_locked = False
    is_open = False

    def __init__(self, description, location_a, location_b):
        self.description = description
        self.location_a = location_a
        self.location_b = location_b
        self.command_map = {
                "open": self.open_up, "unlock": self.unlock,
                "enter": self.enter}

    def unlock(self, player):
        if self not in player.position.inventory:
            print("You don't see a door here.")
            return
        if self.is_locked:
            player_has_key = False
            for game_item in player.inventory:
                if game_item.description == "key":
                    player_has_key = True
                    break
            if player_has_key:
                print("You used the key to unlock the door.")
                self.is_locked = False
            else:
                print("You don't have a key.")
        else:
            print("The door isn't locked!")

    def open_up(self, player):
        if self not in player.position.inventory:
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

    def enter(self, player):
        if self not in player.position.inventory:
            print("You don't see a door here.")
            return
        if self.is_open:
            print("You walk through the door.")
            if player.position == self.location_a:
                player.position = self.location_b
            else:
                player.position = self.location_a
            player.position.get_description(player)
        else:
            print("You can't enter the door. It's closed.")


class Stairs:
    def __init__(self, description, location_a, location_b):
        self.description = description
        self.location_a = location_a
        self.location_b = location_b
        self.command_map = {"ascend": self.enter, "descend": self.enter}

    def enter(self, player):
        if self not in player.position.inventory:
            print("You don't see stairs here.")
            return
        if player.position == self.location_a:
            player_has_torch = False
            for game_item in player.inventory:
                if game_item.description == "torch":
                    player_has_torch = True
                    break
            if not player_has_torch:
                print("You tripped over some stairs in the dark and died.")
                player.is_adventuring = False
                return
            else:
                print("You descend the stairs.")
                player.position = self.location_b
        else:
            print("You ascend the stairs.")
            player.position = self.location_a
        player.position.get_description(player)


class Player:
    def __init__(self, position):
        self.position = position
        self.inventory = []
        self.is_adventuring = True


class GameItem:
    def __init__(self, description):
        self.description = description
        self.command_map = {"get": self.get_item}

    def get_item(self, player):
        for room_item in player.position.inventory:
            if (
                    isinstance(room_item, TreasureChest)
                    and room_item.is_open
                    and self in room_item.inventory):
                print(
                        "You got a(n) " + self.description
                        + " from a(n) " + room_item.description + ".")
                room_item.inventory.remove(self)
                player.inventory.append(self)
                return
        if self in player.position.inventory:
            print("You got a(n) " + self.description + ".")
            player.position.inventory.remove(self)
            player.inventory.append(self)
        elif self in player.inventory:
            print("You already have a(n) " + self.description + ".")
        else:
            print("You don't see that here.")


def leave_the_cave(game_state):
    if game_state["key"] in game_state["player"].inventory:
        print("You walked out of the cave.")
        game_state["adventure_is_ongoing"] = False
    else:
        print("Aren't you forgetting something?")


def listen_to_the_record(game_state):
    if game_state["record_player"] in game_state["player"].position.inventory:
        if game_state["record"] in game_state["player"].inventory:
            print("Mellow music fills the room.")
        else:
            print("You don't have a record to play.")
    else:
        print("You need a record-player for that.")

cave_entrance = GameArea("You are in a dank cave.")
dark_room = GameArea("Surprisingly, you find yourself in a cozy room.")
basement = GameArea("You are in a slimy basement.")

player = Player(cave_entrance)

door = Door("door", cave_entrance, dark_room)
stairs = Stairs("stairs", dark_room, basement)

key = GameItem("key")
torch = GameItem("torch")
record = GameItem("vinyl record")
calzone = GameItem("delicious calzone")
screwdriver = GameItem("screwdriver")
record_player = GameItem("record-player")
mini_fridge = GameItem("mini-fridge")
chest = TreasureChest("treasure chest")

cave_entrance.inventory.append(torch)
cave_entrance.inventory.append(door)
cave_entrance.inventory.append(chest)

dark_room.inventory.append(door)
dark_room.inventory.append(stairs)
dark_room.inventory.append(record_player)
dark_room.inventory.append(mini_fridge)
dark_room.is_lit = False

basement.inventory.append(stairs)
basement.inventory.append(record)

chest.inventory.append(key)
chest.inventory.append(calzone)
chest.inventory.append(screwdriver)

door.is_locked = True

world_list = [
        door, stairs, key, torch, record, calzone, screwdriver,
        record_player, mini_fridge, chest]

print("You are in a cave.")

while player.is_adventuring:
    player_command = input("Whachu wanna do? ")
    command_split = player_command.split()
    if len(command_split) < 2:
        print("Please use [VERB] [ITEM] command.")
        print()
        continue
    command_verb = command_split[0]
    command_noun = " ".join(command_split[1:])

    target_item = None
    for world_item in world_list:
        if world_item.description == command_noun:
            target_item = world_item
            break

    if not target_item:
        print("You don't see that here.")
    else:
        try:
            command_function = target_item.command_map[command_verb]
        except KeyError:
            print("You can't do that.")
        else:
            command_function(player)
    print()

print("Game over.")
