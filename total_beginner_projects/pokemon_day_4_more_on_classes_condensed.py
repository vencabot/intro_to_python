class PokemonMove:
    def __init__(self, owner, move_name, max_pp, elemental_type):
        self.owner = owner
        self.move_name = move_name
        self.max_pp = max_pp
        self.current_pp = max_pp
        self.elemental_type = elemental_type

    def print_startup(self, target):
        print(
                self.owner.monster_type + " used '" + self.move_name
                + "' on " + target.monster_type + "!")

    def use_on(self, target):
        self.print_startup(target)


class Tackle(PokemonMove):
    def __init__(self, owner):
        super().__init__(owner, "tackle", 10, "normal")

    def use_on(self, target):
        if self.current_pp == 0:
            print("'tackle' has no remaining PP!")
            return
        print(
                self.owner.monster_type + " tackled "
                + target.monster_type + "!")
        actual_damage = self.owner.attack - target.defense
        if actual_damage < 0:
            actual_damage = 0
        target.hp = target.hp - actual_damage
        print(
                target.monster_type + " took " + str(actual_damage)
                + " damage!")
        print(
                target.monster_type + " has " + str(target.hp)
                + " HP remaining.")
        self.current_pp = self.current_pp - 1
        print("'tackle' has " + str(self.current_pp) + " PP remaining.")


class CombHair(PokemonMove):
    def __init__(self, owner):
        super().__init__(owner, "comb hair", 1, "normal")

    def use_on(self, target):
        print(self.owner.monster_type + " combs its hair.")


class Pokemon:
    def __init__(
            self, monster_type, elemental_type, hp, attack, defense,
            move_class_list):
        self.monster_type = monster_type
        self.elemental_type = elemental_type
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.move_dict = {}
        for pokemon_move_class in move_class_list:
            new_move = pokemon_move_class(self)
            self.move_dict[new_move.move_name] = new_move


pokemon1 = Pokemon("cyndaquil", "fire", 55, 8, 2, [Tackle, CombHair])
pokemon2 = Pokemon("squirtle", "water", 68, 6, 4, [Tackle, CombHair])

pokemon1.move_dict["tackle"].use_on(pokemon2)
