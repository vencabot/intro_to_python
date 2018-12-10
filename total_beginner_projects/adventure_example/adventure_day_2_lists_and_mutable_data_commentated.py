#########################################################################
# adventure_day_2_lists_and_mutable_data_commentated.py                 #
#     - developed at twitch.tv/vencabot , Intro to Python 11/30/18      #
#     - watch the archived stream at _______________________________    #
#                                                                       #
# We're continuing our ZORK-styled text adventure! Because this kind of #
# game is more abstract than the simple RPG that we made in our last    #
# season, we're getting into more advanced concepts slightly sooner --  #
# maybe sooner than I'd like!                                           #
#                                                                       #
# In the last episode, we went over the basics of function definitions: #
# code blocks that can be executed by 'calling' them from anywhere else #
# in the program. We talked about how functions shouldn't access data   #
# from outside of them unless that data is supplied as an 'argument',   #
# and variables that are created or updated within a function aren't    #
# changed OUTSIDE of the function, so they need to 'return' some data   #
# in order to have an affect on the rest of the game.                   #
#                                                                       #
# That's all still true, except that, today, we look at our first type  #
# of 'mutable' data, whose changes are always saved no matter where     #
# those changes are made in the program. This means that a piece of     #
# mutable data can be altered within a function, and that alteration is #
# reflected beyond the confines of that function, so no 'return'        #
# statement is necessary.                                               #
#                                                                       #
# To be more specific, we replaced our old 'player_has_key' boolean     #
# variable, which used to save whether or not the player had picked up  #
# the key, with a 'player_inventory' list. A 'list' is a data-type that #
# can contain any number of other data types, and, in this case, we're  #
# using a list to store a bunch of textual strings representing what    #
# the player owns, including "key" and "torch".                         #
#                                                                       #
# Now, for functions that need to know whether or not the player has a  #
# key, such as when they're trying to leave the cave or open a door, we #
# don't feed them a boolean argument to tell them whether or not the    #
# player has a key; rather, we supply them a list of what the player    #
# has in their inventory, and the function checks to see whether or not #
# "key" is in that list.                                                #
#                                                                       #
# When functions like 'get_the_key' and 'get_the_torch' use             #
# player_inventory's "append" method (a 'method' is a function that     #
# BELONGS to a piece of data, called using that data's name followed by #
# a period, such as player_inventory.append()), the value of the list   #
# is universally updated, so the player_inventory doesn't need to be    #
# returned out of the function.                                         #
#                                                                       #
# Basically, data types like booleans (and all of the others we've used #
# up to this point) are 'immutable,' which means that their data can    #
# never be changed. If that's true, though, then how does a variable    #
# like 'chest_is_open' go from being False to True?                     #
#                                                                       #
# Basically, when you say something like:                               #
#                                                                       #
# chest_is_open = False                                                 #
# chest_is_open = True                                                  #
#                                                                       #
# You're not changing (or 'mutating') the False to a True. Rather,      #
# you're replacing the old False with a brand new True, and the old     #
# False ceases to exist. Furthermore, as far as Python is concerned,    #
# the value of 'chest_is_open' isn't 'changing', either. Instead,       #
# you're making a brand new variable called 'chest_is_open', and it's   #
# overwriting any old variables which shared the same name.             #
#                                                                       #
# This is why you can't 'change' the value of a variable within a       #
# function and have that change be reflected outside of the function.   #
# Any variable created in a function, even if it has the same name as a #
# variable that exists OUTSIDE of the function, is deleted when the     #
# function ends.                                                        #
#                                                                       #
# In the case of a list, though, the underlying data is capable of      #
# being altered, and so, if you feed a list into a function, that list  #
# can be changed, even if the name (variable) that we're using to refer #
# to that list goes away when the function is over. If we feed a        #
# boolean into a function as an argument and want to 'change' it, we    #
# need to create a whole new boolean with a new name to refer to it     #
# (even if that name is the same as its old name), and all of the names #
# in a function vanish when that function is over. We gotta RETURN the  #
# new data out in order to save it. In the case of a list, though, or   #
# any other piece of 'mutable' data, we can change the data without     #
# having to create a new piece of data. Although the name we're using   #
# to refer to the list within the function goes away, the list, itself, #
# is the same list that we were fed from outside, so it continues to    #
# exist -- including any changes we made to it during our function!     #
#                                                                       #
# It's a little bit complicated, so be sure to watch the archive of the #
# stream to see some more demonstrations. We'll also review this idea   #
# in greater depth in the future!                                       #
#                                                                       #
# Aside from that, we also created a few new boolean variables and      #
# simple functions in the same style as in our previous episode, to     #
# make our game a little bit more involved. For instance, there's now a #
# door that can be unlocked and opened using the key, and a torch to    #
# pick up.                                                              #
#                                                                       #
#########################################################################

# The 'look_around' function has been updated since our last episode.
# Before, it simply printed out a description of the cave, but now that
# description will vary depending on whether or not the player has picked
# up the torch. As you might expect, we need to supply the player's
# inventory as an argument to the function, now, so that it can see what
# the list does and doesn't have.
def look_around(player_inventory):
    # Print off a simple description.
    print("The cave is dank and there's a treasure chest.")
    print("There's also a door.")

    # The 'in' operator returns True if the supplied data matches any
    # piece of data in a supplied list. As before, the 'not' operator
    # reverses the value of the following boolean.

    # Remember, an 'if' block will only run if its condition is True.
    # So, if player_inventory looks like '["key", "gold"]', then:
    # "torch" in player_inventory
    # returns False, and then:
    # not False
    # returns True.

    # So, if the player doesn't have a torch, then:
    # not "torch" in player_inventory
    # returns True, triggering the 'if' block.
    if not "torch" in player_inventory:
        print("There's also a torch.")

    # Otherwise, the player DOES have the torch, so do this.
    else:
        print("There's an empty spot where the torch was.")


# This is still just a function that prints a string. It doesn't require
# any arguments to do its job, nor does it update any data that needs to
# be returned out.
def do_a_dance():
    print("You perform a break-dance. What style!")


# When the player asks to open the treasure chest, we need some info in
# order to know what should happen, and that data is supplied as argu-
# ments to the function. We need to know whether or not the chest is
# already open, and we need to know if the player already has the key. In
# this updated game, we don't simply tell functions whether or not the
# player has the key; instead, we give them the player's inventory, and
# they can check to see if it has the key.
def open_the_chest(chest_is_open, player_inventory):
    # If the chest isn't open, open it!
    if not chest_is_open:
        print("You open the chest. There's a key inside.")
        chest_is_open = True

    # If the chest IS open and the player doesn't have the key...
    elif not "key" in player_inventory:
        print("The chest is already open. There's a key inside.")

    # If the chest is open and the player DOES have the key...
    else:
        print("The chest is already open. It's empty.")

    # Report to the caller whether or not the chest is open, now.
    return chest_is_open


# 'get_the_key' used to have to return a boolean that represented whether
# or not, by the end of the function, the player has the key.
# Now, instead of returning a boolean that the caller can use to update
# the player's progress, the supplied inventory gets updated directly.
# Because lists are pieces of 'mutable' data, the list that we're given
# as the 'player_inventory' argument can be altered within the function.
# The changes that we make to the list are saved, even though we're not
# returning anything.
def get_the_key(chest_is_open, player_inventory):
    # If the chest is open and the player doesn't already have the key...
    if chest_is_open and "key" not in player_inventory:
        # Let the player know that they grabbed the key.
        print("You picked up the key!")

        # Use the list's 'append' method to add a string representing the
        # key to the list.
        player_inventory.append("key")

    # If the chest is open and the player DOES have the key...
    elif chest_is_open and "key" in player_inventory:
        print("You already got the key!")

    # Otherwise, the chest is closed.
    else:
        print("You don't see a key.")


# Just as before, the player can only leave the cave if they have the
# key. The boolean value that's returned by this function is what the
# game's main loop looks for to decide whether or not to keep running.
# So, if this function returns False, the game will end.
def leave_the_cave(player_inventory):
    # If the player has the key, they're allowed to leave.
    if "key" in player_inventory:
        print("You walked out of the cave.")
        adventure_is_ongoing = False

    # Otherwise, they can't leave, yet!
    else:
        print("Aren't you forgetting something?")
        adventure_is_ongoing = True

    # If 'adventure_is_ongoing' is False, the game is over. Find out why
    # that is in the 'while' loop, below!
    return adventure_is_ongoing


# The player can also grab a torch, now, although it doesn't have a use.
def get_the_torch(player_inventory):
    if "torch" not in player_inventory:
        print("You picked up the torch.")
        player_inventory.append("torch")
    else:
        print("You already have the torch, dumb-dumb.")


# In order to open the door, we need to know two things about the
# player's current progress, which are supplied as boolean arguments to
# the 'open_the_door' function. By the end of the function, depending on
# the player's current progress, the state of 'door_is_open' may have
# changed, so return that data out to the caller, who can update the
# player's progress.
def open_the_door(door_is_unlocked, door_is_open):
    # If the door is locked...
    if not door_is_unlocked:
        print("The door's locked, dang it!")

    # Otherwise, if the door is locked but still closed, open it!
    elif not door_is_open:
        print("You open the door.")
        door_is_open = True

    # Otherwise, the door must be unlocked and open.
    else:
        print("It's already open.")

    # Let the caller know if the door is open or not, now.
    return door_is_open


# In order to unlock the door, we gotta know if the door is already
# unlocked and whether or not the player has the key. We can figure out
# that second part if we can have a list of what the player currently
# has, which we supply as the second argument, 'player_inventory'.
def unlock_the_door(door_is_unlocked, player_inventory):
    if door_is_unlocked:
        print("The door's already unlocked.")

    # So, the door's locked. But what if you don't have a key?
    elif "key" not in player_inventory:
        print("You don't have a key.")

    # The door is locked AND you have a key? Let's unlock it, then!
    else:
        print("You use the key to unlock the door.")
        door_is_unlocked = True

    # We're done, so report to the caller if the door is still locked.
    return door_is_unlocked


# Now that we've defined all of the things the player can do in the game,
# let's set up the player's progress data at the very start of the game.

# The chest starts off closed.
chest_is_open = False

# The door starts off locked.
door_is_unlocked = False

# And the door is closed, of course.
door_is_open = False

# The player starts with nothign, so 'inventory' is an empty list.
player_inventory = []

# As long as this is True, the game will keep asking for commands.
adventure_is_ongoing = True

# Print off a string welcoming the player to the game.
print("You are in a cave.")


# This is the main 'while' loop that keeps the game running. It'll keep
# repeating for as long as 'adventure_is_ongoing' is True. As you can
# see, 'adventure_is_ongoing' gets updated when the player tries to leave
# the cave.
while adventure_is_ongoing:
    # At the start of the loop, ask the player for a command and save it.
    player_command = input("Whachu wanna do? ")

    # Compare the player's command to a bunch of textual strings that the
    # game can recognize. The '==' operator returns True if the data on
    # either side is equivalent and False if they aren't. If the command
    # is recognized, run the appropriate function, supplying whatever
    # arguments that function needs and, if necessary, take the data
    # returned by the function and use it to update the player's progress.

    # If the player wants to look around, we need to know if the player
    # already has the torch. If they do, they won't see it on the ground.
    if player_command == "look around":
        look_around(player_inventory)

    # If the player wants to do a dance, well, we don't need to supply any
    # arguments or save any new progress. They just do a dance.
    elif player_command == "do a dance":
        do_a_dance()

    # If the player wants to open the chest, we gotta know if the chest is
    # already open and whether or not the player has the key, which will
    # determine whether or not they see the key in the chest. The function
    # returns True or False, representing whether the chest is open or not
    # once it completes, so we update the player's progress.
    elif player_command == "open the chest":
        chest_is_open = open_the_chest(chest_is_open, player_inventory)

    # If the player wants to get the key, they can only do so if the
    # chest is open and they don't already have the key. The function
    # USED to return True or False, and we'd save that as 'player_has_key'
    # to update the player's progress. Now, the player has a mutable
    # (changeable) inventory, instead. We supply the inventory as an
    # argument, and the function can add the key to the inventory, itself.
    elif player_command == "get the key":
        get_the_key(chest_is_open, player_inventory)

    # If the player wants to leave the cave, we need to know whether or
    # not they have the key, which is how we're arbitrarily determining if
    # they've 'completed' the game (even though we have a locked door to
    # open, now; we just never updated the win condition). The function
    # returns a True or False value which represents whether or not we
    # should keep playing, which we save and use to determine if we should
    # keep looping and asking the player for commands.
    elif player_command == "leave the cave":
        adventure_is_ongoing = leave_the_cave(player_inventory)

    # The player can get a torch, now. We supply the player's inventory as
    # an argument to the function we made for this purpose. If the torch
    # isn't already in the inventory, it'll be added. Since the inventory
    # is a 'list' (mutable data), the function can update the last for us;
    # it doesn't need to return anything for us to manually update, here.
    elif player_command == "get the torch":
        get_the_torch(player_inventory)

    # If the player wants to open the door, we need to know if the door is
    # locked and if it's already open. The function returns a boolean
    # value which represents whether or not the door is open, now.
    elif player_command == "open the door":
        door_is_open = open_the_door(door_is_unlocked, door_is_open)

    # If the player wants to unlock the door, we just gotta know if the
    # door is currently locked and if the player has the key. To answer
    # the latter question, we supply the player's inventory, and the
    # function can check whether or not it contains the key. The function
    # returns a boolean value representing whether or not the door is
    # locked anymore, and we save the player's progress.
    elif player_command == "unlock the door":
        door_is_unlocked = unlock_the_door(door_is_unlocked, player_inventory)

    # If none of the other commands were recognized, the player is S.O.L.
    else:
        print("You can't do that.")

    # Print a blank line before asking the player for another command.
    # This just makes the screen more readable.
    print()

# If we're down here, then we finished the 'while' loop. That means that
# 'leave_the_cave' got executed and returned 'False' as the new value for
# 'adventure_is_ongoing'. Since the game is done, just print a message
# and end.
print("Game over.")
