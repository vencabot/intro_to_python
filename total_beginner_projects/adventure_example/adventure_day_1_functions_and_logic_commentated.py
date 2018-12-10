#########################################################################
# adventure_day_1_functions_and_logic_commentated.py                    #
#     - developed at twitch.tv/vencabot , Intro to Python 11/30/18      #
#     - watch the archived stream at youtube.com/watch?v=BfiMU2GwVNY    #
#                                                                       #
# In this episode, we're starting a brand new project! Because a text-  #
# based adventure game (in the tradition of ZORK) is more abstract than #
# a simple RPG like Pokemon, we're getting into more advanced concepts  #
# slightly sooner -- maybe sooner than I would like!                    #
#                                                                       #
# For instance, we're already examining 'functions' in this script,     #
# which are a very powerful tool, although they may be somewhat hard to #
# understand for those who have never programmed before.                #
#                                                                       #
# Also, we're using a lot more 'boolean' (True / False) values than we  #
# did with Pokemon and fewer numerical values (since numbers are the    #
# core of RPGs and not that useful in adventure games).                 #
#                                                                       #
# The most important thing to remember when reading this program is     #
# that indented code is only run under certain circumstances, but code  #
# that's along the margin is always read top-to-bottom.                 #
#                                                                       #
# For instance, this script starts with a bunch of function definitions #
# that are called later in the program, but those functions are not     #
# executed when the program starts; they're only defined. Once the      #
# functions are defined, then 3 boolean variables are defined to be     #
# used to keep track of the player's progress in the game. Finally, the #
# game's main gameplay loop begins, where the player is asked for input #
# and that input is tested against the game's known commands. If the    #
# command is a match, the game runs the matching function that was      #
# defined earlier and maybe updates the player's progress.              #
#                                                                       #
# Once the 'adventure_is_ongoing' variable is changed from True to      #
# False, the 'while' loop can end and the game prints 'Game Over'!      #
#                                                                       #
#########################################################################

# Before anything else in our code, we define a bunch of functions that
# the game will use whenever the player inputs a particular command.

# Some of these functions, like look_around and do_a_dance, simply show
# the user some text so that they can get a sense of the game.

# Other functions need to know the player's current progress in order to
# decide what to do, and they made even 'return' some new data to update
# the player's progress after they run.

# 'look_around' just prints a description of the cave so that the player
# gets some atmosphere and knows there's a chest.
def look_around():
    print("The cave is dank and there's a treasure chest.")


# This is just a cute function that doesn't really do anything.
def do_a_dance():
    print("You perform a break-dance. What style!")

# 'open_the_chest' needs some data to know how to do its job, and it also
# needs to be able to update the player's progress (change the state of
# the chest from 'closed' to 'open'.

# Functions can use data from the outside world by taking it in as
# 'arguments'. When defining a function, you can specify the arguments
# that it needs by putting the comma-separated variable names between the
# parenthesis after the function's name.

# This function requires two variables that we're calling chest_is_open
# and player_has_key. Because our code isn't commented very well (we can
# talk about proper commenting later), you might not realize that both of
# these values need to be booleans (True or False). Now, when the
# function is called, it can take for granted that it has access to these
# two variables.

# The variables that are created or changed within a function cease to
# exist once the function ends. Therefore, functions can't have an affect
# on the code outside of them (with the exception of 'mutable' data,
# which we'll talk about at a future date).

# So, to get data OUT of a function, you 'return' the data. Then, when
# the function is called, the 'result' or 'return value' of the function
# can be assigned to a variable by whoever called the function.
def open_the_chest(chest_is_open, player_has_key):
    # If the chest is closed, give the player some feedback and open it.
    if not chest_is_open:
        print("You open the chest. There's a key inside.")
        chest_is_open = True
    # If the chest is open but the key hasn't been collected...
    elif not player_has_key:
        print("The chest is already open. There's a key inside.")
    # If the chest is open and the key has been collected...
    else:
        print("The chest is already open. It's empty.")
    # Let the caller know whether the chest is open or closed, now.
    return chest_is_open


# The function for grabbing the key is very similar to the function for
# opening the chest. Its behavior changes depending on whether or not the
# chest is open and the player has the key, so it needs some boolean
# arguments in order to work. Then, it returns whether or not the player
# has the key once the function is over.
def get_the_key(chest_is_open, player_has_key):
    if chest_is_open and not player_has_key:
        print("You picked up the key!")
        player_has_key = True
    elif chest_is_open and player_has_key:
        print("You already got the key!")
    else:
        print("You don't see a key.")
    return player_has_key


# Once the player has the key, they can end the game by leaving the cave.
# In order to escape the 'while' loop which keeps the game running, the
# 'adventure_is_ongoing' variable must be set to False, so we return that
# data with this function so that the game can end (or not, if the player
# doesn't have the key, yet).
def leave_the_cave(player_has_key):
    if player_has_key:
        print("You walked out of the cave.")
        adventure_is_ongoing = False
    else:
        print("Aren't you forgetting something?")
        adventure_is_ongoing = True
    return adventure_is_ongoing


# Now that all of our functions are defined, we're going to define the
# starting progress of the player. We'll feed these variables as
# arguments to the functions we defined, above, so that their behavior
# can change based on the player's progress. That's what gives the game a
# beginning, middle, and end!
chest_is_open = False
player_has_key = False
adventure_is_ongoing = True


# Print off a message that invites the player to the game.
print("You are in a cave.")


# A 'while' loop will only run if its 'condition' is True. In that sense,
# it's a lot like an 'if' block -- but, once Python reaches the last line
# of code indented into the 'while' block, it'll actually return BACK to
# the top and will run AGAIN if its condition is still True.

# In this case, we're going to keep asking the player for a command and
# acting on that command for as long as the name 'adventure_is_ongoing'
# points to a value that is True.

# When the player tries to leave the cave, the value of
# 'adventure_is_ongoing' will be changed to False if they already
# collected the key. Thus, when the 'while' loop returns back to the top,
# its condition will be False and it won't run again, letting us continue
# to the next line of code after the block. In our case, that's just a
# 'game over' message.

# Keep on looping the indented code until adventure_is_ongoing is False.
while adventure_is_ongoing:
    # Ask the player to type something. When they hit 'enter', save what
    # they typed into a variable named 'player_command'.
    player_command = input("Whachu wanna do? ")

    # Execute a different function depending on what the player typed.
    #     'if' blocks will only run if their condition is True.
    #
    #     'else' blocks will only run if the preceding 'if' (or 'elif')
    #     failed to run, because its condition was False.
    #
    #     'elif' blocks will only run if the previous 'if' or 'elif'
    #      condition was False and the provided condition is True.
    #      Think of it as an 'else' immediately followed by a new 'if'.
    #
    # The '==' operator will compare two pieces of data and return True
    # if they're equivalent or False if they're not.

    # If the player typed "look around", run the appropriate function.
    if player_command == "look around":
        look_around()

    # Otherwise, if they typed "do a dance", run THAT function.
    elif player_command == "do a dance":
        do_a_dance()

    # Otherwise, if they want to open the chest, run 'open_the_chest' by
    # supplying the information that it needs as arguments. Also, save
    # the value that it returns as the new value for 'chest_is_open'.
    elif player_command == "open the chest":
        chest_is_open = open_the_chest(chest_is_open, player_has_key)

    # Otherwise, if they want to get the key, run the appropriate
    # function, which requires two arguments so that it can do its job.
    # Save the value that it returns as the new value for
    # 'player_has_key'.
    elif player_command == "get the key":
        player_has_key = get_the_key(chest_is_open, player_has_key)

    # Otherwise, if they want to leave the cave, supply the argument, run
    # the function, and save the new value for whether or not the
    # adventure is ongoing. If this value becomes 'False', the 'while'
    # loop that we're in will end and the game will be over.
    elif player_command == "leave the cave":
        adventure_is_ongoing = leave_the_cave(player_has_key)

    # Otherwise, if NONE of the above conditions were met, the player
    # must have typed a command that we don't have a response ready for.
    # Tell them that we can't do whatever they asked us to do.
    else:
        print("You can't do that.")

    # Before returning back to the top of the 'while' loop, print a blank
    # line to make the game's output easier to read.
    print()

# Once the 'while' loop is over, we just print 'Game over' and stop.
print("Game over.")
