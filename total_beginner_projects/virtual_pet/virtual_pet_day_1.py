#Cool bro been reading over your codes =)
pets_favorite_food = "caramel apple"
pets_hated_food = "okra"
pets_happiness = 50
pets_hunger = 50

print("What is your pet's name?")
pets_name = input()
print()

while pets_hunger > 0:
    print("What do you want to feed " + pets_name + "?")
    pets_food = input()

    if pets_food == pets_favorite_food:
        pets_happiness = pets_happiness + 20
    else:
        if pets_food == pets_hated_food:
            pets_happiness = pets_happiness - 40
        else:
            pets_happiness = pets_happiness - 10

    print()
    print(pets_name + " eats the " + pets_food + ".")

    if pets_happiness >= 80:
        print(pets_name + " seems ecstatic!!")
    else:
        if pets_happiness >= 50:
            print(pets_name + " seems in high spirits.")
        else:
            if pets_happiness >= 25:
                print(pets_name + " seems kind of down.")
            else:
                print(pets_name + " seems mad depressed.")
    print()

    pets_hunger = pets_hunger - 20

print(pets_name + " is full.")
