import random
target =random.randint(1,100)
while True:
    user_choice = int(input("guess the target or quit:"))
    if (user_choice == quit):
        print("better luck next time !")
    userchoice = int(user_choice)
    if (user_choice ==target ):
        print("succes,you won the game")
        break
    elif (user_choice < target):
        print("it is a small value,guess the target correctly")
    else:
        print("it is a larger value,guess the target correctly")
print('Game Over')
    

