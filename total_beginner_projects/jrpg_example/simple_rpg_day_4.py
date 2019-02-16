import random

class Protagonist:
    def __init__(self, protagonist_name):
        self.moniker = protagonist_name
        if self.moniker == "Chun Li":
            print("You're the strongest woman in the world!")
            self.atk = 10
        else:
            self.atk = 6
        self.hp = 25
        self.is_defending = False
        self.inventory = [SpearItem(), PotionItem()]
        self.purse = 0


class SpearItem:
    def __init__(self):
        self.item_name = "spear"
        self.gold_value = 15

    def use_item(self, game_state):
        inventory_dict = {}
        for inventory_item in game_state["protagonist"].inventory:
            inventory_dict[inventory_item.item_name] = inventory_item
        if "spear" in inventory_dict:
            game_state["monster_hp"] = (
                    game_state["monster_hp"]
                    - (game_state["protagonist"].atk * 2))
            print(
                    game_state["protagonist"].moniker
                    + " hurled a bad-assed spear at "
                    + game_state["monster_name"] + "!")
            print(
                    game_state["monster_name"] + " HP: "
                    + str(game_state["monster_hp"]))
            game_state["protagonist"].inventory.remove(
                    inventory_dict["spear"])
        else:
            print(
                    game_state["protagonist"].moniker
                    + " doesn't have a bad-assed spear.")


class PotionItem:
    def __init__(self):
        self.item_name = "potion"
        self.gold_value = 10

    def use_item(self, game_state):
        inventory_dict = {}
        for inventory_item in game_state["protagonist"].inventory:
            inventory_dict[inventory_item.item_name] = inventory_item
        if "potion" in inventory_dict:
            game_state["protagonist"].hp = (
                    game_state["protagonist"].hp + 10)
            print(
                    game_state["protagonist"].moniker
                    + " chugs a delicious potion.")
            print(
                    game_state["protagonist"].moniker + " HP: "
                    + str(game_state["protagonist"].hp))
            game_state["player"].inventory.remove(
                    inventory_dict["potion"])
        else:
            print(
                    game_state["protagonist"].moniker
                    + " doesn't have a potion.")
            print("Sad face. :,(")

def turn_attack(game_state):
    print(
            game_state["protagonist"].moniker + " slashed "
            + game_state["monster_name"] + " with his sword.")
    if not game_state["monster_is_defending"]:
        game_state["monster_hp"] = (
                game_state["monster_hp"] - game_state["protagonist"].atk)
    else:
        game_state["monster_hp"] = (
                game_state["monster_hp"] - game_state["protagonist"].atk
                / 2)
    print(
            game_state["monster_name"] + " HP: "
            + str(game_state["monster_hp"]))


def turn_defend(game_state):
    game_state["protagonist"].is_defending = True
    print(game_state["protagonist"].moniker + " raises his shield.")


def turn_item(game_state):
    print("You have:")
    inventory_dict = {}
    for inventory_item in game_state["protagonist"].inventory:
        print("    " + inventory_item.item_name)
        inventory_dict[inventory_item.item_name] = inventory_item
    player_choice = input("Which do you want to use? ")
    try:
        item_method = inventory_dict[player_choice].use_item
    except KeyError:
        print(
                game_state["protagonist"].moniker
                + " isn't carrying that.")
    else:
        item_method(game_state)


def create_new_monster(game_state):
    game_state["monster_name"] = random.choice(["Gouki", "Baby Gouki"])
    if game_state["monster_name"] == "Baby Gouki":
        game_state["monster_hp"] = 15
        game_state["monster_atk"] = 8
        game_state["monster_gold_value"] = 5
    else:
        game_state["monster_hp"] = 20
        game_state["monster_atk"] = 15
        game_state["monster_gold_value"] = 10
    game_state["monster_is_defending"] = False


def take_player_turn(game_state):
    game_state["protagonist"].is_defending = False
    players_choice = input("Attack, defend, or item? ")
    if players_choice == "attack":
        turn_attack(game_state)
    elif players_choice == "defend":
        turn_defend(game_state)
    elif players_choice == "item":
        turn_item(game_state)
    else:
        print("You have to either 'attack', 'defend', or 'item'!")


def monster_turn_attack(game_state):
    print(
            game_state["monster_name"] + " tatsumaki'd "
            + game_state["protagonist"].moniker + "!")
    if game_state["protagonist"].is_defending:
        game_state["protagonist"].hp = (
                game_state["protagonist"].hp
                - (game_state["monster_atk"] / 2))
    else:
        game_state["protagonist"].hp = (
                game_state["protagonist"].hp
                - game_state["monster_atk"])
    print(
        game_state["protagonist"].moniker + " HP: "
        + str(game_state["protagonist"].hp))


def monster_turn_taunt(game_state):
    print(
            game_state["monster_name"] + " flexed its muscles and "
            + "talked a little smack.")


def monster_turn_defend(game_state):
    print(
            game_state["monster_name"] + " covered their soft belly.")
    game_state["monster_is_defending"] = True


def take_monster_turn(game_state):
    game_state["monster_is_defending"] = False
    monster_turn_options = [
            monster_turn_attack, monster_turn_defend, monster_turn_taunt]
    monster_action = random.choice(monster_turn_options)
    monster_action(game_state)


def do_battle(game_state):
    create_new_monster(game_state)
    print(game_state["monster_name"] + " is approaching!!")
    print()
    print(
            game_state["monster_name"] + " HP: "
            + str(game_state["monster_hp"]))
    print(
            game_state["protagonist"].moniker + " HP: "
            + str(game_state["protagonist"].hp))
    print()
    while (
            game_state["monster_hp"] > 0
            and game_state["protagonist"].hp > 0):
        take_player_turn(game_state)
        print()
        if game_state["monster_hp"] > 0:
            take_monster_turn(game_state)
            print()
    conclude_battle(game_state)


def conclude_battle(game_state):
    if game_state["protagonist"].hp > 0:
        print(game_state["protagonist"].moniker + " is victorious!")
        game_state["protagonist"].purse = (
                game_state["protagonist"].purse
                + game_state["monster_gold_value"])
        print(
                game_state["protagonist"].moniker + " earned "
                + str(game_state["monster_gold_value"]) + " gold!")
        print(
                game_state["protagonist"].moniker + " is now carrying "
                + str(game_state["protagonist"].purse) + " gold.")
    else:
        print(
                game_state["monster_name"] + " has slain "
                + game_state["protagonist"].moniker + "...")
        print("SHOOOOOSH!!")


def go_shopping(game_state):
    shop_inventory = {"spear": SpearItem(), "potion": PotionItem()}
    print(game_state["protagonist"].moniker + " walks into a shop.")
    print("The shopkeeper presents their available wares:")
    for item_key in shop_inventory:
        inventory_item = shop_inventory[item_key]
        print(
                "    " + item_key + ": " + str(inventory_item.gold_value))
    print()
    print(
            game_state["protagonist"].moniker + " is carrying "
            + str(game_state["protagonist"].purse) + " gold.")
    print()
    players_choice = input(
            "What're ya buyin'? Or do you wanna 'leave'? ")
    if players_choice == "leave":
        print(game_state["protagonist"].moniker + " leaves the shop.")
        return
    try:
        purchased_item = shop_inventory[players_choice]
    except KeyError:
        print("The shopkeeper isn't selling that. You leave the store.")
        return
    if game_state["protagonist"].purse >= purchased_item.gold_value:
        game_state["protagonist"].inventory.append(purchased_item)
        game_state["protagonist"].purse -= purchased_item.gold_value
        print(
                game_state["protagonist"].moniker
                + " has purchased a(n) " + purchased_item.item_name + ".")
    else:
        print(
                game_state["protagonist"].moniker + " can't afford a(n) "
                + purchased_item.item_name + ".")
        print("The shopkeeper kicks them out.")


game_state = {}
game_state["protagonist"] = Protagonist(input("What's your name, son? "))
while game_state["protagonist"].hp > 0:
    destination = input("Do you want to 'fight' or 'shop'? ")
    if destination == "fight":
        do_battle(game_state)
    elif destination == "shop":
        go_shopping(game_state)
    else:
        print("You have to either 'fight' or 'shop'.")
    print()
print("Game Over")
input("Press 'enter' to close.")
