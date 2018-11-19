#########################################################################
# pokemon_day_5_try_exceptions_commented.py                             #
#     - developed at twitch.tv/vencabot , Intro to Python 11/16/18      #
#     - watch the archived stream at youtube.com/watch?v=rJuaza3ssKg    #
#                                                                       #
# We're continuing development of our Pokemon battle example as a way   #
# to learn the very basics of programming.                              #
#                                                                       #
# In this episode, we finally have a working Pokemon battle again! If   #
# you look at the 'while' loop near the bottom of the program, you'll   #
# see that, in some ways, it resembles our 'combat' loop from day_2,    #
# but it's been dramatically shortened by using our new knowledge of    #
# classes, lists, and dictionaries.                                     #
#                                                                       #
# Furthermore, the enemy's AI is much improved: it won't try to use     #
# moves that are empty of PP, and it won't try to use 'comb hair' if    #
# its name is 'Dixxucker,' since Dixx never comes his hair.             #
#                                                                       #
# We reviewed class inheritance, which we talked about in the last      #
# episode, but, much more interestingly, we introduced the idea of      #
# 'Exceptions' and how to deal with them and even use them to our       #
# advantage.                                                            #
#                                                                       #
# An 'Exception' is an error, and it occurs whenever you try to do      #
# something that you're not allowed to do. Whenever an Exception is     #
# 'raised' (occurs), Python will crash (and give you details about the  #
# Exception) unless you explicitly prepare for and deal with the        #
# Exception by using the 'try' and 'except' statements, which we        #
# introduce in this episode.                                            #
#                                                                       #
# Basically, you can put your code within a 'try' block, and then, if   #
# that code raises an Exception, it'll trigger the following 'except'   #
# code block instead of simply crashing Python. By default, 'except'    #
# blocks will be triggered on ANY Exception, but you can also give the  #
# 'except' statement a certain type of Exception to look for in         #
# particular, such as 'except KeyError:'.                               #
#                                                                       #
# In our code, we even define our OWN type of Exception, 'PPError', by  #
# inheriting from 'Exception'; in fact, we don't even override any of   #
# 'Exception's methods or attributes. All we need 'PPError' for is to   #
# have an Exception that we can manually raise, using the 'raise'       #
# statement, which has a customized name that we can specifically       #
# except (or "catch").                                                  #
#                                                                       #
# This way, when the player chooses to use a particular move, we can    #
# attempt to use it. If they entered a move name that isn't a key that  #
# exists within pokemon1.move_dict, we can except KeyError and tell the #
# user that they entered an incorrect move name. If they try to use a   #
# move which is out of PP, 'PPError' gets raised, and so we can except  #
# PPError and tell the user that the move is out of PP. Cool!           #
#                                                                       #
# At the time of uploading this to github, I also made some changes to  #
# the code that you won't see in the actual episode. At the request of  #
# our friend 'carbonoid,' I fixed a bug that would cause the battle to  #
# crash with 'PPError' if the opponent AI tried to use a move that was  #
# empty of PP. Now, before it picks a move at random, the AI uses a     #
# 'for' loop to create a list of available moves, which must all have   #
# PP.                                                                   #
#                                                                       #
# Secondly, to save 4 lines of code, I replaced the final 'winner,      #
# loser' if-statements with our first-ever use of an 'inline            #
# conditional'. Basically, you can evaluate a conditional statement     #
# during variable assignment to choose a value to assign. The syntax    #
# looks like:                                                           #
#                                                                       #
# variable_name = possible_value1 if CONDITION else possible_value 2    #
#                                                                       #
# We're nearing the end of our work on this example! I hope that you've #
# been learning a lot! :D                                               #
#                                                                       #
#########################################################################

# Import a library (a collection of tools) to add randomness to our AI.
import random

# By extending (inheriting from) 'Exception', we can 'raise' our own
# errors for various situations.
# Here, we're creating an error to raise when we try to use a move that
# has no PP remaining.
class PPError(Exception):
    pass


# This hasn't changed since our last episode. It's a class that contains
# all of the attributes and methods that a Pokemon move will need, so
# that we can easily create new moves by inheriting from (or 'extending')
# this generic class.
class PokemonMove:
    # '__init__' always gets called when a new object is 'instantiated'
    # from this class. A class is just a mold; the 'instance' is what
    # gets made from a class.
    def __init__(self, owner, move_name, max_pp, elemental_type):
        # 'owner' is the 'Pokemon' object that's gonna use this move.
        self.owner = owner
        # 'move_name' is a string used as a key in owner.move_dict .
        self.move_name = move_name
        # 'max_pp' is how much ammo the move starts with.
        self.max_pp = max_pp
        # 'current_pp' is how much ammo the move has. It starts at max.
        self.current_pp = max_pp
        # 'elemental_type' may help calculate damage. Pokemon stuff.
        self.elemental_type = elemental_type

    # This simple method just prints out a customized message to tell the
    # player that the move got used.
    def print_startup(self, target):
        print(
                self.owner.nickname + " the " + self.owner.monster_type
                + " used '" + self.move_name + "' on "
                + target.nickname + " the " + target.monster_type + "!")

    # This method is meant to be overridden by classes that inherit from
    # 'PokemonMove', and it defines what happens when the move is used on
    # a target. By default, it just prints the startup message.
    def use_on(self, target):
        self.print_startup(target)


# This is a simple move that deals straight-forward damage.
class Tackle(PokemonMove):
    def __init__(self, owner):
        # By using 'super(),' we can use the parent class's methods.
        # This is important when we're 'overriding' our parent's methods
        # by creating new methods with those same names.
        # For instance, the method we're currently in is 'self.__init__',
        # so how do we use our parent's '__init__' method? If we hadn't
        # overridden it, 'self' would just inherit the parent's __init__,
        # but since we ARE overriding it, we can access the parent's
        # __init__ method by using 'super()'.
        # In this case, 'Tackle's __init__ is simply a method that
        # supplies special arguments to PokemonMove.__init__.
        super().__init__(owner, "tackle", 10, "normal")

    def use_on(self, target):
        # If we try to use a move that has no PP, our custom 'PPError'
        # Exception gets raised. If we don't deal with this error using
        # 'try' and 'except,' our program will crash. :O
        if self.current_pp == 0:
            raise PPError

        # If we made it this far, the move has PP remaining. Use it.
        # Print a message to let the player know what's going on.
        print(
                self.owner.nickname + " the " + self.owner.monster_type
                + " tackled " + target.nickname + " the "
                + target.monster_type + "!")

        # Calculate the tackle's damage using attributes of both Pokemon.
        actual_damage = self.owner.attack - target.defense

        # If the damage is negative, the opponent will be healed. Prevent
        # this bug from happening.
        if actual_damage < 0:
            actual_damage = 0

        # Reduce the opponent's HP by how much damage we're doing.
        target.hp = target.hp - actual_damage

        # Show the player how much damage was done / HP remaining.
        print(
                target.nickname + " the " + target.monster_type
                + " took " + str(actual_damage) + " damage!")
        print(
                target.nickname + " the " + target.monster_type + " has " + str(target.hp)
                + " HP remaining.")

        # Consume PP and report how much PP is left to the player.
        self.current_pp = self.current_pp - 1
        print("'tackle' has " + str(self.current_pp) + " PP remaining.")


# This simple move was just created so that we'd have more than one move.
class CombHair(PokemonMove):
    def __init__(self, owner):
        # Like Tackle, CombHair.__init__ just feeds arguments to
        # PokemonMove.__init__ .
        super().__init__(owner, "comb hair", 1, "normal")

    # This move doesn't do damage or anything. It just prints a message
    # and consumes PP.
    def use_on(self, target):
        if self.current_pp == 0:
            raise PPError
        print(
                self.owner.nickname + " the " + self.owner.monster_type
                + " combs its hair.")
        self.current_pp = self.current_pp - 1


# This generic class is meant to be inherited from by other, more
# specialized Pokemon classes. It has all of the attributes that a
# Pokemon needs, as well as a method that all Pokemon require, which
# allows them to use their moves by name without having to directly
# access the Pokemon's move_dict and call the move's 'use_on' method.
class Pokemon:
    def __init__(
            self, nickname, monster_type, elemental_type, hp, attack,
            defense, move_class_list):
        # The name given to the individual Pokemon, like 'Steve'.
        self.nickname = nickname
        # The monster's species, such as 'bulbasaur'.
        self.monster_type = monster_type
        # The element defines how much damage attacks do. Pokemon stuff.
        self.elemental_type = elemental_type
        # How much 'health' a Pokemon currently has. At 0, it faints.
        self.hp = hp
        # The base attack damage of simple moves like 'Tackle'.
        self.attack = attack
        # How much damage is subtracted when this Pokemon is attacked.
        self.defense = defense

        # 'move_dict' is a dictionary where move instances are accessed
        # by their 'move_name' attributes. So, to get an instance of
        # 'CombHair' out of move_dict, you use the key "comb hair".
        # These four lines populate move_dict using the list of
        # PokemonMove classes that were supplied as __init__'s final
        # argument. Each class is instantiated and then added to the
        # dictionary using its 'move_name' attribute for the key.
        self.move_dict = {}
        for pokemon_move_class in move_class_list:
            new_move = pokemon_move_class(self)
            self.move_dict[new_move.move_name] = new_move

    # This simple method is just meant to simplify the process of using
    # moves. Before, you always had to use:
    #
    # pokemon_instance.move_dict[move_name].use_on(target)
    #
    # That's kind of a mouthful! With this method, you can now just:
    #
    # pokemon_instance.use(move_name, target)
    def use(self, move_name, target):
        self.move_dict[move_name].use_on(target)


# The following classes inherit from 'Pokemon' and simply call its
# '__init__' method with arguments customized to each species of Pokemon.
# For now, both Cyndaquil and Machamp have the same moves, and Machamp
# isn't even used.
# You still need to supply a 'nickname' when instantiating these classes,
# though.
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


# Define a couple of cyndaquils with different nicknames.
pokemon1 = Cyndaquil("Zanzhu")
pokemon2 = Cyndaquil("Dixxucker")

# This is where the Pokemon battle starts.
# Continue taking turns for as long as both Pokemon have HP remaining.
while pokemon1.hp > 0 and pokemon2.hp > 0:
    # This is our Pokemon's turn. Print a blank line for readability.
    print()

    # Prompt the user to enter a string, which is saved to a variable.
    user_input = input(
            "What move should " + pokemon1.nickname + " the "
            + pokemon1.monster_type + " use? ")

    # Code that's contained in a 'try' block won't cause the program to
    # crash as long as its Exception is handled / caught / excepted by an
    # appropriate 'except' statement, below.
    # Here, we try to use a move based on the move name that the user
    # inputted.
    try:
        pokemon1.use(user_input, pokemon2)

    except KeyError:
        # Oh shit! The user inputted a string that isn't a key in
        # pokemon1.move_dict, which means that it's either a typo or a
        # move that our Pokemon doesn't know.
        # Thankfully, since we caught the resulting KeyError exception,
        # our program didn't crash. In fact, we can even use this error
        # to show our player a custom message and use the 'continue'
        # statement to restart the combat loop, asking them for another
        # move name.
        print(pokemon1.nickname + " doesn't know " + user_input + "!")
        continue

    except PPError:
        # Oh shit! During the move's 'use_on' method, a PPError was
        # raised. We actually created that Exception type and
        # specifically coded our 'use_on' methods to 'raise' it when the
        # move's PP is empty. Since we know the move is out of PP, we can
        # print off a message for the user and then restart the combat
        # loop, asking them for another move name.
        print(user_input + " has no remaining PP!")
        continue
    
    # Opponent Pokemon's turn. Print a blank line for readability.
    print()

    # The opponent only gets a turn if it's still alive after our turn.
    if pokemon2.hp > 0:
        
        # The enemy Pokemon has a list of moves, and it's going to choose
        # one at random. However, there are some moves that it just can't
        # use, so they shouldn't be included in the pool of moves that
        # it'll randomly pick from.
        # First, create an empty list representing the list of moves the
        # AI can use.
        available_moves = []

        # Now, we're going to use 'for' to go through every move that the
        # Pokemon knows and, if it's usable, append it to the list of
        # moves that it can randomly choose from.
        for move_instance in pokemon2.move_dict.values():

            # Dixxucker NEVER combs his hair. Don't even bother adding
            # 'comb hair' to the pool of available moves. We use
            # 'continue' to move to the next cycle of the loop, just like
            # with 'while'. In a 'for' loop, this means moving on to the
            # next item in the list we're going through.
            if (
                    pokemon2.nickname == "Dixxucker"
                    and move_instance.move_name == "comb hair"):
                continue

            # If we made it this far, the Pokemon's nickname isn't and/or
            # the move that we're examining isn't 'comb hair'.
            # Whatever move we're looking at, then, is safe to use as
            # long as it has PP.
            if move_instance.current_pp > 0:
                available_moves.append(move_instance)

        # We've populated our list of available moves. If the length of
        # the list is '0', though, then there's no moves we can use!
        # Print a message off and then 'continue' to our opponent's turn.
        if len(available_moves) == 0:
            print(
                    pokemon2.nickname + " the " + pokemon2.monster_type
                    + " has no available moves!")
            continue

        # If we made it this far, then there's at least one move to
        # choose from in our available_moves list. Use a method from the
        # 'random' library to choose an item from the list at random.
        random_move = random.choice(available_moves)
        random_move.use_on(pokemon1)

# If we're down here, that means that the 'while' loop ended, so somebody
# fainted. Let's figure out who the winners and losers are!
#
# This is our first-ever 'inline conditional' statement. It's just some
# syntactic sugar that we can use in Python to save some lines.
# We could have written the first statement as:
#
# if pokemon1.hp > 0:
#     winner = pokemon1
# else:
#     winner = pokemon2
#
# We can save a lot of lines by just using an inline conditional to say,
# "The winner is pokemon1 if it still has HP. Otherwise, it's pokemon2.
winner = pokemon1 if pokemon1.hp > 0 else pokemon2

# Then we use another inline-conditional to say, "The loser is pokemon2
# if pokemon1 is the winner. Otherwise, it's pokemon1."
loser = pokemon2 if winner is pokemon1 else pokemon1

# Print off a little game-over message, and we're done!
print(loser.nickname + " the " + loser.monster_type + " has fainted!")
print(
        winner.nickname + " the " + winner.monster_type
        + " is the winner!")
