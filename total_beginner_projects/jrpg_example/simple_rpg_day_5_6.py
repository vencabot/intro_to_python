import random

class Protagonist:
    def __init__(self, protagonist_name, parent_game_state):
        self.moniker = protagonist_name
        self.parent_game_state = parent_game_state
        if self.moniker == "Chun Li":
            print("You're the strongest woman in the world!")
            self.atk = 10
        else:
            self.atk = 6
        self.hp = 25
        self.is_defending = False
        self.inventory = [
                SpearItem(parent_game_state),
                PotionItem(parent_game_state),
                PoisonedDaggerItem(parent_game_state)]
        self.purse = 0

    def take_turn(self):
        self.is_defending = False
        players_choice = input("Attack, defend, or item? ")
        if players_choice == "attack":
            self.attack()
        elif players_choice == "defend":
            self.defend()
        elif players_choice == "item":
            self.use_item()
        else:
            print("You have to either 'attack', 'defend', or 'item'!")

    def attack(self):
        monster = self.parent_game_state["monster"]
        print(
                self.moniker + " slashed " + monster.monster_type
                + " with his sword.")
        if not monster.is_defending:
            attack_damage = self.atk
        else:
            attack_damage = self.atk / 2
        monster.hp -= attack_damage

    def defend(self):
        self.is_defending = True
        print(self.moniker + " raises his shield.")

    def use_item(self):
        print("You have:")
        inventory_dict = {}
        for inventory_item in self.inventory:
            print("    " + inventory_item.item_name)
            inventory_dict[inventory_item.item_name] = inventory_item
        player_choice = input("Which do you want to use? ")
        try:
            item_method = inventory_dict[player_choice].use
        except KeyError:
            print(self.moniker + " isn't carrying that.")
        else:
            item_method()


class Monster:
    def __init__(
            self, monster_type, atk, hp, gold_value, parent_game_state):
        self.monster_type = monster_type
        self.atk = atk
        self.hp = hp
        self.gold_value = gold_value
        self.parent_game_state = parent_game_state
        self.is_defending = False
        self.is_poisoned = False

    def take_turn(self):
        self.is_defending = False
        if self.is_poisoned:
            print(self.monster_type + " rubs some sweat off its brow...")
            print(self.monster_type + " is damaged by the poison!!")
            self.hp -= 3
            if self.hp <= 0:
                print(
                        self.monster_type + " crossed its eyes and "
                        + "dropped DEAD from the poison!")
                return
        turn_options = [self.attack, self.defend, self.taunt]
        monster_action = random.choice(turn_options)
        monster_action()

    def attack(self):
        protagonist = self.parent_game_state["protagonist"]
        print(
                self.monster_type + " tatsumaki'd " + protagonist.moniker
                + "!")
        if protagonist.is_defending:
            attack_damage = self.atk / 2
        else:
            attack_damage = self.atk
        protagonist.hp -= attack_damage

    def taunt(self):
        print(
                self.monster_type + " flexed its muscles and talked a "
                + "little smack.")

    def defend(self):
        print(self.monster_type + " covered their soft belly.")
        self.is_defending = True


class BabyGouki(Monster):
    def __init__(self, parent_game_state):
        self.monster_type = "Baby Gouki"
        self.atk = 8
        self.hp = 15
        self.gold_value = 5
        self.parent_game_state = parent_game_state
        self.is_defending = False
        self.is_poisoned = False


class Gouki(Monster):
    def __init__(self, parent_game_state):
        self.monster_type = "Gouki"
        self.atk = 15
        self.hp = 20
        self.gold_value = 10
        self.parent_game_state = parent_game_state
        self.is_defending = False
        self.is_poisoned = False


class Dragon(Monster):
    def __init__(self, parent_game_state):
        self.monster_type = "Billy the dragon"
        self.atk = 20
        self.hp = 40
        self.gold_value = 50
        self.parent_game_state = parent_game_state
        self.is_defending = False
        self.is_poisoned = False


class Unicorn(Monster):
    def __init__(self, parent_game_state):
        self.monster_type = "Stacy the unicorn"
        self.atk = 3
        self.hp = 100
        self.gold_value = 100
        self.parent_game_state = parent_game_state
        self.is_defending = False
        self.is_poisoned = False


class SpearItem:
    def __init__(self, parent_game_state):
        self.parent_game_state = parent_game_state
        self.item_name = "spear"
        self.gold_value = 15

    def use(self):
        protagonist = self.parent_game_state["protagonist"]
        monster = self.parent_game_state["monster"]
        if self in protagonist.inventory:
            monster.hp -= protagonist.atk * 2
            print(
                    protagonist.moniker + " hurled a bad-assed spear at "
                    + monster.monster_type + "!")
            print(monster.monster_type + " HP: " + str(monster.hp))
            protagonist.inventory.remove(self)
        else:
            print(
                    protagonist.moniker + " doesn't have a bad-assed"
                    + " spear.")


class PotionItem:
    def __init__(self, parent_game_state):
        self.parent_game_state = parent_game_state
        self.item_name = "potion"
        self.gold_value = 10

    def use(self):
        protagonist = self.parent_game_state["protagonist"]
        if self in protagonist.inventory:
            protagonist.hp += 10
            print(protagonist.moniker + " chugs a delicious potion.")
            print(protagonist.moniker + " HP: " + str(protagonist.hp))
            protagonist.inventory.remove(self)
        else:
            print(protagonist.moniker + " doesn't have a potion.")
            print("Sad face. :,(")


class PoisonedDaggerItem:
    def __init__(self, parent_game_state):
        self.parent_game_state = parent_game_state
        self.item_name = "poisoned dagger"
        self.gold_value = 15

    def use(self):
        protagonist = self.parent_game_state["protagonist"]
        monster = self.parent_game_state["monster"]
        if self in protagonist.inventory:
            print(
                    protagonist.moniker + " chucks a poisoned dagger at "
                    + monster.monster_type + "!")
            print("The dagger finds its mark!")
            monster.is_poisoned = True
            protagonist.inventory.remove(self)
        else:
            print(protagonist.moniker + " doesn't have a dagger.")
            print("Sad face. :,(")


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


def do_battle(game_state):
    monster_class = random.choice(game_state["monster_classes"])
    game_state["monster"] = monster_class(game_state)
    print(game_state["monster"].monster_type + " is approaching!!")
    print()
    while (
            game_state["monster"].hp > 0
            and game_state["protagonist"].hp > 0):
        print(
                game_state["monster"].monster_type + " HP: "
                + str(game_state["monster"].hp))
        print(
                game_state["protagonist"].moniker + " HP: "
                + str(game_state["protagonist"].hp))
        print()
        game_state["protagonist"].take_turn()
        print()
        if game_state["monster"].hp > 0:
            game_state["monster"].take_turn()
            print()
    conclude_battle(game_state)


def conclude_battle(game_state):
    if game_state["protagonist"].hp > 0:
        print(game_state["protagonist"].moniker + " is victorious!")
        game_state["protagonist"].purse = (
                game_state["protagonist"].purse
                + game_state["monster"].gold_value)
        print(
                game_state["protagonist"].moniker + " earned "
                + str(game_state["monster"].gold_value) + " gold!")
        print(
                game_state["protagonist"].moniker + " is now carrying "
                + str(game_state["protagonist"].purse) + " gold.")
    else:
        print(
                game_state["monster"].monster_type + " has slain "
                + game_state["protagonist"].moniker + "...")
        print("SHOOOOOSH!!")


def go_shopping(game_state):
    shop_inventory = {
            "spear": SpearItem(game_state),
            "potion": PotionItem(game_state),
            "poisoned dagger": PoisonedDaggerItem(game_state)}
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
game_state["monster_classes"] = [BabyGouki, Gouki, Dragon, Unicorn]
protagonist_name = input("What's your name, son? ")
game_state["protagonist"] = Protagonist(protagonist_name, game_state)
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
