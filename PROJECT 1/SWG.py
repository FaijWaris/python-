'''\
1 for snake 
-1 for water 
0 for gun
    '''
import random


def swg():
    you = int(input("Enter your choice (1 for snake, -1 for water, 0 for gun): "))
    computer = random.choice([1, -1, 0])
    print("Computer's choice:", computer)

    if you == computer:
        print("It's a tie!")
    elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
        print("You win!")
    else:
        print("You lose!")

# Run the function
swg()
