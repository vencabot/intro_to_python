#########################################################################
# pokemon_day_1_no_def_or_classes_commentated.py                        #
#     - developed at twitch.tv/vencabot , Intro to Python 10/12/18      #
#     - watch the archived stream at ___________________________        #
#                                                                       #
# This simple game is an exercise meant to strengthen our understanding #
# of the VERY BASICS of programming, including:                         #
#                                                                       #
#     * The assignment of variable names to integers & strings (text).  #
#                                                                       #
#     * The usage of variables and 'literals' in arithmetic operations. #
#                                                                       #
#     * Usage of the 'print' function to show information to the user.  #
#                                                                       #
#     * Usage of the 'input' function to get a string from the user.    #
#                                                                       #
#     * Usage of the 'str' function to get the string form of an int.   #
#                                                                       #
#     * Controlling program 'flow' with indented logic blocks, such as: #
#         + 'if' blocks only run if their condition evaluates True.     #
#         + 'else' blocks run if their partnered 'if' evaluated False.  #
#         + 'elif' is an 'else' directely followed by another 'if'.     #
#         + 'while' loops when, by its end, its condition remains True. #
#             - 'continue' immediately jumps to the top of the loop.    #
#             - 'break' immediately drops out of the loop.              #
#                                                                       #
# In the future, we'll improve this game with some slightly more        #
# advanced tools, such as by defining our own functions, taking better  #
# advantage of Python's built-in functions, and implementing 'classes'  #
# to better-organize our data and operations. Even with our limited,    #
# beginner-oriented toolset, however, we can already do some very       #
# interesting stuff!                                                    #
#                                                                       #
# Our goal for today is to have our pokemon, with 4 moves, fight        #
# against a 'pokebot,' which only has one attack that it uses           #
# repeatedly.                                                           #
#                                                                       #
# Our Pokemon and the pokebot need attributes such as HP, ATK, DEF.     #
# Our Pokemon's moves all require PP.                                   #
#                                                                       #
# The game will take place over a number of turns until either our      #
# pokemon or the enemy pokebot faint from loss of HP.                   #
#                                                                       #
#########################################################################

# Our pokemon's name will be 'print'ed in messages to the player.
pokemon_name = "cyndaquil"

# Moves may be more or less effective depending on elemental type.
pokemon_type = "fire"

# Once a pokemon's 'hp' (health points) hits 0 or below, they faint.
pokemon_hp = 55

# Moves will use 'atk' to determine how much 'hp' damage to deal.
pokemon_atk = 8

# For now, 'def' simply represents exactly how much damage is absorbed.
pokemon_def = 2

# Each of a pokemon's four moves can be used 'pp' number of times.
pokemon_move1_pp = 10
pokemon_move2_pp = 5
pokemon_move3_pp = 12
pokemon_move4_pp = 8

# The 'pokebot' has the same stats as our pokemon, but only one move.
pokebot_name = "pokebot bulbasaur"
pokebot_type = "grass"
pokebot_hp = 68
pokebot_atk = 6
pokebot_def = 4

# Tell the player what moves their pokemon has access to.
print(pokemon_name + "'s available moves are:")
print("    tackle")
print("    flamethrower")
print("    tail whip")
print("    growl")

# This turn-based combat loop repeats until someone faints.
while pokemon_hp > 0 and pokebot_hp > 0:
    # Every turn starts with a blank line, to make combat easier to read.
    print()

    # Our Pokemon gets the first turn. Ask the player what move to use.
    inputted_text = input("What move should " + pokemon_name + " use? ")

    # Compare the string (text) we got from the player to known moves.
    if inputted_text == "tackle":
        # If this code is running, the player entered 'tackle'.
        if pokemon_move1_pp == 0:
            # Tackle has no PP left? Print a message...
            print("'tackle' has no remaining PP!")
            
            # ...and immediately 'continue' back to the top of the loop,
            # where the player is asked to enter a move name, skipping
            # the rest of the code, below.
            continue

        # If we got this far, we must have PP remaining. Show a message!
        print(pokemon_name + " tackled " + pokebot_name + "!")

        # Calculate the attack's damage, factoring in the foe's 'def'.
        actual_damage = pokemon_atk - pokebot_def

        # If the foe has more 'def' than we deal damage, 'actual_damage'
        # is a negative number. This results in the foe being HEALED.
        # Here, we make sure that, if 'actual_damage' is negative, it's
        # raised to be no less than '0'.
        if actual_damage < 0:
            actual_damage = 0

        # Actually reduce the foe's HP. Now pokebot has taken damage!
        pokebot_hp = pokebot_hp - actual_damage

        # A pokemon's moves have limited uses. Reduce move's PP by 1.
        pokemon_move1_pp = pokemon_move1_pp - 1

        # Display some useful information to the player.
        print(pokebot_name + " took " + str(actual_damage) + " damage!")
        print(pokebot_name + " now has " + str(pokebot_hp) + " HP.")
        print("'tackle' has " + str(pokemon_move1_pp) + " PP remaining.")

    # Because we're using 'elif,' we only continue testing the player's
    # entered text if we haven't already figured out what move they want.
    elif inputted_text == "flamethrower":
        if pokemon_move2_pp == 0:
            print("'flamethrower' has no remaining PP!")
            continue
        
        print(pokemon_name + " blew flames at " + pokebot_name + "!")

        # Unlike 'tackle' above, this move may hit twice as hard if the
        # pokebot is a 'grass' type.
        if pokebot_type == "grass":
            print("It's super effective!")
            actual_damage = (pokemon_atk * 2) - pokebot_def
            
        else:
            # Not a grass type? Normal damage for you, then.
            actual_damage = pokemon_atk - pokebot_def
            
        if actual_damage < 0:
            actual_damage = 0
            
        pokebot_hp = pokebot_hp - actual_damage
        pokemon_move2_pp = pokemon_move2_pp - 1
        print(pokebot_name + " took " + str(actual_damage) + " damage!")
        print(pokebot_name + " now has " + str(pokebot_hp) + " HP.")
        print("'flamethrower' has " + str(pokemon_move2_pp) + " PP remaining.")

    elif inputted_text == "tail whip":
        if pokemon_move3_pp == 0:
            print("'tail whip' has no remaining PP!")
            continue
        
        print(pokemon_name + " whipped its tail at " + pokebot_name + "!")

        # This move doesn't deal HP damage. Instead, it lowers foe's def.
        pokebot_def = pokebot_def - 1

        # Make sure that the foe's 'def' doesn't fall into the negatives.
        if pokebot_def < 0:
            pokebot_def = 0
            
        pokemon_move3_pp = pokemon_move3_pp - 1
        print("'tail whip' has " + str(pokemon_move3_pp) + " PP remaining.")

    elif inputted_text == "growl":
        if pokemon_move4_pp == 0:
            print("'growl' has no remaining PP!")
            continue
        
        print(pokemon_name + " growled at " + pokebot_name + "!")

        # This move lowers the foe's atk.
        pokebot_atk = pokebot_atk - 1
        
        if pokebot_atk < 0:
            pokebot_atk = 0
            
        pokemon_move4_pp = pokemon_move4_pp - 1
        print("'growl' has " + str(pokemon_move4_pp) + " PP remaining.")

    else:
        # We only get here if every 'if' and 'elif' in the chain failed.
        print(pokemon_name + " doesn't know that move!")

        # Since the player entered unrecognized text, return to the top
        # of the loop and re-ask them to enter a command.
        continue

    # Print a blank line to visually separate the enemy pokebot's turn.
    print()

    # If the pokebot hasn't fainted, it fires its built-in water pistol.
    if pokebot_hp > 0:
        print(pokebot_name + " shoots its water pistol at " + pokemon_name + "!")

        # Depending on our pokemon's type, the attack may hit twice or
        # half as hard.
        if pokemon_type == "fire":
            actual_damage = (pokebot_atk * 2) - pokemon_def
            print("It's super effective!")
        elif pokemon_type == "grass":
            actual_damage = (pokebot_atk / 2) - pokemon_def
            print("It's not very effective...")
        else:
            actual_damage = pokebot_atk - pokemon_def
            
        if actual_damage < 0:
            actual_damage = 0
            
        pokemon_hp = pokemon_hp - actual_damage
        print(pokemon_name + " took " + str(actual_damage) + " damage!")
        print(pokemon_name + " now has " + str(pokemon_hp) + " HP.")

# If we're down here, someone has fainted. Who was it?
if pokebot_hp <= 0:
    print(pokebot_name + " has been shut down! " + pokemon_name + " wins!")

else:
    print(pokemon_name + " has fainted! " + pokebot_name + " wins!")
print()
print("Game Over")
