player_attack_power = 3
player_magic_power = 8
player_health_points = 20

monster_attack_power = 5
monster_health_points = 20

while monster_health_points > 0 and player_health_points > 0:
    user_command = input("Attack or magic? ")
    print()

    if user_command == "attack":
        monster_health_points = monster_health_points - player_attack_power
        print("You attacked the monster with your sword!")

    if user_command == "magic":
        monster_health_points = monster_health_points - player_magic_power
        print("You hit the monster with a fireball!")

    if user_command != "attack" and user_command != "magic":
        print("Unrecognized command.")
        continue

    print("Monster health: " + str(monster_health_points))
    print()

    player_health_points = player_health_points - monster_attack_power
    print("The monster bit you on the ass!")
    print("Player health: " + str(player_health_points))
    print()

if monster_health_points > 0:
    print("You lose!")

if player_health_points > 0:
    print("You win!")
