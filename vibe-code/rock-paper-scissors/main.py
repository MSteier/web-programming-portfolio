import random

while True:
    
    # user picks move
    user_choice = input("Select the number that corresponds with your choice, (1) Rock, (2) Paper, (3) Scissors, (0) Quit: ")
    
    if user_choice == '0':
        print("Thanks for playing! Goodbye!")
        break

    if user_choice not in ['1', '2', '3']:
        print("Invalid input. Please select 1, 2, 3, or 0 to quit.")
        continue

    user_choice = int(user_choice)
    if user_choice == 1:
        print("You picked Rock!")
    elif user_choice == 2:
        print("You picked Paper")
    elif user_choice == 3:
        print("You picked Scissors")

    # The computer picks move
    computer_choice = random.randint(1, 3)
    print("The computer chose:", computer_choice)

    if computer_choice == 1:
        print("The Computer picked Rock!")
    elif computer_choice == 2:
        print("The Computer picked Paper")
    elif computer_choice == 3:
        print("The Computer picked Scissors")

    # determine the winner
    if user_choice == computer_choice:
        print("It's a Tie!")
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 3 and computer_choice == 2) or (user_choice == 2 and computer_choice == 1):
        print("You Win!")
    
    else:
        print("Computer Wins!")
       
