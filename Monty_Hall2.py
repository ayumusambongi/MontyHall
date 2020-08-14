import random


def question(opt, message):
    invalid = ["Ugh. That wasn't an option.", "Oops, something went wrong :(", "Sorry, can't do that ̄ \_(ツ)_/̄ ", "Please enter a valid option."]
    while True:
        print(message)
        choice = input("Enter Here: ")
        if choice in opt:
            return choice
        print(random.choice(invalid))


def find_goat(choice, doors):
    for i in range(len(doors)):
        if i != choice and doors[i] == "Goat":
            return i


def stay_switch(choice, doors):
    goat = find_goat(choice, doors)
    opt = ["y", "n"]
    switch = question(opt, f"Door {goat + 1} is a Goat.\nWould you like to change doors? y/n")
    for i in range(len(doors)):
        if i != goat and i != choice:
            not_selected = i
            break
    if switch == "y":
        return not_selected
    else:
        return choice


def randomizing_door_options():
    doors = ["Car", "Goat", "Goat"]
    random.shuffle(doors)
    return doors


def main():
    doors = randomizing_door_options()
    opt = ["1", "2", "3"]
    choice = int(question(opt, "Guess Which Door has the Car:\n1)Door 1\n2)Door 2\n3)Door 3")) - 1
    final_answer = stay_switch(choice, doors)
    if doors[final_answer] == "Car":
        print("Win")
    else:
        print("Lose")
    print(doors)


if __name__ == "__main__":
    opt = ["1", "2"]
    choice = int(question(opt, "Options:\n1)Play\n2)Quit"))
    if choice == 1:
        main()
    elif choice == 2:
        print("Goodbye")
