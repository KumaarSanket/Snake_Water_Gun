import random
'''
1 for snake
-1 for water
0 for gun
'''

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s":1 , "w":-1 , "g":0}
you = youDict[youstr]

if (computer == you):
    print("It's a DRAW")

else:
    if (computer == -1 and you ==1):
        print("Computer chose water. You win!")

    elif (computer ==-1 and you ==0):
        print("Computer chose water. You lose!")

    elif (computer ==1 and you ==-1):
        print("Computer chose snake. You win!")
    elif (computer ==1 and you ==0):
        print("Computer chose snake. You lose!")

    elif (computer ==0 and you ==-1):
        print("Computer chose gun. You win!")
    elif (computer ==0 and you ==1):
        print("Computer chose gun. You lose!")

    else:
        print("Something went wrong!")