"""Create a Character Generator for Fallout 4."""

print("You awake from 200 years in deep freeze. The wasteland awaits you.")
name = input("What's your name? ")
gender = input("What's your gender? ")
points = 21
attributes = ("Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck")
strength = 1
perception = 1
endurance = 1
charisma = 1
intelligence = 1
agility = 1
luck = 1

while True:
    print
    print("You have ", points, "points left.")
    print(
        """
        1 - add points
        2 - remove points
        3 - see points per attribute
        4 - exit
        """)

    choice = input("choice: ")
    if choice == "1":
        attribute = input("which attribute? S. P. E. C. I. A. L.?")
        if attribute in attributes:
            add = int(input("How many points? "))
            if add <= points and add > 0:
                if attribute == "S" or attribute == "s":
                    strength += add
                    print(name, "now has ", strength, "strength points.")
                elif attribute == "P" or attribute == "p":
                    perception += add
                    print(name, "now has ", perception, "perception points.")
                elif attribute == "E" or attribute == "e":
                    endurance += add
                    print(name, "now has ", endurance, "endurance points.")
                elif attribute == "C" or attribute == "c":
                    charisma += add
                    print(name, "now has ", charisma, "charisma points.")
                elif attribute == "I" or attribute == "i":
                    intelligence += add
                    print(name, "now has ", intelligence, "intelligence points.")
                elif attribute == "A" or attribute == "a":
                    agility += add
                    print(name, "now has ", agility, "agility points.")
                elif attribute == "L" or attribute == "l":
                    luck += add
                    print(name, "now has ", luck, "luck points.")
                points -= add
            else:
                print("Invalid attribute. You are likely to be eaten by a Grue.")
        elif choice == "2":
            if attribute in attributes:
                remove = int(input("How many points? "))
                # if remove <= points and remove > 0:
                if attribute == "S" or attribute == "s" and remove <= strength and remove > 1:
                    strength -= remove
                    print(name, "now has ", strength, "strength points.")
                    points += remove
                elif attribute == "P" or attribute == "p" and remove <= strength and remove > 1::
                    perception -= remove
                    print(name, "now has ", perception, "perception points.")
                    points += remove
                elif attribute == "E" or attribute == "e" and remove <= strength and remove > 1::
                    endurance -= remove
                    print(name, "now has ", endurance, "endurance points.")
                    points += remove
                elif attribute == "C" or attribute == "c" and remove <= strength and remove > 1::
                    charisma -= remove
                    print(name, "now has ", charisma, "charisma points.")
                    points += remove
                elif attribute == "I" or attribute == "i" and remove <= strength and remove > 1::
                    intelligence -= remove
                    print(name, "now has ", intelligence, "intelligence points.")
                    points += remove
                elif attribute == "A" or attribute == "a" and remove <= strength and remove > 1::
                    agility -= remove
                    print(name, "now has ", agility, "agility points.")
                    points += remove
                elif attribute == "L" or attribute == "l" and remove <= strength and remove > 1::
                    luck -= remove
                    print(name, "now has ", luck, "luck points.")
                    points += remove
                points += remove
            else:
                print("Invalid attribute. You are likely to be eaten by a Grue.")
        elif choice == "3":
            print("Strength: "), strength
            print("Perception: "), perception
            print("Endurance: "), endurance
            print("Charisma: "), charisma
            print("Intellignce: "), intellignce
            print("Agility: "), agility
            print("Luck: "), luck
        elif choice == "4":
            if points == 0:
                break
            else:
                print("Use all your points first!")
        else:
            print("Invalid Choice. You are likely to be eaten by a Grue.")
    print("Congrats. ", name, " is ready to face the wasteland of the Commonwealth. Good Luck!")
    