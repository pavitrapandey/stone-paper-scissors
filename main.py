import random

while True:
    youStr = input('''Enter Your Choice 
for Stone  press 1
for Paper  press 2
for Scissor press 3\n''')

    youDict = {"1": 1, "3": -1, "2": 0}
    reverseDict = {1: "Stone", -1: "Scissor", 0: "Paper"}
    computerStr = random.choice(list(youDict.keys()))
    computer = youDict[computerStr]
    you = youDict[youStr]
    print(f"You Chose {reverseDict[you]}\nComputer Chose {reverseDict[computer]}")

    if computer == you:
        print("IT's a DRAW")
    else:
        if computer == -1 and you == 1:
            print("YOU WIN!!!")
        elif computer == -1 and you == 0:
            print("COMPUTER WINS!!!")
        elif computer == 0 and you == 1:
            print("COMPUTER WINS!!!")
        elif computer == 1 and you == -1:
            print("COMPUTER WINS!!!")
        elif computer == 1 and you == 0:
            print("YOU WIN!!!")
        elif computer == 0 and you == -1:
            print("YOU WIN!!!")
        else:
            print("Something went wrong")



    play_again = input("Do you want to play again? press Y for yes/N for no: ").lower()
    if play_again != "y":
        break

print("Thanks for playing!")
