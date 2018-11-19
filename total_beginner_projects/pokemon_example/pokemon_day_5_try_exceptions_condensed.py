import random

class PPError(Exception):
    pass


class PokemonMove:
    def __init__(self, owner, move_name, max_pp, elemental_type):
        self.owner = owner
        self.move_name = move_name
        self.max_pp = max_pp
        self.current_pp = max_pp
        self.elemental_type = elemental_type

    def print_startup(self, target):
        print(
                self.owner.nickname + " the " + self.owner.monster_type
                + " used '" + self.move_name + "' on "
                + target.nickname + " the " + target.monster_type + "!")

    def use_on(self, target):
        self.print_startup(target)


class Tackle(PokemonMove):
    def __init__(self, owner):
        super().__init__(owner, "tackle", 10, "normal")

    def use_on(self, target):
        if self.current_pp == 0:
            raise PPError
        print(
                self.owner.nickname + " the " + self.owner.monster_type
                + " tackled " + target.nickname + " the "
                + target.monster_type + "!")
        actual_damage = self.owner.attack - target.defense
        if actual_damage < 0:
            actual_damage = 0
        target.hp = target.hp - actual_damage
        print(
                target.nickname + " the " + target.monster_type
                + " took " + str(actual_damage) + " damage!")
        print(
                target.nickname + " the " + target.monster_type + " has " + str(target.hp)
                + " HP remaining.")
        self.current_pp = self.current_pp - 1
        print("'tackle' has " + str(self.current_pp) + " PP remaining.")


class CombHair(PokemonMove):
    def __init__(self, owner):
        super().__init__(owner, "comb hair", 1, "normal")

    def use_on(self, target):
        if self.current_pp == 0:
            raise PPError
        print(
                self.owner.nickname + " the " + self.owner.monster_type
                + " combs its hair.")
        self.current_pp = self.current_pp - 1


class Pokemon:
    def __init__(
            self, nickname, monster_type, elemental_type, hp, attack,
            defense, move_class_list):
        self.nickname = nickname
        self.monster_type = monster_type
        self.elemental_type = elemental_type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.move_dict = {}
        for pokemon_move_class in move_class_list:
            new_move = pokemon_move_class(self)
            self.move_dict[new_move.move_name] = new_move

    def use(self, move_name, target):
        self.move_dict[move_name].use_on(target)


class Cyndaquil(Pokemon):
    def __init__(self, nickname):
        super().__init__(
                nickname, "cyndaquil", "fire", 55, 8, 2,
                [Tackle, CombHair])
        

class Machamp(Pokemon):
    def __init__(self, nickname):
        super().__init__(
                nickname, "machamp", "fighting", 80, 20, 6,
                [Tackle, CombHair])


pokemon1 = Cyndaquil("Zanzhu")
pokemon2 = Cyndaquil("Dixxucker")

# This is where the Pokemon battle starts.
while pokemon1.hp > 0 and pokemon2.hp > 0:
    # This is our Pokemon's turn.
    print()
    user_input = input(
            "What move should " + pokemon1.nickname + " the "
            + pokemon1.monster_type + " use? ")
    try:
        pokemon1.use(user_input, pokemon2)
    except KeyError:
        print(pokemon1.nickname + " doesn't know " + user_input + "!")
        continue
    except PPError:
        print(user_input + " has no remaining PP!")
        continue
    print()
    # This is the opponent Pokemon's turn.
    if pokemon2.hp > 0:
        available_moves = []
        for move_instance in pokemon2.move_dict.values():
            if (
                    pokemon2.nickname == "Dixxucker"
                    and move_instance.move_name == "comb hair"):
                continue
            if move_instance.current_pp > 0:
                available_moves.append(move_instance)
        if len(available_moves) == 0:
            print(
                    pokemon2.nickname + " the " + pokemon2.monster_type
                    + " has no available moves!")
            continue
        random_move = random.choice(available_moves)
        random_move.use_on(pokemon1)
winner = pokemon1 if pokemon1.hp > 0 else pokemon2
loser = pokemon2 if winner is pokemon1 else pokemon1
print(loser.nickname + " the " + loser.monster_type + " has fainted!")
print(
        winner.nickname + " the " + winner.monster_type
        + " is the winner!")
