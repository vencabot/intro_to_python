#########################################################################
# pokemon_day_2_no_classes_commented.py                                 #
#     - developed at twitch.tv/vencabot , Intro to Python 10/19/18      #
#     - watch the archived stream at youtube.com/watch?v=js3y5mlTqdQ    #
#                                                                       #
# This is the second day (and second form) of our 'pokemon' project,    #
# where we're learning the very basics of programming by creating a     #
# Pokemon-like RPG.                                                     #
#                                                                       #
# In the last version, which can be found at 'pokemon_day_1.py', we     #
# explored the basics of assignment, logic, and code-blocks.            #
#                                                                       #
# In this version, we're using the 'def' statement to create our own    #
# 'function', which takes 3 'arguments' (as seen below) and 'return's a #
# value based on those arguments. This saves us a few lines of code,    #
# although the true strength of function definitions will become more   #
# clear, in the context of this project, once we explore 'classes' in   #
# our next lesson.                                                      #
#                                                                       #
# Previously, our opponent Pokemon was actually a 'pokebot', which was  #
# distinct from our 'pokemon' because it only had one attack, which     #
# consumed no PP. Here, we're introducing a new data type, 'list', and  #
# a new function, 'random.randint', to give our opponent 4 attacks      #
# which all consume PP -- just like us -- and the ability to randomly   #
# choose from those attacks, making combat much more dynamic.           #
#                                                                       #
# In order to use 'random.randint', we have to import our first         #
# library. Think of libraries like large collections of themed tools    #
# that we can use in our code, but we don't have access to them by      #
# default. Instead, we have to choose which tools we want access to and #
# bring them into our code via the 'import' statement.                  #
#                                                                       #
# Although we changed relatively little about our code, th game just    #
# became much more fun!                                                 #
#                                                                       #
#########################################################################

# Import a library so our opponent choose attacks at random.
import random

# Define a function which fulfills a task that we repeatedly do.
def deal_damage(opponent_name, opponent_hp, actual_damage):
    # If an attack does negative damage, it heals the opponent.
    # Make sure that doesn't happen by bottoming out at '0' damage.
    if actual_damage < 0:
        actual_damage = 0

    # Calculate the opponent's new HP value after the attack lands.
    opponent_hp = opponent_hp - actual_damage

    # Display some useful information for the player.
    print(opponent_name + " took " + str(actual_damage) + " damage!")
    print(opponent_name + " now has " + str(opponent_hp) + " HP.")

    # Since the opponent's HP changed, make sure to report the new value.
    return opponent_hp

# Define OUR Pokemon's attributes.
pokemon1_name = "cyndadixx"
pokemon1_type = "fire"
pokemon1_hp = 55
pokemon1_atk = 8
pokemon1_def = 2
pokemon1_move1_pp = 10
pokemon1_move2_pp = 5
pokemon1_move3_pp = 12
pokemon1_move4_pp = 8
# As of right now, we have no internal use for OUR Pokemon's movelist.
pokemon1_move_list = ["tackle", "flamethrower", "tail whip", "growl"]

# Define the OPPONENT Pokemon's attributes.
pokemon2_name = "squirtle"
pokemon2_type = "water"
pokemon2_hp = 68
pokemon2_atk = 6
pokemon2_def = 4
pokemon2_move1_pp = 10
pokemon2_move2_pp = 6
pokemon2_move3_pp = 12
pokemon2_move4_pp = 666
# This list of 'str's is chosen from at random on the opponent's turn.
pokemon2_move_list = [
        "tackle", "bubble", "tail whip", "tatsumakisenpuuken"]

# Display both movelists so the player knows what to do.
print(pokemon1_name + "'s available moves are:")
print("    tackle")
print("    flamethrower")
print("    tail whip")
print("    growl")
print()
print(pokemon2_name + "'s available moves are:")
print("    tackle")
print("    bubble")
print("    tail whip")
print("    tatsumakisenpuuken")

# As long as both Pokemon are standing, continue taking turns!
while pokemon1_hp > 0 and pokemon2_hp > 0:
    # Print a blank line to separate each turn, visually, for the player.
    print()

    # Ask the player what move to use and save their response as a 'str'.
    inputted_text = input("What move should " + pokemon1_name + " use? ")

    # Compare the user's command to our known moves and act accordingly.
    if inputted_text == "tackle":
        # A simple move, dealing damage that can be absorbed by defense.
        
        # If a move is out of PP, it can't be used.
        if pokemon1_move1_pp == 0:
            print("'tackle' has no remaining PP!")
            # Go back to the top of the 'while' loop to re-ask for input.
            continue

        # Display the attack for the player
        print(pokemon1_name + " tackled " + pokemon2_name + "!")

        # Calculate damage dealth based on character stats.
        actual_damage = pokemon1_atk - pokemon2_def

        # Get the opponent's new HP using our 'deal_damage' function.
        pokemon2_hp = deal_damage(
                pokemon2_name, pokemon2_hp, actual_damage)

        # Reduce move's PP, since it was used, and display remaining.
        pokemon1_move1_pp = pokemon1_move1_pp - 1
        print(
                "'tackle' has " + str(pokemon1_move1_pp)
                + " PP remaining.")
        
    elif inputted_text == "flamethrower":
        # An elemental move that deals extra damage to 'grass' types.
        
        if pokemon1_move2_pp == 0:
            print("'flamethrower' has no remaining PP!")
            continue
        
        print(pokemon1_name + " blew flames at " + pokemon2_name + "!")
        
        if pokemon2_type == "grass":
            print("It's super effective!")
            actual_damage = (pokemon1_atk * 2) - pokemon2_def
        else:
            actual_damage = pokemon1_atk - pokemon2_def
            
        pokemon2_hp = deal_damage(
                pokemon2_name, pokemon2_hp, actual_damage)
        pokemon1_move2_pp = pokemon1_move2_pp - 1
        print(
                "'flamethrower' has " + str(pokemon1_move2_pp)
                + " PP remaining.")
        
    elif inputted_text == "tail whip":
        # A move that weakens the opponent's defense.
        
        if pokemon1_move3_pp == 0:
            print("'tail whip' has no remaining PP!")
            continue
        
        print(
                pokemon1_name + " whipped its tail at " + pokemon2_name
                + "!")

        # Reduce the opponent's defense, but don't go into negatives.
        pokemon2_def = pokemon2_def - 1
        if pokemon2_def < 0:
            pokemon2_def = 0
            
        pokemon1_move3_pp = pokemon1_move3_pp - 1
        print(
                "'tail whip' has " + str(pokemon1_move3_pp)
                + " PP remaining.")

    elif inputted_text == "growl":
        # A move that lowers the opponent's offensive power.
        
        if pokemon1_move4_pp == 0:
            print("'growl' has no remaining PP!")
            continue
        
        print(pokemon1_name + " growled at " + pokemon2_name + "!")

        # Reduce the opponent's 'atk' value, but don't go into negatives.
        pokemon2_atk = pokemon2_atk - 1
        if pokemon2_atk < 0:
            pokemon2_atk = 0
            
        pokemon1_move4_pp = pokemon1_move4_pp - 1
        print("'growl' has " + str(pokemon1_move4_pp) + " PP remaining.")
        
    else:
        # If none of the 'if' statements above were triggered, this runs.
        print(pokemon1_name + " doesn't know that move!")

        # The player typed an unknown move, so start over and ask again.
        continue

    # Print a line to separate our Pokemon's turn from the opponent's.
    print()

    # If the opponent is still standing after our turn, they get a turn.
    if pokemon2_hp > 0:
        # Choose a random integer between '0' and '3'.
        pokemon2_random_index = random.randint(0, 3)

        # Use the random 'int' as an index to get a move from the 'list'.
        inputted_text = pokemon2_move_list[pokemon2_random_index]

        # Treat the randomly selected 'str' like our inputted text.
        if inputted_text == "tackle":

            # When the opponent is out of 'PP', a bug occurs. Oops!
            if pokemon2_move1_pp == 0:
                print("'tackle' has no remaining PP!")

                # This returns to the top of the loop, which is OUR turn!
                # Randomly-chosen move is empty? Foe's turn is skipped.
                # We'll have to address this bug, later!
                continue
            
            print(pokemon2_name + " tackled " + pokemon1_name + "!")
            actual_damage = pokemon2_atk - pokemon1_def
            pokemon1_hp = deal_damage(pokemon1_name, pokemon1_hp, actual_damage)
            pokemon2_move1_pp = pokemon2_move1_pp - 1
            print("'tackle' has " + str(pokemon2_move1_pp) + " PP remaining.")

        elif inputted_text == "bubble":
            # An elemental move good against fire but bad against grass.

            if pokemon2_move2_pp == 0:
                print("'bubble' has no remaining PP!")
                continue

            print(pokemon2_name + " blew oily bubbles at " + pokemon1_name + "!")

            if pokemon1_type == "fire":
                print("It's super effective!")
                actual_damage = (pokemon2_atk * 2) - pokemon1_def
            elif pokemon2_type == "grass":
                print("It's not very effective...")
                actual_damage = (pokemon2_atk / 2) - pokemon1_def
            else:
                # If opponent isn't 'fire' or 'grass', do normal damage.
                actual_damage = pokemon2_atk - pokemon1_def

            pokemon1_hp = deal_damage(pokemon1_name, pokemon1_hp, actual_damage)
            pokemon2_move2_pp = pokemon2_move2_pp - 1
            print("'bubble' has " + str(pokemon2_move2_pp) + " PP remaining.")

        elif inputted_text == "tail whip":
            if pokemon2_move3_pp == 0:
                print("'tail whip' has no remaining PP!")
                continue
            
            print(pokemon2_name + " whipped its tail at " + pokemon1_name + "!")

            pokemon1_def = pokemon1_def - 1
            if pokemon1_def < 0:
                pokemon1_def = 0

            pokemon2_move3_pp = pokemon2_move3_pp - 1
            print("'tail whip' has " + str(pokemon2_move3_pp) + " PP remaining.")

        elif inputted_text == "tatsumakisenpuuken":
            # Ken's special attack. Always does big damage!
            
            if pokemon2_move4_pp == 0:
                print("'tatsukamisenpuuken' has no remaining PP!")
                continue

            print(pokemon2_name + " executed a whirling kick at " + pokemon1_name + "!")

            actual_damage = (pokemon2_atk * 2) - pokemon1_def

            pokemon1_hp = deal_damage(pokemon1_name, pokemon1_hp, actual_damage)
            pokemon2_move4_pp = pokemon2_move4_pp - 1
            print("'tatsumakisenpuuken' has " + str(pokemon2_move4_pp) + " PP remaining.")

        else:
            # This will never run, since a move is chosen automatically.
            print(pokemon2_name + " doesn't know that move!")
            continue

# The combat loop is over, so someone fainted. Who won?
if pokemon2_hp <= 0:
    # Opponent has fainted. We win!
    print(pokemon2_name + " has fainted! " + pokemon1_name + " wins!")
else:
    # Our Pokemon fainted. We lose! T_T
    print(pokemon1_name + " has fainted! " + pokemon2_name + " wins!")
    
print()
print("Game Over")
