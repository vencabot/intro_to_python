#########################################################################
# pokemon_day_3_learning_classes_commented.py                           #
#     - developed at twitch.tv/vencabot , Intro to Python 10/26/18      #
#     - watch the archived stream at ___________________________        #
#                                                                       #
# This is the third day (and third form) of our 'pokemon' project,      #
# where we're learning the very basics of programming by creating a     #
# Pokemon-like RPG.                                                     #
#                                                                       #
# Previously, we'd gotten a simple Pokemon battle fully working using   #
# only the very basics of programming: simple data types, simple oper-  #
# ations, and simple logical blocks such as 'if', 'else', and 'while'.  #
#                                                                       #
# In this script, we're beginning to learn about 'Object Oriented       #
# Programming', which is a way of thinking about code as the inter-     #
# action of conceptual 'things' rather than just as a cascade of linear #
# instructions.                                                         #
#                                                                       #
# For instance, in our old code, the attributes of all Pokemon and all  #
# moves were made up of simple variable assignments made at the start   #
# of our program. The limitation of this is that the size and complex-  #
# ity of our code multiplies every time we want to add a new monster or #
# a new type of attack. Wouldn't it be simpler if we could, instead,    #
# define what a 'Pokemon' or a 'move' is and what they do so that we    #
# could easily create countless variations of them?                     #
#                                                                       #
# Well, that's exactly what we're doing here by creating and using      #
# 'classes'. Once you use a class to define a certain type of hypo-     #
# thetical object, you can easily construct objects of that type which  #
# have similar 'attributes' (variables that BELONG to the object) and   #
# 'methods' (functions that BELONG to the object, defining what it can  #
# do).                                                                  #
#                                                                       #
# Although we weren't able to get the combat loop working in time for   #
# the end of the stream, you can already see how much easier it will be #
# to create and organize new types of monsters and new types of moves   #
# now that we're using classes!                                         #
#                                                                       #
#########################################################################

# Define a new type of object that represents a Pokemon move, "tackle".
class PokemonMoveTackle:
    # A function that belongs to a class of object is called a 'method'.
    # A method whose name starts and ends with '__' is special.
    # These methods aren't usually used explicitly, but are used
    # automatically, by Python, under certain circumstances.
    # '__init__' is always run when this class is 'instantiated'.
    # In other words, it's run when an object of this type is created.
    def __init__(self, owner):
        # What sorts of 'attributes' does 'tackle' need in order to work?

        # It needs to know what Pokemon is using it, to access their
        # name (for printing) and attack power (for damage calculation).
        self.owner = owner

        # Having a 'move name' will be handy for sorting moves, later.
        self.move_name = "tackle"

        # It needs a max and current PP value. 'current_pp' starts full.
        self.max_pp = 10
        self.current_pp = self.max_pp

        # Moves have an elemental type to use for damage calculation.
        self.elemental_type = "normal"

    # We're gonna run the 'use_on' method when we wanna tackle something!
    def use_on(self, target):
        # First, make sure we have enough PP to execute this move.
        if self.current_pp == 0:
            print("'tackle' has no remaining PP!")

            # Crap, we're out of PP. Just exit the method with 'return'.
            return

        # We have enough PP! Tell the player that a tackle is occuring!
        print(
                self.owner.monster_type + " tackled "
                + target.monster_type + "!")

        # Calculate damage, but make sure it doesn't go into negatives.
        actual_damage = self.owner.attack - target.defense
        if actual_damage < 0:
            actual_damage = 0

        # Deal the calculated damage to the opponent's HP.
        target.hp = target.hp - actual_damage

        # Give the player some messages about the damage.
        print(
                target.monster_type + " took " + str(actual_damage)
                + " damage!")
        print(
                target.monster_type + " has " + str(target.hp)
                + " HP remaining.")

        # Reduce the move's PP by '1' and report the remaining PP.
        self.current_pp = self.current_pp - 1
        print("'tackle' has " + str(self.current_pp) + " PP remaining.")


# Define a type of object which represents an entire Pokemon.
class Pokemon:
    # Arguments to '__init__' are passed in when the object is created.
    def __init__(
            self, monster_type, elemental_type, hp, attack, defense,
            move_class_list):
        # Save our arguments as attributes of this monster.
        self.monster_type = monster_type
        self.elemental_type = elemental_type
        self.hp = hp
        self.attack = attack
        self.defense = defense

        # This next bit is kind of tricky, but fun. Let's talk about it!
        # First, we create a new 'dict', where we can use any type of
        # data to REFER to any other type of data.
        # In this case, we're going to use Pokemon move names (strings)
        # to refer to actual move objects (such as instances of our
        # PokemonMoveTackle class, above).
        # In other words, we're sorting moves by their name.
        self.move_dict = {}

        # When a Pokemon is being created, the last argument is a list of
        # classes representing each of that Pokemon's moves.
        # Right now, our program only has one class of move, called
        # PokemonMoveTackle. Looking below, where we create our two
        # Pokemon, both of their move_class_list's only contain one
        # class, for now, and it's PokemonMoveTackle.

        # We're going to use a 'for' loop to take each item in the
        # supplied 'move_class_list' and use it in a special way.
        # After 'for', the first name is a variable name that will
        # contain whatever our current item in the list is.
        # Then, in the intended block, we can use that variable.
        # The block gets executed for every item in the list.
        for pokemon_move_class in move_class_list:
            # For each class in the list, instantiate (create) a move of
            # that type.
            # PokemonMoveTackle (and, in the future, other move classes)
            # require one argument: a 'Pokemon' that is the owner of that
            # move. In this case, we're supplying 'self', which is the
            # Pokemon that we're creating.
            new_move = pokemon_move_class(self)

            # Add the newly instantiated move to our collection of moves,
            # 'move_dict', and refer to it by its 'move_name'.
            # Now, we can refer to our new 'tackle' using
            # self.move_dict["tackle"] .
            self.move_dict[new_move.move_name] = new_move

# Instantiate (create) a couple of objects of the 'Pokemon' class.
# Arguments used at instantiation are sent to the '__init__' method.
pokemon1 = Pokemon("cyndaquil", "fire", 55, 8, 2, [PokemonMoveTackle])
pokemon2 = Pokemon("squirtle", "water", 68, 6, 4, [PokemonMoveTackle])

# Now, we can have the monsters attack each other w/ the 'use_on' method
# of any instantiated move, such as this tackle. :D
pokemon1.move_dict["tackle"].use_on(pokemon2)

# To break down what this line of code is doing, we need to understand
# attributes, methods, and dictionary keys.

# In Python (and most other programming languages), '.' is used to
# represent ownership, similar to "'s" (apostrophe, S) in English.
# Instead of "Vencabot's stream," you would say, "vencabot.stream".

# Also, to get data out of a 'dict', you supply its 'key' (the data
# chosen to REFER to the data you want) between square brackets ([ ]).

# For the moves in move_dict, we dediced to use the a string containing
# that move's name as our keys. So, "tackle" refers to a tackle move in
# move_dict.

# To break down the line of code above: "Pass pokemon2 as an argument to
# the 'use_on' method belong to whatever move is called 'tackle' in
# pokemon1's move_dict ."
