class PPError(Exception):
    pass


class PokemonMove:
    def __init__(self, owner, move_name, max_pp, elemental_type):
        self.owner = owner
        self.move_name = move_name
        self.max_pp = max_pp
        self.current_pp = max_pp
        self.elemental_type = elemental_type

    def use_on(self, target):
        if self.current_pp == 0:
            raise PPError
        self._take_effect(target)
        self.current_pp = self.current_pp - 1
        print(
                self.move_name + " has " + str(self.current_pp)
                + " PP remaining.")

    def _take_effect(self, target):
        print(
                self.owner.nickname + " used " + self.move_name + " on "
                + target.nickname + ".")


class Tackle(PokemonMove):
    def __init__(self, owner):
        super().__init__(owner, "tackle", 10, "normal")

    def _take_effect(self, target):
        print(
                self.owner.nickname + " the " + self.owner.monster_type
                + " tackled " + target.nickname + " the "
                + target.monster_type + "!")
        actual_damage = self.owner.attack - target.defense
        if actual_damage <= 0:
            actual_damage = 1
        target.hp = target.hp - actual_damage
        print(
                target.nickname + " the " + target.monster_type
                + " took " + str(actual_damage) + " damage!")
        print(
                target.nickname + " the " + target.monster_type + " has "
                + str(target.hp) + " HP remaining.")
        

class CombHair(PokemonMove):
    def __init__(self, owner):
        super().__init__(owner, "comb hair", 1, "normal")

    def _take_effect(self, target):
        print(
                self.owner.nickname + " the " + self.owner.monster_type
                + " combs its hair.")


class Growl(PokemonMove):
    def __init__(self, owner):
        super().__init__(owner, "growl", 10, "normal")

    def _take_effect(self, target):
        print(
                self.owner.nickname + " growled menacingly at "
                + target.nickname)
        if target.attack > 0:
            target.attack = target.attack - 1
            print(target.nickname + " backed off!")
        else:
            print(target.nickname + " can't get any weaker!")


class Flamethrower(PokemonMove):
    def __init__(self, owner):
        super().__init__(owner, "flamethrower", 5, "fire")

    def _take_effect(self, target):
        print(
                self.owner.nickname + " blew flames at " + target.nickname
                + ".")
        if target.elemental_type == "grass":
            actual_damage = self.owner.attack * 2 - target.defense
            print("It's super effective!")
        else:
            actual_damage = self.owner.attack - target.defense
        if actual_damage <= 0:
            actual_damage = 1
        target.hp = target.hp - actual_damage
        print(
                target.nickname + " took " + str(actual_damage)
                + " damage!")
        print(
                target.nickname + " has " + str(target.hp)
                + " HP remaining.")


class Vinewhip(PokemonMove):
    def __init__(self, owner):
        super().__init__(owner, "vinewhip", 5, "grass")

    def _take_effect(self, target):
        print(
                self.owner.nickname + " whipped a vine at "
                + target.nickname + ".")
        if (
                target.elemental_type == "rock"
                or target.elemental_type == "ground"):
            actual_damage = self.owner.attack * 2 - target.defense
            print("It's super effective!")
        else:
            actual_damage = self.owner.attack - target.defense
        if actual_damage <= 0:
            actual_damage = 1
        target.hp = target.hp - actual_damage
        print(
                target.nickname + " took " + str(actual_damage)
                + " damage!")
        print(
                target.nickname + " has " + str(target.hp)
                + " HP remaining.")

class LightUp(PokemonMove):
    def __init__(self, owner):
        super().__init__(owner, "light up", 3, "grass")

    def _take_effect(self, target):
        print(self.owner.nickname + " lit up!")
        self.owner.defense = self.owner.defense + 2
