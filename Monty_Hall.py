import random


def stay_switch(first_choice, new_opt):
    for _ in range(len(new_opt)):
        if first_choice[1] == "Car":
            return "stay"
        else:
            return "switch"


def remove_goat(first_choice, opt):
    for key in opt:
        if key == first_choice[0]:
            continue
        elif opt[key] == "Goat":
            del opt[key]
            break
    return opt


def randomizing_door_options():
    doors = ["Door 1", "Door 2", "Door 3"]
    d_options = ["Car", "Goat", "Goat"]
    random.shuffle(d_options)
    opt = {doors[i] : d_options[i] for i in range(len(doors))}
    return opt


def cpu_sim():
    stay, switch = 0, 0
    reps = 1000
    for _ in range(reps):
        opt = randomizing_door_options()
        first_choice = random.choice(list(opt.items()))
        new_opt = remove_goat(first_choice, opt)
        winner = stay_switch(first_choice, new_opt)
        if winner == "stay":
            stay += 1
        elif winner == "switch":
            switch += 1
    print("Stay:", stay, "wins\nSwitch:", switch, "wins")
    

def main():
    cpu_sim()
"""    sim_or_play = int(input("Options:\n1)Play\n2)Cpu Simulation\nEnter Here: "))
    try:
        if sim_or_play == 1:
            player()
        elif sim_or_play == 2:
            cpu_sim()
        else:
            raise ValueError
    except ValueError:
        print("invalid option")
"""    

if __name__ == "__main__":
    main()
        