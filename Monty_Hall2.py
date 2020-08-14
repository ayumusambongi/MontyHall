import random


def stay_switch(choice, opt):
    Goat = goat(choice, opt)
    print(f"Door {Goat + 1} is a Goat.\nWould you like to change doors? (y/n)")
    ss = input("Enter Here: ")
    if ss == "y" and opt[choice] != "Car":
        print("You Won a Car!")
    elif ss == "y" and opt[choice] == "Car":
        print("You Won a Goat!")
    elif ss == "n" and opt[choice] == "Car":
        print("You Won a Car!")
    elif ss == "n" and opt[choice] == "Car":
        print("You Wont a Goat!")


def goat(choice, opt):
    for i in range(len(opt)):
        if i != choice and opt[i] == "Goat":
            Goat = i
            del opt[i]
            break
    return Goat


def randomizing_door_options():
    opt = ["Car", "Goat", "Goat"]
    random.shuffle(opt)
    return opt


def main():
    opt = randomizing_door_options()
    while True:
        try:
            choice = int(input("Guess Which Door has the Car:\n1)Door 1\n2)Door 2\n3)Door 3\nEnter Here: ")) - 1
            if choice in range(len(opt)):
                stay_switch(choice, opt)
                break
            else:
                raise ValueError
        except ValueError:
            print("Oops! That door doesn't exist. Choose Again")


if __name__ == "__main__":
    sim_or_play = int(input("Options:\n1)Play\n2)Quit\nEnter Here: "))
    try:
        if sim_or_play == 1:
            main()
        elif sim_or_play == 2:
            print("Goodbye")
        else:
            raise ValueError
    except ValueError:
        print("invalid option")