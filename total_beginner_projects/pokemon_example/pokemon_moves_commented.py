#########################################################################
# pokemon_moves_commented.py                                            #
#     - developed at twitch.tv/vencabot , Intro to Python 11/23/18      #
#     - watch the archived stream at ___________________________        #
#                                                                       #
# This module is imported by 'pokemon_day_6_using_modules_commented.py' #
# and 'pokedex_commented.py' so that they aren't all cluttered up by a  #
# bunch of PokemonMove definitions.                                     #
#                                                                       #
# All we're doing here is defining the attributes and effects of a      #
# bunch of moves that can be used by a given Pokemon during battle.     #
#                                                                       #
#########################################################################

# This simple Exception is meant to be raised whenever a PokemonMove is
# called upon but doesn't have any PP (ammo) remaining.
# The only reason that we give it a special name is so that it can be
# targeted specifically by the 'except' statement. That being the case,
# it doesn't require any special properties, so we can just 'pass'
# instead of overriding anything from the parent class, 'Exception'.
class PPError(Exception):
    pass


# This generic class is meant to be inherited from. It defines everything
# that a Pokemon move needs. Basically, individual Pokemon moves will
# just inherit from 'PokemonMove' and override its '__init__' with
# something that just calls the parent __init__ with special arguments.
# '_take_effect' should also be overridden by any child classes, since
# it defines what actually HAPPENS when a move is used.
class PokemonMove:
    def __init__(self, owner, move_name, max_pp, elemental_type):
        # We're just defining some attributes of this move.
        # The Pokemon instance that this move belongs to.
        self.owner = owner

        # A string representing the move's name, such as "tackle".
        self.move_name = move_name

        # An integer: how many times the move can be used after resting.
        self.max_pp = max_pp

        # An integer: how many uses are left before resting again.
        self.current_pp = max_pp

        # A string representing the move's element, such as "fire".
        self.elemental_type = elemental_type

    # This method, 'use_on', isn't meant to be overridden. If this move
    # has PP, use_on calls the '_take_effect' method, then subtracts 1 PP
    # and reports the remaining PP to the player.
    def use_on(self, target):
        if self.current_pp == 0:
            raise PPError
        self._take_effect(target)
        self.current_pp = self.current_pp - 1
        print(
                self.move_name + " has " + str(self.current_pp)
                + " PP remaining.")

    # Every child class of PokemonMove should override this method to
    # define what the move actually does, since this is what 'use_on'
    # calls whenever a move is used.
    # The default behavior, shown here, is to just print a string that
    # explains that the move was used. Pretty useless.
    def _take_effect(self, target):
        print(
                self.owner.nickname + " used " + self.move_name + " on "
                + target.nickname + ".")


# 'tackle' just inflicts a normal amount of 'normal'-element damage.
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
        

# 'comb hair' doesn't inflict any damage; it just prints a message. Since
# it only has 1 PP, it's used for testing PPError.
class CombHair(PokemonMove):
    def __init__(self, owner):
        super().__init__(owner, "comb hair", 1, "normal")

    def _take_effect(self, target):
        print(
                self.owner.nickname + " the " + self.owner.monster_type
                + " combs its hair.")


# 'growl' reduces the target's attack power.
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


# 'flamethrower' deals fire-elemental damage. Extra damage against grass!
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


# 'vinewhip' is basically flamethrower, but grass-flavored. It does extra
# damage against 'rock' AND 'ground' types!
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


# The special move of the Pokemon 'ganja'. Raises the user's defense.
class LightUp(PokemonMove):
    def __init__(self, owner):
        super().__init__(owner, "light up", 3, "grass")

    def _take_effect(self, target):
        print(self.owner.nickname + " lit up!")
        self.owner.defense = self.owner.defense + 2
