import random as ran

my_choices = ["rock", "paper", "scissors"]

print("\nWelcome to the Rock, Paper, Scissor game. Created by CODEWITHJAGADISH")
print("----------------------------------------------------------------------")
while 1:
    players_choice = input("Enter your choice (rock/paper/scissors), or 'q' to quit: ").lower()
    print("----------------------------------------------------------------")
    if players_choice == 'q':
        print("Quitting game...")
        break
    elif players_choice not in my_choices:
        print("Invalid input. Please select from given choices only\n")
        print("----------------------------------------------------------------")
        continue

    computers_choice = ran.choice(my_choices)

    print("Your Turn")
    print("Your choice is: ", players_choice)
    print('-------------------')
    print("Computers Turn")
    print("Computers choice is: ", computers_choice)

    if players_choice == computers_choice:
        print('-------------------')
        print("-> Tie")
    elif players_choice == "rock":
        if computers_choice == "paper":
            print('-------------------')
            print("-> Computer Win")
        else:
            print('-------------------')
            print("-> You Win")
    elif players_choice == "paper":
        if computers_choice == "scissors":
            print('-------------------')
            print("-> Computer Win")
        else:
            print('-------------------')
            print("-> You Win")
    else:
        if computers_choice == "rock":
            print('-------------------')
            print("-> Computer Win")
        else:
            print('-------------------')
            print("-> You Win")

print("Thanks for playing")
print("Visit again to our website...")
