def turn_attack(game_state):
    print(
            game_state["protagonist_name"] + " slashed "
            + game_state["monster_name"] + " with his sword.")
    game_state["monster_hp"] = (
            game_state["monster_hp"] - game_state["protagonist_atk"])
    print(
            game_state["monster_name"] + " HP: "
            + str(game_state["monster_hp"]))


def turn_defend(game_state):
    game_state["player_is_defending"] = True
    print(game_state["protagonist_name"] + " raises his shield.")


def turn_item(game_state):
    item_map = {
            "spear": item_spear,
            "roll of toilet paper": item_roll_of_toilet_paper,
            "potion": item_potion,
            "thumb-drive": item_thumb_drive}
    print("You have:")
    for inventory_item in game_state["player_inventory"]:
        print("    " + inventory_item)
    player_choice = input("Which do you want to use? ")
    try:
        item_function = item_map[player_choice]
    except KeyError:
        print(game_state["protagonist_name"] + " isn't carrying that.")
    else:
        item_function(game_state)


def item_spear(game_state):
    if "spear" in game_state["player_inventory"]:
        game_state["monster_hp"] = (
                game_state["monster_hp"]
                - (game_state["protagonist_atk"] * 2))
        print(
                game_state["protagonist_name"]
                + " hurled a bad-assed spear at "
                + game_state["monster_name"] + "!")
        print(
                game_state["monster_name"] + " HP: "
                + str(game_state["monster_hp"]))
        game_state["player_inventory"].remove("spear")
    else:
        print(
                game_state["protagonist_name"]
                + " doesn't have a bad-assed spear.")


def item_roll_of_toilet_paper(game_state):
    if "roll of toilet paper" in game_state["player_inventory"]:
        print(
                game_state["protagonist_name"]
                + " hurled a roll of toilet paper at "
                + game_state["monster_name"] + ".")
        print("It wasn't very effective.")
        game_state["player_inventory"].remove("roll of toilet paper")
    else:
        print(
                game_state["protagonist_name"]
                + " doesn't have a roll of toilet paper.")
        print("Probably gonna need to do something about that, later.")


def item_potion(game_state):
    if "potion" in game_state["player_inventory"]:
        game_state["protagonist_hp"] = game_state["protagonist_hp"] + 10
        print(
                game_state["protagonist_name"]
                + " chugs a delicious potion.")
        print(
                game_state["protagonist_name"] + " HP: "
                + str(game_state["protagonist_hp"]))
        game_state["player_inventory"].remove("potion")
    else:
        print(
                game_state["protagonist_name"]
                + " doesn't have a potion.")
        print("Sad face. :,(")


def item_thumb_drive(game_state):
    print("No one can ever know what's on this drive.")


game_state = {}
game_state["protagonist_name"] = input("What's your name, son? ")
game_state["protagonist_hp"] = 25
game_state["protagonist_atk"] = 6
game_state["player_is_defending"] = False
game_state["player_inventory"] = [
        "spear", "roll of toilet paper", "potion", "thumb-drive"]

game_state["monster_name"] = input("What monster do you face? ")
game_state["monster_hp"] = 20
game_state["monster_atk"] = 6

print(
        game_state["monster_name"] + " HP: "
        + str(game_state["monster_hp"]))
print(
        game_state["protagonist_name"] + " HP: "
        + str(game_state["protagonist_hp"]))
print()

while game_state["monster_hp"] > 0 and game_state["protagonist_hp"] > 0:
    game_state["player_is_defending"] = False
    players_choice = input("Attack, defend, or item? ")
    if players_choice == "attack":
        turn_attack(game_state)
    elif players_choice == "defend":
        turn_defend(game_state)
    elif players_choice == "item":
        turn_item(game_state)
    else:
        print("You have to either 'attack', 'defend', or 'item'!")
        continue
    print()

    if game_state["monster_hp"] > 0:      
        print(
                game_state["monster_name"] + " burninated "
                + game_state["protagonist_name"] + "!")
        if game_state["player_is_defending"]:
            game_state["protagonist_hp"] = (
                    game_state["protagonist_hp"]
                    - (game_state["monster_atk"] / 2))
        else:
            game_state["protagonist_hp"] = (
                    game_state["protagonist_hp"]
                    - game_state["monster_atk"])
        print(
            game_state["protagonist_name"] + " HP: "
            + str(game_state["protagonist_hp"]))
        print()

if game_state["protagonist_hp"] > 0:
    print(game_state["protagonist_name"] + " is victorious!")
else:
    print(
            game_state["monster_name"] + " has slain "
            + game_state["protagonist_name"] + "...")

print("Game Over")
input("Press 'enter' to close.")
