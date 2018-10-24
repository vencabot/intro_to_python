import random

def deal_damage(opponent_name, opponent_hp, actual_damage):
    if actual_damage < 0:
        actual_damage = 0
    opponent_hp = opponent_hp - actual_damage
    print(opponent_name + " took " + str(actual_damage) + " damage!")
    print(opponent_name + " now has " + str(opponent_hp) + " HP.")
    return opponent_hp

pokemon1_name = "cyndadixx"
pokemon1_type = "fire"
pokemon1_hp = 55
pokemon1_atk = 8
pokemon1_def = 2
pokemon1_move1_pp = 10
pokemon1_move2_pp = 5
pokemon1_move3_pp = 12
pokemon1_move4_pp = 8
pokemon1_move_list = ["tackle", "flamethrower", "tail whip", "growl"]
pokemon2_name = "squirtle"
pokemon2_type = "water"
pokemon2_hp = 68
pokemon2_atk = 6
pokemon2_def = 4
pokemon2_move1_pp = 10
pokemon2_move2_pp = 6
pokemon2_move3_pp = 12
pokemon2_move4_pp = 666
pokemon2_move_list = ["tackle", "bubble", "tail whip", "tatsumakisenpuuken"]

print(pokemon1_name + "'s available moves are:")
print("    tackle")
print("    flamethrower")
print("    tail whip")
print("    growl")
print(pokemon2_name + "'s available moves are:")
print("    tackle")
print("    bubble")
print("    tail whip")
print("    tatsumakisenpuuken")
while pokemon1_hp > 0 and pokemon2_hp > 0:
    print()
    inputted_text = input("What move should " + pokemon1_name + " use? ")
    if inputted_text == "tackle":
        if pokemon1_move1_pp == 0:
            print("'tackle' has no remaining PP!")
            continue
        print(pokemon1_name + " tackled " + pokemon2_name + "!")
        actual_damage = pokemon1_atk - pokemon2_def
        pokemon2_hp = deal_damage(pokemon2_name, pokemon2_hp, actual_damage)
        pokemon1_move1_pp = pokemon1_move1_pp - 1
        print("'tackle' has " + str(pokemon1_move1_pp) + " PP remaining.")
    elif inputted_text == "flamethrower":
        if pokemon1_move2_pp == 0:
            print("'flamethrower' has no remaining PP!")
            continue
        print(pokemon1_name + " blew flames at " + pokemon2_name + "!")
        if pokemon2_type == "grass":
            print("It's super effective!")
            actual_damage = (pokemon1_atk * 2) - pokemon2_def
        else:
            actual_damage = pokemon1_atk - pokemon2_def
        pokemon2_hp = deal_damage(pokemon2_name, pokemon2_hp, actual_damage)
        pokemon1_move2_pp = pokemon1_move2_pp - 1
        print("'flamethrower' has " + str(pokemon1_move2_pp) + " PP remaining.")
    elif inputted_text == "tail whip":
        if pokemon1_move3_pp == 0:
            print("'tail whip' has no remaining PP!")
            continue
        print(pokemon1_name + " whipped its tail at " + pokemon2_name + "!")
        pokemon2_def = pokemon2_def - 1
        if pokemon2_def < 0:
            pokemon2_def = 0
        pokemon1_move3_pp = pokemon1_move3_pp - 1
        print("'tail whip' has " + str(pokemon1_move3_pp) + " PP remaining.")
    elif inputted_text == "growl":
        if pokemon1_move4_pp == 0:
            print("'growl' has no remaining PP!")
            continue
        print(pokemon1_name + " growled at " + pokemon2_name + "!")
        pokemon2_atk = pokemon2_atk - 1
        if pokemon2_atk < 0:
            pokemon2_atk = 0
        pokemon1_move4_pp = pokemon1_move4_pp - 1
        print("'growl' has " + str(pokemon1_move4_pp) + " PP remaining.")
    else:
        print(pokemon1_name + " doesn't know that move!")
        continue
    print()
    if pokemon2_hp > 0:
        pokemon2_random_index = random.randint(0, 3)
        inputted_text = pokemon2_move_list[pokemon2_random_index]

        if inputted_text == "tackle":
            if pokemon2_move1_pp == 0:
                print("'tackle' has no remaining PP!")
                continue
            print(pokemon2_name + " tackled " + pokemon1_name + "!")
            actual_damage = pokemon2_atk - pokemon1_def
            pokemon1_hp = deal_damage(pokemon1_name, pokemon1_hp, actual_damage)
            pokemon2_move1_pp = pokemon2_move1_pp - 1
            print("'tackle' has " + str(pokemon2_move1_pp) + " PP remaining.")
        elif inputted_text == "bubble":
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
            if pokemon2_move4_pp == 0:
                print("'tatsukamisenpuuken' has no remaining PP!")
                continue
            print(pokemon2_name + " executed a whirling kick at " + pokemon1_name + "!")
            actual_damage = (pokemon2_atk * 2) - pokemon1_def
            pokemon1_hp = deal_damage(pokemon1_name, pokemon1_hp, actual_damage)
            pokemon2_move4_pp = pokemon2_move4_pp - 1
            print("'tatsumakisenpuuken' has " + str(pokemon2_move4_pp) + " PP remaining.")
        else:
            print(pokemon2_name + " doesn't know that move!")
            continue
if pokemon2_hp <= 0:
    print(pokemon2_name + " has fainted! " + pokemon1_name + " wins!")
else:
    print(pokemon1_name + " has fainted! " + pokemon2_name + " wins!")
print()
print("Game Over")
