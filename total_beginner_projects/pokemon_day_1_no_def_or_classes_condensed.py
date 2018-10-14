pokemon_name = "cyndaquil"
pokemon_type = "fire"
pokemon_hp = 55
pokemon_atk = 8pokemon_def = 2
pokemon_move1_pp = 10
pokemon_move2_pp = 5
pokemon_move3_pp = 12
pokemon_move4_pp = 8

pokebot_name = "pokebot bulbasaur"
pokebot_type = "grass"
pokebot_hp = 68
pokebot_atk = 6
pokebot_def = 4

print(pokemon_name + "'s available moves are:")
print("    tackle")
print("    flamethrower")
print("    tail whip")
print("    growl")

while pokemon_hp > 0 and pokebot_hp > 0:
    print()
    inputted_text = input("What move should " + pokemon_name + " use? ")
    if inputted_text == "tackle":
        if pokemon_move1_pp == 0:
            print("'tackle' has no remaining PP!")
            continue
        print(pokemon_name + " tackled " + pokebot_name + "!")
        actual_damage = pokemon_atk - pokebot_def
        if actual_damage < 0:
            actual_damage = 0
        pokebot_hp = pokebot_hp - actual_damage
        pokemon_move1_pp = pokemon_move1_pp - 1
        print(pokebot_name + " took " + str(actual_damage) + " damage!")
        print(pokebot_name + " now has " + str(pokebot_hp) + " HP.")
        print("'tackle' has " + str(pokemon_move1_pp) + " PP remaining.")
    elif inputted_text == "flamethrower":
        if pokemon_move2_pp == 0:
            print("'flamethrower' has no remaining PP!")
            continue
        print(pokemon_name + " blew flames at " + pokebot_name + "!")
        if pokebot_type == "grass":
            print("It's super effective!")
            actual_damage = (pokemon_atk * 2) - pokebot_def
        else:
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
        pokebot_def = pokebot_def - 1
        if pokebot_def < 0:
            pokebot_def = 0
        pokemon_move3_pp = pokemon_move3_pp - 1
        print("'tail whip' has " + str(pokemon_move3_pp) + " PP remaining.")
    elif inputted_text == "growl":
        if pokemon_move4_pp == 0:
            print("'growl' has no remaining PP!")
            continue
        print(pokemon_name + " growled at " + pokebot_name + "!")
        pokebot_atk = pokebot_atk - 1
        if pokebot_atk < 0:
            pokebot_atk = 0
        pokemon_move4_pp = pokemon_move4_pp - 1
        print("'growl' has " + str(pokemon_move4_pp) + " PP remaining.")
    else:
        print(pokemon_name + " doesn't know that move!")
        continue
    print()
    if pokebot_hp > 0:
        print(pokebot_name + " shoots its water pistol at " + pokemon_name + "!")
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

if pokebot_hp <= 0:
    print(pokebot_name + " has been shut down! " + pokemon_name + " wins!")
else:
    print(pokemon_name + " has fainted! " + pokebot_name + " wins!")
    
print()
print("Game Over")
