#########################################################################
# pokemon_day_4_more_on_classes_commented.py                            #
#     - developed at twitch.tv/vencabot , Intro to Python 11/09/18      #
#     - watch the archived stream at ___________________________        #
#                                                                       #
# We're continuing development of our Pokemon battle example as a way   #
# to learn the very basics of programming.                              #
#                                                                       #
# By this point, we've introduced classes, but it's a deep-enough topic #
# that it begs elaboration -- and that's exactly what we did, in this   #
# session! We also reviewed the usages of our most complicated data     #
# types, including lists and dicts.                                     #
#                                                                       #
# As for NEW progress, we're utilizing 'inheritance' for the first      #
# time, in this session; the class 'PokemonMove' is a generic class     #
# which includes the attributes and methods that would be useful for    #
# any Pokemon move, and then classes like 'Tackle' and 'CombHair' can   #
# 'inherit' from or 'extend' PokemonMove, gaining access to all of its  #
# features without having to rewrite all of its code.                   #
#                                                                       #
# When the method of a parent class has been 'overridden' in a child    #
# class (replaced by a method of the same exact name), the parent's     #
# method can still be used via the 'super()' function, which returns    #
# the parent class and supplies 'self' to it as the object.             #
#                                                                       #
# So, for instance, even though Tackle.__init__() takes a different set #
# of arguments than PokemonMove.__init__(), because __init__ has been   #
# overridden, Tackle's __init__ can call super().__init__() to do all   #
# of the initializations that PokemonMove would've done.                #
#                                                                       #
# It sounds complex, but look at the code, below, and maybe you'll      #
# understand what I'm talking about!                                    #
#                                                                       #
#########################################################################

class PokemonMove:
    # This is the parent class that all other Pokemon moves will inherit.

    def __init__(self, owner, move_name, max_pp, elemental_type):
        # When initialized, all Pokemon moves need these attributes.

        # self.owner is the Pokemon object that owns this move.
        self.owner = owner

        # self.move_name is a plain-text name for the move. It might be
        # used for message-printing (as in self.print_startup(), below),
        # but it's definitely used as the move's key in the dictionary at
        # self.owner.move_dict . See Pokemon.move_dict below.
        self.move_name = move_name

        # How much PP this move has, directly after resting.
        self.max_pp = max_pp

        # self.current_pp gets updated whenever the move is used.
        self.current_pp = max_pp

        # Every move has an elemental_type (str), even if just 'normal'.
        self.elemental_type = elemental_type

    def print_startup(self, target):
        # If a child class doesn't override 'print_startup', running the
        # method will just print this generic message.
        print(
                self.owner.monster_type + " used '" + self.move_name
                + "' on " + target.monster_type + "!")

    def use_on(self, target):
        # This method will definitely be overridden by the child, since
        # all Pokemon moves need a 'use_on' method that causes the move
        # to be used. If they don't override, it just prints a message.
        self.print_startup(target)


class Tackle(PokemonMove):
    # This class inherits from (or 'extends') PokemonMove.
    # By default, it has all of the exact same methods and attributes,
    # but we can override those with new ones, too.
    
    def __init__(self, owner):
        # We override '__init__', here, to take fewer arguments. Then, we
        # just run PokemonMove's __init__ with some arguments that are
        # true of all Tackles.
        super().__init__(owner, "tackle", 10, "normal")

    def use_on(self, target):
        # Pretty much all child-classes of 'PokemonMove' will override
        # the 'use_on' method, since this is where the move's behavior is
        # defined.

        # If the move is out of PP, just print a message and stop.
        if self.current_pp == 0:
            print("'tackle' has no remaining PP!")
            return

        # If we made it this far, the move must have PP. Use tackle!
        # First, print a message for the user to know what's going on.
        print(
                self.owner.monster_type + " tackled "
                + target.monster_type + "!")

        # Calculate damage from the user's attack and target's defense.
        # self.owner and this method's 'target' argument are both
        # 'Pokemon' objects, so we know what kinds of attributes they
        # have, including 'attack' and 'defense'.
        actual_damage = self.owner.attack - target.defense

        # If a Tackle does negative damage, it'll heal the opponent.
        # Prevent this by making sure damage is at least 0.
        if actual_damage < 0:
            actual_damage = 0

        # The target Pokemon has its 'hp' attribute reduced. This is the
        # most important feature about classes and object-oriented pro-
        # gramming: objects have 'state' which can change. 'target' is
        # still the same 'Pokemon' object it ever was, but now its 'hp'
        # attribute has a different value.
        # This method doesn't belong to the target Pokemon; it belongs to
        # a 'Tackle' object that's owned by a completely different
        # Pokemon. Since we received 'target' as an attribute, however,
        # we're free to read and alter that Pokemon's attributes.
        # This opens up all kinds of doors and makes so many things
        # easier, but it also greatly increases the risk of bugs in your
        # code, because it can become difficult to tell WHERE an object's
        # attributes are being altered. If you use arguments and alter
        # attributes too liberally, debugging can be a huge pain in the
        # ass, which is why 'purely functional' programmers don't like to
        # use classes at all.
        # In this case, we're taking it for granted that, if you're using
        # a PokemonMove on a target Pokemon, you're expected to alter its
        # attributes -- but keep this in mind as you learn to flex the
        # great power that comes with classes: be very clear about what
        # attributes are being changed on your objects, and why!
        target.hp = target.hp - actual_damage

        # Print some messages about how much damage the target took.
        print(
                target.monster_type + " took " + str(actual_damage)
                + " damage!")
        print(
                target.monster_type + " has " + str(target.hp)
                + " HP remaining.")

        # Just as above, we're altering an object's 'state' in this line.
        # It isn't quite as dangerous, though, because we're changing an
        # attribute that actually belongs to the same object as this
        # method we're currently running.
        # It's expected that an object's methods will read and write that
        # object's attributes.
        self.current_pp = self.current_pp - 1
        print("'tackle' has " + str(self.current_pp) + " PP remaining.")


class CombHair(PokemonMove):
    # This second, simpler example of a PokemonMove was created to
    # demonstrate how many classes can inherit the same parent class.
    def __init__(self, owner):
        super().__init__(owner, "comb hair", 1, "normal")

    def use_on(self, target):
        print(self.owner.monster_type + " combs its hair.")


class Pokemon:
    # This class represents a character in our game which will be using
    # 'PokemonMove's.
    
    def __init__(
            self, monster_type, elemental_type, hp, attack, defense,
            move_class_list):
        # All of these attributes may be read and altered by a
        # 'PokemonMove', used for calculating damage and determining the
        # course of the battle.

        # self.monster_type is just a string to refer to this Pokemon.
        self.monster_type = monster_type

        # self.elemental_type is a string used in damage calculation.
        self.elemental_type = elemental_type

        # 'hp', 'attack', and 'defense' relate to damage-dealing moves.
        self.hp = hp
        self.attack = attack
        self.defense = defense

        # When a 'Pokemon' object is instantiated, causing __init__ to be
        # run, the last argument it takes is a list of classes which
        # refer to PokemonMoves.
        # The following four lines go through every class in that list,
        # instantiate an object from that PokemonMove class (create the
        # actual 'move' in question), and then save that new move to a
        # dictionary where its name (such as "tackle") is the key.

        # Create an empty dictionary for us to add keys to.
        self.move_dict = {}

        # Use a 'for' loop to iterate through items in the class list.
        for pokemon_move_class in move_class_list:
            # The current class in our list is 'pokemon_move_class'.

            # Instantiate the new move, supplying 'self' as the owner.
            # As you can see in 'Tackle' and 'CombHair' above, 'owner' is
            # the only argument necessary when instantiating a new move,
            # and it refers to the Pokemon object that will be using the
            # move. In this case, 'self' is the Pokemon object we're
            # currently constructing.
            new_move = pokemon_move_class(self)

            # Add the move to the dictionary, using its 'move_name'
            # attribute as the key.
            self.move_dict[new_move.move_name] = new_move


# Instantiate two Pokemon. Remember, when you instantiate (create an
# object from) a class, you're actually calling its __init__ method, so
# supply arguments accordingly.
pokemon1 = Pokemon("cyndaquil", "fire", 55, 8, 2, [Tackle, CombHair])
pokemon2 = Pokemon("squirtle", "water", 68, 6, 4, [Tackle, CombHair])

# Get the move at key "tackle" in this Pokemon's move_dict, and then run
# its 'use_on' method on the supplied target, pokemon2.
pokemon1.move_dict["tackle"].use_on(pokemon2)
