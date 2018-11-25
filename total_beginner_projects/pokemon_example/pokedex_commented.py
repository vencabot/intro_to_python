#########################################################################
# pokedex_commented.py                                                  #
#     - developed at twitch.tv/vencabot , Intro to Python 11/23/18      #
#     - watch the archived stream at ___________________________        #
#                                                                       #
# This module is imported by 'pokemon_day_6_using_modules_commented.py' #
# so that it isn't all cluttered up by a bunch of Pokemon definitions.  #
#                                                                       #
# All we're doing here is defining the attributes of a bunch of Pokemon #
# that can be used for battle.                                          #
#                                                                       #
#########################################################################

# Our Pokemon need moves to use. We didn't want to clutter up this file,
# so we moved them all to their own module.
# We're using the 'import MODULE_NAME as ALIAS' syntax so that we don't
# need to keep typing the 'commented' suffix over and over again.
import pokemon_moves_commented as pokemon_moves

# 'Pokemon' is the generic Pokemon class that all other, more specific
# classes of Pokemon inherit from. So, all other Pokemon classes inherit
# the 'use' method, which is a shorthand way for using attacks that
# doesn't require manually finding a Pokemon's move-instances.
# Plus, all types of Pokemon will use 'Pokemon's __init__ method to
# easily get set up with a bunch of attributes and get their move classes
# instantiated into actual PokemonMove objects.
class Pokemon:
    def __init__(
            self, nickname, monster_type, elemental_type, base_hp,
            base_attack, base_defense, move_class_list):

        # Attach the supplied attributes to this Pokemon.
        self.nickname = nickname
        self.monster_type = monster_type
        self.elemental_type = elemental_type
        self.base_hp = base_hp
        self.hp = base_hp
        self.base_attack = base_attack
        self.attack = base_attack
        self.base_defense = base_defense
        self.defense = base_defense

        # Set up the Pokemon's starting level and experience.
        self.level = 1
        self.experience = 0
        self.exp_required_for_level = 50

        # Use the supplied list of PokemonMove classes to instantiate
        # moves that this Pokemon can use. Organize them in a dictionary
        # where each move's key is its name (a string, such as "tackle").
        self.move_dict = {}
        for pokemon_move_class in move_class_list:
            new_move = pokemon_move_class(self)
            self.move_dict[new_move.move_name] = new_move

    # As stated above, this method is just to make our code look nicer.
    # This allows a programmer to use a Pokemon's move simply by
    # supplying the move's name and a target Pokemon.
    # Without this method, the programmer would need to manually use the
    # Pokemon's move_dict to access the PokemonMove instance's 'use_on'
    # method, as seen below.
    # Just a time saver, and it makes our later code easier to read!
    # Would you rather:
    #     pokemon_a.use("tackle", pokemon_b)
    # or:
    #     pokemon_a.move_dict["tackle"].use_on(pokemon_b)
    # ?
    def use(self, move_name, target):
        self.move_dict[move_name].use_on(target)


# All of the classes, below, represent types of Pokemon. As such, they
# unsurprisingly inherit from the 'Pokemon' class.
# Since 'Pokemon' pretty much defines all of the features and
# functionality that any monster needs, all of these inheriting classes
# are super simple: they just override 'Pokemon's __init__ with a method
# that just runs 'Pokemon's __init__, via the 'super' function, supplying
# attributes unique to each type of Pokemon.

class Cyndaquil(Pokemon):
    def __init__(self, nickname):
        move_classes = [
                pokemon_moves.Tackle, pokemon_moves.CombHair,
                pokemon_moves.Growl]
        super().__init__(
                nickname, "cyndaquil", "fire", 24, 8, 2, move_classes)


class Machamp(Pokemon):
    def __init__(self, nickname):
        move_classes = [pokemon_moves.Tackle, pokemon_moves.CombHair]
        super().__init__(
                nickname, "machamp", "fighting", 40, 13, 6, move_classes)


class Ganja(Pokemon):
    def __init__(self, nickname):
        move_classes = [
                pokemon_moves.Tackle, pokemon_moves.CombHair,
                pokemon_moves.Vinewhip, pokemon_moves.LightUp]
        super().__init__(
                nickname, "ganja", "grass", 28, 5, 5, move_classes)


class Geodude(Pokemon):
    def __init__(self, nickname):
        move_classes = [pokemon_moves.Tackle]
        super().__init__(
                nickname, "geodude", "rock", 32, 8, 6, move_classes)
