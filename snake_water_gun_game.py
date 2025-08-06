def game(): 
    import random

    '''
    Choices:
    Snake = 1
    Water = -1
    Gun = 0
    '''
    choices = {1: "Snake", -1: "Water", 0: "Gun"}
    yourDict = {"s": 1, "w": -1, "g": 0}

    computer = random.choice([0, -1, 1])
    youstr = input("Enter Your Choice (s for snake, w for water, g for gun): ").lower()

    if youstr not in yourDict:
        print("Invalid input! Use 's', 'w', or 'g'.")
        return

    you = yourDict[youstr]

    print(f"You chose: {choices[you]}")
    print(f"Computer chose: {choices[computer]}")

    if computer == you:
        print("It's a draw.")
    elif computer == 1 and you == -1:
        print("You Lose! Snake drinks water.")
    elif computer == 1 and you == 0:
        print("You Win! Gun kills snake.")
    elif computer == -1 and you == 1:
        print("You Win! Snake drinks water.")
    elif computer == -1 and you == 0:
        print("You Lose! Water damages gun.")
    elif computer == 0 and you == 1:
        print("You Lose! Gun kills snake.")
    elif computer == 0 and you == -1:
        print("You Win! Water damages gun.")
    else:
        print("Something Went Wrong")

# Play multiple rounds
game()
game()
game()
game()
game()
game()
game()
game()
game()
game()
