"""Create a Character Generator for Fallout 4."""

# print("You awake from 200 years in deep freeze. The wasteland awaits you.")
# name = input("What's your name? ")
# gender = input("What's your gender? ")
# points = 21
# attributes = ("Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck")
# strength = 1
# perception = 1
# endurance = 1
# charisma = 1
# intelligence = 1
# agility = 1
# luck = 1

# while True:
#     print
#     print("You have ", points, "points left.")
#     print(
#         """
#         1 - add points
#         2 - remove points
#         3 - see points per attribute
#         4 - exit
#         """)

    # choice = input("choice: ").upper()
    # if choice == "1":
    #     attribute = input("which attribute? S. P. E. C. I. A. L.?")
    #     if attribute in attributes:
    #         add = int(input("How many points? "))
    #         if add <= points and add > 0:
    #             if attribute == "S" or attribute == "s":
    #                 strength += add
    #                 print(name, "now has ", strength, "strength points.")
    #             elif attribute == "P":
    #                 perception += add
    #                 print(name, "now has ", perception, "perception points.")
    #             elif attribute == "E":
    #                 endurance += add
    #                 print(name, "now has ", endurance, "endurance points.")
    #             elif attribute == "C":
    #                 charisma += add
    #                 print(name, "now has ", charisma, "charisma points.")
    #             elif attribute == "I":
    #                 intelligence += add
    #                 print(name, "now has ", intelligence, "intelligence points.")
    #             elif attribute == "A":
    #                 agility += add
    #                 print(name, "now has ", agility, "agility points.")
    #             elif attribute == "L":
    #                 luck += add
    #                 print(name, "now has ", luck, "luck points.")
    #             points -= add
    #         else:
    #             print("Invalid attribute. You are likely to be eaten by a Grue.")
    #     elif choice == "2":
    #         if attribute in attributes:
    #             remove = int(input("How many points? "))
    #             # if remove <= points and remove > 0:
    #             if attribute == "S" or attribute == "s" and remove <= strength and remove > 1:
    #                 strength -= remove
    #                 print(name, "now has ", strength, "strength points.")
    #                 points += remove
    #             elif attribute == "P" and remove <= strength and remove > 1:
    #                 perception -= remove
    #                 print(name, "now has ", perception, "perception points.")
    #                 points += remove
    #             elif attribute == "E" and remove <= strength and remove > 1:
    #                 endurance -= remove
    #                 print(name, "now has ", endurance, "endurance points.")
    #                 points += remove
    #             elif attribute == "C" and remove <= strength and remove > 1:
    #                 charisma -= remove
    #                 print(name, "now has ", charisma, "charisma points.")
    #                 points += remove
    #             elif attribute == "I" and remove <= strength and remove > 1:
    #                 intelligence -= remove
    #                 print(name, "now has ", intelligence, "intelligence points.")
    #                 points += remove
    #             elif attribute == "A" and remove <= strength and remove > 1:
    #                 agility -= remove
    #                 print(name, "now has ", agility, "agility points.")
    #                 points += remove
    #             elif attribute == "L" and remove <= strength and remove > 1:
    #                 luck -= remove
    #                 print(name, "now has ", luck, "luck points.")
    #                 points += remove
    #             points += remove
    #         else:
    #             print("Invalid attribute. You are likely to be eaten by a Grue.")
    #     elif choice == "3":
            # print("Strength: "), strength
            # print("Perception: "), perception
            # print("Endurance: "), endurance
            # print("Charisma: "), charisma
            # print("Intellignce: "), intelligence
            # print("Agility: "), agility
            # print("Luck: "), luck


def create_character():
    """Set up the character creation method."""
    attribute = input("\nwhich attribute? S. P. E. C. I. A. L.?").upper()

    if attribute in my_character.keys():
        amount = int(input("By how much?"))

        if (amount > my_character['points']) or (my_character['points'] <= 1):
            print("Not enough points!")
        else:
            my_character[attribute] += amount
            my_character['points'] -= amount
    else:
        print("\nThat attribute doesn't exist!\n")


def print_character():
    """Display the character stats for the user."""
    for attribute in my_character.keys():
        print(attribute, " : ", my_character[attribute])

# MAIN FUNCTION

my_character = {'name': '', 'S': 1, 'P': 1, 'E': 1, 'C': 1, 'I': 1, 'A': 1, 'L': 1, 'points': 21}
running = True

print("You awake from 200 years in deep freeze. The wasteland awaits you.")

my_character['name'] = input("What is your character's name? ")

while running:
    print("\nYou have ", my_character['points'], " points to distribute amongst your S.P.E.C.I.A.L. attributes.\n")
    print("1. Add points\n2. Remove points\n3. See current attributes\n4. Exit\n")

    choice = input("Choose wisely:")

    if choice == "1":
        add_character_points()
    elif choice == "2":
        remove_character_points()
    elif choice == "3":
        print_character()
    elif choice == "4":
        if points > 0:
            print("Use all your points first!")
        else:
            running = False
    else:
        pass
