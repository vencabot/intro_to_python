pets_favorite_food = "potato slices"
pets_hated_food = "orange"
pets_happiness = 50
pets_hunger = 100
poop_on_floor = False

pets_name = input("What is your pet's name? ")
print()

while True:
    if not poop_on_floor:
        pet_activity = input("Do you want to 'feed' or 'play' with " + pets_name + "? ")
    else:
        pet_activity = input("Do you want to 'feed' or 'play' with " + pets_name + ", or do you want to 'clean' the room? ")
    print()

    if pet_activity == "feed":
        pets_food = input("What do you want to feed " + pets_name + "? ")
        print()

        if pets_food == pets_favorite_food:
            pets_happiness += 20
        elif pets_food == pets_hated_food:
            pets_happiness -= 40
        elif pets_food == "rocks":
            print("Don't do that, you meanie!")
            print()
            continue
        else:
            pets_happiness -= 10

        print(pets_name + " eats the " + pets_food + ".")

        if pets_happiness >= 80:
            print(pets_name + " seems ecstatic!!")
        elif pets_happiness >= 50:
            print(pets_name + " seems in high spirits.")
        elif pets_happiness >= 25:
            print(pets_name + " seems kind of down.")
        else:
            print(pets_name + " seems mad depressed.")
        print()

        pets_hunger -= 20

        if pets_hunger <= 0:
            print(pets_name + " takes a massive DUMP.")
            print()
            poop_on_floor = True
            pets_hunger = 100

    elif pet_activity == "play":
        if pets_happiness >= 50:
            if pets_hunger > 60:
                print(pets_name + " is too hungry to play!")
                pets_happiness -= 20
            else:
                thrown_object = input("What do you want to fetch with? ")
                print()
                print("You throw the " + thrown_object + ".")
                print()
                if pets_happiness >= 80:
                    print(pets_name + " retrieves the " + thrown_object + " with lightning speed!")
                elif pets_happiness >= 70:
                    print(pets_name + " takes their time retrieving the " + thrown_object + " while wagging their tail(?).")
                else:
                    print(pets_name + " watches the " + thrown_object + " fall and looks at you dumbly.")
                print()
                pets_hunger += 20
        else:
            print(pets_name + " isn't in the mood to play...")
            print()

    elif pet_activity == "quit":
        print(pets_name + " goes back to bed. :D")
        break

    elif pet_activity == "clean":
        if poop_on_floor:
            print("You clean up " + pets_name + "'s poop.")
            print()
            poop_on_floor = False
        else:
            print("There's nothing to clean.")

    elif pet_activity == "dagger":
        print("Dagger's dat dude! How could " + pets_name + " not love 'im?!")
        pets_happiness = 100

    else:
        print("Please either 'feed' or 'play' with " + pets_name + ". Or 'clean' or 'quit'.")
        print()
        continue

    if pets_hunger > 70:
        print(pets_name + " seems kind of hungry...")
        print()
        pets_happiness -= 10

    if poop_on_floor:
        pets_happiness -= 10

    if pets_happiness <= 0:
        print(pets_name + " bites you! And then poops on the dang carpet!")
        print("You faint from embarrassment...")
        break

print("Game Over")
