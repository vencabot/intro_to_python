import random

import pokemon_moves_condensed as pokemon_moves
import pokedex_condensed as pokedex

def battle_turns(combatant_a, combatant_b):
    # This is our Pokemon's turn.
    print()
    print(
            combatant_a.nickname + " the " + combatant_a.monster_type
            + "'s moves:")
    for move_instance in combatant_a.move_dict.values():
        print("    " + move_instance.move_name)
    print()
    user_input = input(
            "What move should " + combatant_a.nickname + " use? ")
    try:
        combatant_a.use(user_input, combatant_b)
    except KeyError:
        print(combatant_a.nickname + " doesn't know " + user_input + "!")
        return
    except pokemon_moves.PPError:
        print(user_input + " has no remaining PP!")
        return
    # This is the opponent Pokemon's turn.
    print()
    if combatant_b.hp > 0:
        available_moves = []
        for move_instance in combatant_b.move_dict.values():
            if (
                    combatant_b.nickname == "Dixxucker"
                    and move_instance.move_name == "comb hair"):
                continue
            if move_instance.current_pp > 0:
                available_moves.append(move_instance)
        if len(available_moves) == 0:
            print(
                    combatant_b.nickname + " the "
                    + combatant_b.monster_type
                    + " has no available moves!")
            return
        random_move = random.choice(available_moves)
        random_move.use_on(combatant_a)


pokemon1 = pokedex.Cyndaquil("Zanzhu")
pokemon2 = pokedex.Cyndaquil("Dixxucker")
pokemon3 = pokedex.Ganja("Locust")
pokemon4 = pokedex.Geodude("Arksam")
combatant_a = pokemon4
opponents = [pokemon1, pokemon2, pokemon3]
random.shuffle(opponents)

# This is where the series of Pokemon battles begins.
for combatant_b in opponents:
    # A new battle begins.
    print(
            combatant_b.nickname + " the " + combatant_b.monster_type
            + " appears!")
    print("It looks pissed off!")
    while combatant_a.hp > 0 and combatant_b.hp > 0:
        battle_turns(combatant_a, combatant_b)
    # The fight is over.
    winner = combatant_a if combatant_a.hp > 0 else combatant_b
    loser = combatant_b if winner is combatant_a else combatant_a
    print(loser.nickname + " the " + loser.monster_type + " has fainted!")
    print(
            winner.nickname + " the " + winner.monster_type
            + " is the winner!")
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
    if loser is combatant_a:
        print("Game Over!")
        break
    print()
