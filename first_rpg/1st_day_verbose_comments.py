# We begin by assigning some int literals (raw integer data) to
# reference names (variables).

player_attack_power = 3
player_magic_power = 8
player_health_points = 20

monster_attack_power = 5
monster_health_points = 20

# For player_attack_power, player_magic_power, and monster_attack_power,
# this assignment has two purposes:
#    1.) It makes it easier to see how later code works. Sure, we could
#        replace every instance of 'player_attack_power' in the code
#        with literal '3', but using the assigned name makes it easier
#        to understand what the purpose of '3' is and how it's being
#        used; it's referring to the player's attack power.
#
#    2.) It allows us to make broad, sweeping changes to the code by
#        changing a single line. We may need to utilize the player's
#        attack power in ten different equations (critical hits,
#        special attacks, etc.) on many different lines. By using the
#        'player_attack_power' reference on all of those lines, instead
#        of a literal '3', we could later change the player's attack
#        power to '7' simply by changing one line: the assignment. If
#        we used a literal '3' for each of those equations, we'd need to
#        change every single '3' to a '7' to increase the attack power,
#        which would be time-consuming and prone to bugs (when you miss
#        one).
#
# For player_health_points and monster_health_points, this assignment
# serves one more purpose: dynamism! As the player's battle rages on,
# these values are constantly changing, but we're able to reuse the
# same lines of code in the 'while' loop because we're referring to
# character health points by REFERENCE (or 'name').
#
# As the fight continues, the raw data that these references are
# POINTING TO is constantly being updated (the number values are
# changing), but the name we've given to refer to that value stays the
# same, so we can loop over the exact same line of code but with a
# different outcome. This is why reference names are often referred to
# as 'variables': the name stays the same, but the value can vary over
# time.

# Now, we enter a 'while' block that will loop over itself until we
# reach a game-over state.

while monster_health_points > 0 and player_health_points > 0:

    # Indented 'code blocks' are run only in certain conditions and may
    # even run outside of a simple top-to-bottom order.
    #
    # In the case of a 'while' block, the indented code will run if the
    # block's 'condition' equals True, which is the same as an 'if'
    # block.
    #
    # However, unlike an 'if' block, when a 'while' block ends, the
    # condition is reevaluated. If it's still True, the code will run
    # again.
    #
    # Just like 'if', the 'while' statement is followed by its
    # condition. 'while True' will run forever, because True is always
    # True.
    #
    # In our case, our 'while' block's condition includes variables that
    # are constantly changing, so there may (and will) come a point where
    # it evaluates to False. At that time, we finally continue with the
    # code below the 'while' block.
    #
    # This 'while' block's "conditional statement" is actually two
    # conditional statements combined using the 'and' operator.
    #    * The '>' operator only evaluates True if the value to its left
    #      is greater than the value to its right.
    #
    #    * The 'and' operator only evaluates True if the the values on
    #      both of its sides equal True.
    #
    # So, our 'while' block only runs (and then re-runs) if
    #    'monster_health_points > 0' works out to be True
    #        and
    #    'player_health_points > 0' works out to be True.
    #
    # If either one of those statements is False, the 'and' operation
    # works out to be False, because 'and' is only True if the statements
    # on both sides of it are True.
    #
    # In other words, if either the monster or the player are dead, we
    # can stop looping over the combat turns and continue to the end of
    # the program.

    # Up until this point, we've only used '=' (the 'assignment
    # operator) to assign reference names to 'literal' (explicitly
    # shown) data.
    #
    # Assignment to an int literal:
    #    my_variable = 121
    #
    # Assignment to a float literal:
    #    my_variable = 121.287
    #
    # Assignment to a str literal:
    #    my_variable = "Hello, world!"
    #
    # Assignment to a bool literal:
    #    my_variable = True
    #
    # However, assignments can also be made to EVALUATED data. That is,
    # data that we don't know what it is until the code is run. This
    # includes:
    #
    # Assignments to mathematical statements:
    #    my_variable = 1 + 2 * 8      # 'my_variable' now refers to '17'.
    #
    # Assignments to conditional statements:
    #    my_variable = 23 > 18     # 'my_variable' now refers to 'False'.
    #
    # Assignments to the value returned by a 'function':
    #    def get_kaiju_greeting(friends_name):
    #        return "Hey, " + friends_name + ". How's it hanging?"
    #
    #    my_variable = get_kaiju_greeting("David")
    # 'my_variable' now refers to '"Hey, David. How's it hanging?"'
    #
    # On the next line, we assign the name 'user_command' to the value
    # returned by Python's built-in 'input' function.
    #
    # 'input' asks the user to type in some data, and it returns that
    # data to our program as a str. Like all functions, it's run by
    # putting parenthesis after the function name. Optionally, between
    # its parenthesis, 'input' takes an 'argument' (supplied data) which
    # is a str that it will print out when it prompts the user.

    user_command = input("Attack or magic? ")

    # 'print' is a Python built-in function which takes any number of
    # comma-separated arguments and will show those arguments to the user.
    # When used without any arguments, it just outputs a blank line.
    #
    # We could technically assign a name to the returned data of 'print',
    # like so:
    #
    #    my_variable = print("Hello, world!")
    #
    # However, this is never done, because print always returns None.
    # 'None' is Python's special data type that means "nothing."
    #
    # Functions which are designed to handle a task that doesn't involve
    # giving data back to the code usually just return None.

    print()

    # 'if' blocks contain code which is only run if the following
    # 'conditional statement' works out to be true.
    #
    # In a conditional statement, the '==' operator means, "is equal to".
    # The '!=' operator means, "is not equal to".
    #
    # Depending on what the user entered as the value for 'user_command',
    # one of the three following code blocks will run.
    #
    # When the player deals damage to the monster, we're updating the
    # name 'monster_health_points' to refer to a new value.
    #
    # At the time of our writing the code, we don't know what this new
    # value is, yet, but it's going to be the CURRENT value referred to
    # by 'monster_health_points' MINUS player_attack_power or
    # player_magic_power, depending on the value of user_command.
    #
    # In other words, the monster's health is now whatever it was
    # minus however much damage we just did.

    if user_command == "attack":
        monster_health_points = monster_health_points - player_attack_power
        print("You attacked the monster with your sword!")
    if user_command == "magic":
        monster_health_points = monster_health_points - player_magic_power
        print("You hit the monster with a fireball!")

    # What follows is our code for dealing with an unrecognized command.
    # Again, the '!=' operator returns True if the values on either side
    # of it are NOT equal. Consider the following examples:
    #
    #    (5 + 5) == 10         # This is True.
    #    (5 + 5) == 11         # This is False.
    #    (5 + 5) != 10         # This is False.
    #    (5 + 5) != 11         # This is True.
    #
    # In our case, we're using the not-equal-to operator to verify that
    # whatever str the user entered into the input prompt, it's NOT
    # one of the str's that we know how to handle.
    #
    # Once again, we're using a compound conditional statement using
    # the 'and' operator. Think of the 'and', 'or', and 'xor'
    # conditional operators as being similar to the simple '+', '-',
    # and '=' mathematical operators that we learned in 1st grade.
    # Instead of working on numbers and returning numbers, these
    # operators work on boolean values ('True' or 'False') and return
    # bools.
    #
    #    1 + 1                 # This is 2.
    #    4 - 1                 # This is 3.
    #
    # For 'and' to return True, the statements on both sides of it
    # must return True.
    #
    #    True and True         # This is True.
    #    False and True        # This is False.
    #    False and False       # This is False.
    #
    #    eligible_for_service = wearing_shirt and wearing_shoes
    #
    # For 'or' to return True, either side of it must return True.
    #
    #    True or True          # This is True.
    #    False or True         # This is True.
    #    False or False        # This is False.
    #
    #    allowed_in_club = cover_charge_has_been_paid or on_vip_list
    #
    # For 'xor' (exclusive-or) to return true, one and ONLY one side
    # of it must return True.
    #
    #    True xor True         # This is False.
    #    False xor True        # This is True.
    #    False xor False       # This is False.
    #
    #    allowed_to_wed_in_texas = person_1_is_male xor person_2_is_male
    #
    # Therefore, the following code block will only run IF the user's
    # command was NOT "attack" and the user's command was NOT "magic".

    if user_command != "attack" and user_command != "magic":
        print("Unrecognized command.")

        # The 'continue' statement, in a looping code block, tells
        # Python to skip the rest of the code in the block and go
        # right back to the top.
        #
        # In this case, the player entered a bad command, so we're
        # skipping the code that follows, which gives the monster an
        # attack, and we're going back to the top of the 'while'
        # loop, which prompts the user for a command.

        continue

    # If we made it this far, that means we didn't trigger the 'if block
    # above which calls 'continue'. So, we know that the player entered
    # a good command and the monster lost health. Let's tell the user
    # how much health the monster has left and then give the monster a
    # turn, lowering the player's health points.
    #
    # Notice that, in Python, the '+' operator isn't only used for
    # numbers such as int's and float's. It can also be used on str's,
    # and it concatenates (adds) them together.
    #
    #    "Hello" + "Bobby"        # This equals "HelloBobby".
    #    "Hello " + "Bobby"       # This equals "Hello Bobby".
    #
    #    best_food = "Pizza"
    #    "The best food is " + best_food
    #
    # The above line equals "The best food is Pizza". Even though we're
    # adding a named reference (variable) instead of a string literal
    # like "Bobby", the values on both sides of '+' are str's, so it
    # works.
    #
    #    "I am " + "31" + " years old."   # Equals "I am 31 years old."
    #    "I am " + 31 + " years old."     # This is an error!
    #
    # In the first line of the preceding code, the middle piece of data
    # is text, and that text just happens to contain an integer. It's a
    # str meant for a human to read, but it has no mathematical value.
    #
    # In the second line, the middle piece of data is an actual integer.
    # That's great when you want to do math on it, but you can't add
    # str's and int's together. They have totally different purposes.
    #
    # Thankfully, Python has built-in functions for intelligently
    # giving us data of a type we want based on an argument we provide.
    #
    #     str(31)     # This returns "31", so you can add it to str's.
    #     int("102")  # This returns 102 as an int, so you can do math.
    #
    # To see how the latter would be useful, consider how the following
    # example uses the built-in function 'input', which always returns
    # a str of whatever the user typed in, and does math on it -- and
    # then turns that data back into a str for printing.
    #
    #    entered_age = input("How old are you, in years? ")
    #    print("In 5 years, you'll be " + str(int(entered_age) + 5)))
    #
    # The line above has many 'nested' functions, or functions whose
    # arguments are the data returned by other functions. Just look at
    # all of those closing-parenthesis at the end! Let's break it down.
    #
    #    1.) The argument for 'int' is 'entered_age', which is the name
    #        we gave to the str value returned earlier by 'input'. This
    #        converts that str value to an int value that we can do
    #        math on.
    #
    #    2.) The argument for 'str' is 'int(entered_age) + 5'. The
    #        built-in function 'str' converts non-textual data to
    #        textual data. In this case, we get the int value of
    #        'entered_age' and add another int, '5', to it. Afterward,
    #        we return the textual version of the whole thing.
    #
    #    3.) The argument for 'print' is a str literal, "In 5 years,
    #        you'll be ", added to the textual data that we got from
    #        the 'str' function.
    #
    # If you don't like the look of nested functions, you can just
    # assign names to all of the data and move it around by reference.
    #
    #    entered_age_as_str = input("How old are you, in years? ")
    #    entered_age_as_int = int(entered_age_as_str)
    #    age_in_5_years_as_int = entered_age_as_int + 5
    #    age_in_5_years_as_str = str(age_in_5_years_as_int)
    #    output_str = "In 5 years, you'll be " + age_in_5_years_as_str
    #    print(output_str)
    #
    # In the code below, in order to print the monster's health points
    # along with the textual label, "Monster health: ", we need to use a
    # textual ('str') version of the int monster_health_points.

    print("Monster health: " + str(monster_health_points))
    print()
    player_health_points = player_health_points - monster_attack_power
    print("The monster bit you on the ass!")
    print("Player health: " + str(player_health_points))
    print()

    # This is the end of our indented 'while' loop. If the loop's
    # condition still returns True, we return to the top from here!

# If we made it this far, the 'while' loop is over, which means that
# its condition finally came up False. Since its condition was that
# both the monster and the player have HP above 0, we know that at
# least one of them is dead if the loop is over.

# If the monster is still alive, you lose!
if monster_health_points > 0:
    print("You lose!")

# If you're still alive, you win!
if player_health_points > 0:
    print("You win!")

# This is the end of the program, but there's a bug, here.
#
# The 'while' loop repeats as long as both the player and monster have HP.
# Because the 'while' loop is over, we know that at least one character is
# totally out of HP.
#
# However, look at the code at the end of our 'while' loop, after our
# attack has reduced the monster's HP:
#
#    print("Monster health: " +str(monster_health_points))
#    print()
#    player_health_points = player_health_points - monster_attack_power
#    print("The monster bit you on the ass!")
#
# We just hit the monster and printed its health points, and then it hit
# us -- but we never checked if the monster was still alive before it got
# its turn! Therefore, at the end of the 'while' loop, we could BOTH be
# dead, and so we won't receive a "You lose!" or "You win!" message. We
# could've killed it and then gotten killed by its dying attack.
#
# We could fix our game-over code by adding another 'if' block using the
# '<=' operator, which means "less-than or equal-to":
#
#    if monster_health_points <= 0 and player_health_points <= 0:
#        print("You're both dead! It's a draw!")
