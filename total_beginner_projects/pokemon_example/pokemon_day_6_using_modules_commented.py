#########################################################################
# pokemon_day_6_using_modules_commented.py                              #
#     - developed at twitch.tv/vencabot , Intro to Python 11/23/18      #
#     - watch the archived stream at ___________________________        #
#                                                                       #
# This is the final on-stream lesson that's utilizing this ongoing      #
# Pokemon example. We began with the most basic of programming concepts #
# for total non-programmers, and now we've graduated to some more       #
# advanced concepts, including classes, object-oriented programming,    #
# and, now, using modules to help keep a project organized.             #
#                                                                       #
# In this episode, we generally make enhancements and improvements to   #
# the existing 'game', making it much more interesting to play! Mostly, #
# we utilize concepts that we've already looked at in previous lessons, #
# but the most important concept introduced here is that of 'modules'   #
# or 'packages'. In this simple example, all we end up doing is         #
# splitting our program across three different Python files (modules)   #
# that are all stored in the same directory (folder) on our PC. This    #
# allows us to simply import those files using the 'import' command     #
# using their filenames (minus the '.py' extension).                    #
#                                                                       #
# As for general improvements made to the game, we've added quite a few #
# new Pokemon moves and several new types of Pokemon as well. At the    #
# very end of our lesson, we turned our battle system from a simple     #
# one-off encounter into a series of encounters, where each victory     #
# yields experience points that can level up our Pokemon and improve    #
# its attributes. Although this is a huge improvement to our game, it's #
# surprisingly simple to implement using very basic concepts that we've #
# already learned.                                                      #
#                                                                       #
#########################################################################

# The standard library 'random' has lots of tools for randomization.
# We use it for enemy AI and to randomize the order of opponents.
import random

# We've defined these two other documents and are importing their stuff.
# 'pokemon_moves_commented' contains all of our 'PokemonMove' classes.
# 'pokedex_commented' contains all of our 'Pokemon' classes.
# Because we've spun them off into their own modules, we don't need to
# clutter up this script with a ton of class definitions. It just focuses
# on gameplay.
# We could've used 'from MODULE_NAME import *' so that we could use
# 'Cyndaquil("Dixxucker")' instead of 'pokedex.Cyndaquil("Dixxucker")',
# but leaving the namespaces makes it extra clear where our tools are
# coming from.
# In this example, we're using 'import MODULE_NAME as ALIAS' so that we
# don't need to keep typing the 'commented' suffix, though.
import pokemon_moves_commented as pokemon_moves
import pokedex_commented as pokedex

# In order for us to have a repeating series of battles (rather than just
# a single battle, like the old code), the game's core combat loop of
# turn-taking would need to be indented VERY deeply, since we have loops
# within loops.
# By putting the turn-taking into its own function, we can minimize how
# much indenting we need to do, and how much re-indenting we need to do
# in the case that we want to change the way that our program works,
# later.
# In other words, as we explained long ago, there are two reasons to
# define a function:
#     1.) to minimize the repetitiveness of code by writing it once and
#         then just calling the function whenever necessary.
#     2.) to make code easier to read or manage by hiding complexity
#         behind simple function names and moving it away from where
#         it'll be used.
# In this case, we're using the latter reason. By putting our battle code
# into a function, we drastically reduce how much the lines need to be
# indented, which makes it much easier to read. Also, it moves the
# complexity of battle away from where the battle actually happens, where
# there is already plenty of other complexity.
# 'combatant_a' is a Pokemon instance representing OUR Pokemon.
# 'combatant_b' is a Pokemon instance representing the AI opponent.
def battle_turns(combatant_a, combatant_b):

    # For player readability, show blank line before our Pokemon's turn.
    print()

    # Print a list of our Pokemon's moves for the player to choose from.
    print(
            combatant_a.nickname + " the " + combatant_a.monster_type
            + "'s moves:")
    # For every move in our Pokemon's move_dict, print its name.
    for move_instance in combatant_a.move_dict.values():
        print("    " + move_instance.move_name)

    # For player readability, show blank line before prompting for input.
    print()
    user_input = input(
            "What move should " + combatant_a.nickname + " use? ")

    # If possible, use the move that the player asked for.
    try:
        combatant_a.use(user_input, combatant_b)

    # If the move name isn't a key in our Pokemon's move_dict, Python
    # raises a KeyError.
    except KeyError:
        print(combatant_a.nickname + " doesn't know " + user_input + "!")
        # 'return' will immediately end a function. Since this function
        # is later used in a 'while' loop, the loop will return to the
        # top and this function will be called again, prompting the user
        # for a move-name once more.
        return

    # If the move requested has no remaining PP, Pokemon.use() will raise
    # our custom-made Exception, 'PPError'.
    except pokemon_moves.PPError:
        print(user_input + " has no remaining PP!")
        return

    # For player readability, show blank line before the opponent's turn.
    print()

    # If the opponent is still alive after our turn, they get a turn.
    if combatant_b.hp > 0:

        # Create a list of moves that are actually USABLE by opponent.
        # Then, go through each move that it has and verify that it's
        # usable. If it is, it gets added to the list. If it's not usable
        # for any reason, it doesn't get added to the list.
        available_moves = []
        for move_instance in combatant_b.move_dict.values():

            # A Pokemon named 'Dixxucker' will never comb its hair.
            # Therefore, if this move is 'comb hair' and this Pokemon's
            # name is 'Dixxucker', 'comb hair' doesn't get added to the
            # list of available moves.
            if (
                    combatant_b.nickname == "Dixxucker"
                    and move_instance.move_name == "comb hair"):
                continue

            # Only moves with remaining PP are available to be used.
            # If the move has PP, add it to the list. If not, don't.
            if move_instance.current_pp > 0:
                available_moves.append(move_instance)

        # If, after all moves have been evaluated for usability, the
        # Pokemon has no available moves, there's nothing they can do!
        # End its turn!
        if len(available_moves) == 0:
            print(
                    combatant_b.nickname + " the "
                    + combatant_b.monster_type
                    + " has no available moves!")
            return

        # If we made it this far, the opponent has some available moves.
        # Use one, at random, on our Pokemon!
        random_move = random.choice(available_moves)
        random_move.use_on(combatant_a)


# Instantiate a bunch of Pokemon to use in our battles.
pokemon1 = pokedex.Cyndaquil("Zanzhu")
pokemon2 = pokedex.Cyndaquil("Dixxucker")
pokemon3 = pokedex.Ganja("Locust")
pokemon4 = pokedex.Geodude("Arksam")

# 'combatant_a' is the Pokemon that we're controlling. Choose from above.
combatant_a = pokemon4

# All of the other Pokemon are our opponents. Put them in a list and then
# shuffle the order that they'll appear in.
opponents = [pokemon1, pokemon2, pokemon3]
random.shuffle(opponents)

# Fight all of our opponents in order!
for combatant_b in opponents:
    # For player readability, print a blank line before each opponent.
    print()

    # Let the player know that a new battle is beginning.
    print(
            combatant_b.nickname + " the " + combatant_b.monster_type
            + " appears!")
    print("It looks pissed off!")

    # As long as both Pokemon are standing, keep taking turns.
    while combatant_a.hp > 0 and combatant_b.hp > 0:
        battle_turns(combatant_a, combatant_b)

    # The 'while' loop above has ended, so this battle is over.
    # Figure out who the winner and loser are and tell the player.
    winner = combatant_a if combatant_a.hp > 0 else combatant_b
    loser = combatant_b if winner is combatant_a else combatant_a
    print(
            loser.nickname + " the " + loser.monster_type
            + " has fainted!")
    print(
            winner.nickname + " the " + winner.monster_type
            + " is the winner!")

    # Give the winning Pokemon 30 EXP and level them up if necessary.
    # When leveling up, Pokemon have their base stats added to their
    # current stats. Then, their next level-up is pushed 50 EXP away from
    # where it was last time.
    print(winner.nickname + " earned 30 experience!")
    winner.experience = winner.experience + 30
    if winner.experience >= winner.exp_required_for_level:
        print(winner.nickname + " leveled up!")
        winner.level = winner.level + 1
        winner.hp = winner.hp + winner.base_hp
        winner.attack = winner.attack + winner.base_attack
        winner.defense = winner.defense + winner.base_defense
        winner.exp_required_for_level = (
                winner.exp_required_for_level + 50)

    # If our Pokemon is the one that fainted, don't bother fighting the
    # rest of our opponents. Break out of the loop and end the program!
    if loser is combatant_a:
        print("Game Over!")
        break
