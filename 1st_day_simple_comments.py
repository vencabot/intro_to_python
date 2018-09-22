# In Python, all text following a '#' is ignored until the line ends.
#
# This text is referred to as a 'comment' and is useful for taking notes
# about your code as you write it, or helping other programmers know
# what you're thinking.

# Our program starts by assigning some names to some numbers.

# From now on, when we say 'player_attack_power', we mean 3.
player_attack_power = 3

# Our character is a wizard, I guess! Magic attack is way stronger.
player_magic_power = 8

# Over the course of the game, the name 'player_health_points' will
# refer to many different numbers. At the start, it's 20!
player_health_points = 20

# The monster's physical attack is stronger than ours. It has no magic.
monster_attack_power = 5

# Like 'player_health_points', the name 'monster_health_points' will
# always be used in the same equations, but the value it points to will
# constantly be changing. It also begins by referring to 20.
monster_health_points = 20

# Keep on looping as long as the monster and the player both have HP
# remaining.
while monster_health_points > 0 and player_health_points > 0:

    # Ask the user to enter a textual command and refer to that command
    # as 'user_command' from now on.
    user_command = input("Attack or magic? ")

    # Print a blank line just to make things easier to read for the user.
    print()

    # If the value we saved as 'user_command' equals the string "attack",
    # run the following, indented code block.
    if user_command == "attack":

        # Update the value of 'monster_health_points' after damage.
        monster_health_points = monster_health_points - player_attack_power

        # Print a cute message to the user letting them know what's up.
        print("You attacked the monster with your sword!")

    # If the user wants to use magic, run the following code block.
    if user_command == "magic":

        # Update the value of 'monster_health_points' after damage.
        monster_health_points = monster_health_points - player_magic_power

        # Print a cute message to let the user know what's up.
        print("You hit the monster with a fireball!")

    # If the command isn't "attack" AND the command isn't "magic", run the
    # following code block.
    if user_command != "attack" and user_command != "magic":

        # Let the user know that they fucked up their command.
        print("Unrecognized command.")

        # Skip the rest of the code in the 'while' loop and go right back
        # to the top.
        continue

    # Let the player know the monster's post-damage health.
    print("Monster health: " + str(monster_health_points))
    print()

    # The monster attacks the player, now! Bastard.
    player_health_points = player_health_points - monster_attack_power
    print("The monster bit you on the ass!")

    # Let the player know how much health they have left.
    print("Player health: " + str(player_health_points))
    print()

    # This is the end of the indented code, so the 'while' block is over.
    # If the 'while' block's condition is still True, it'll go back to
    # the top. If it's now False, the loop ends and we continue below.

# If we're here, the 'while' loop is over, which means that someone is
# dead. Let's print a message depending on who's left alive.

# If the monster is still alive, the player loses.
if monster_health_points > 0:
    print("You lose!")

# If the player is still alive, the player wins.
if player_health_points > 0:
    print("You win!")

# There's a bug in our game-over screen.
# Since, in our 'while' block, the monster ALWAYS gets a turn after the
# player does, EVEN IF THE MONSTER'S HEALTH IS 0 OR BELOW, there's the
# possibility that neither the monster OR the player will be alive by
# the end of the loop. The monster could reduce the player's health to
# 0 or below with its final, dying attack.
#
# Since our game-over code, above, only prints a message based on who
# is left alive, it won't print any message at all if both characters
# are dead. We can fix that with a couple more lines of code.
#
#    if monster_health_points <= 0 and player_health_points <= 0:
#        print("You're both dead! It's a draw!")

