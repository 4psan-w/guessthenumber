import random as r

def level_checker():
    print("Choose the game difficulty: \n")
    print("Easier (not very fun)")
    print("Easy")
    print("Medium")
    print("Hard")
    print("Advanced")
    level=input("Choose the Level of the game\n>>")
    if(level.capitalize()=='Easier'):
        print("Choose a number between 1 to 5")
        return 5;
    elif(level.capitalize()=='Easy'):
        print("Choose a Number between 1 to 10")
        return 10
    elif(level.capitalize()=='Medium'):
        print("Choose a Number between 1 to 20")
        return 20
    elif(level.capitalize()=='Hard'):
        print("Choose a Number between 1 to 30")
        return 30
    elif(level.capitalize()=='Advanced'):
        conf=input("Are You sure: ?")
        if(conf.capitalize()=='Yes'):
            print("Choose a Number between 1 to 100")
            return 100
        else: exit()

def user_input():
    x=int(input("Guess the Number : \n>>"))
    return x

def game_frame():
    min=1
    max=level_checker()
    rand_num=r.randint(min,max)
    ui_num=user_input()
    if(max==5 and ui_num>5):
        print("You guessed more than 5")
    if(max==10 and ui_num>10):
        print("You guessed More than 10 for EASY level")
        print("Please try again later")
        exit()
    elif(max==10 and ui_num>20):
        print("You guessed More than 20 for MEDIUM level")
        print("Please try again later")
        exit()
    elif(max==30 and ui_num>30):
        print("You guessed More than 30 for HARD level")
        print("Please try again later")
        exit()
    elif(max==10 and ui_num>100):
        print("You guessed More than 10 for ADVANCED level")
        print("Please try again later")
        exit()

    if(ui_num==rand_num):
        print(f"Correct Answer{rand_num}")
        print(f"You Guessed{ui_num}")
        print("You Guessed the Number correctly!!")
    else:
        print(f"Correct Answer{rand_num}")
        print(f"You Guessed{ui_num}")
        print("You got it wrong Try again Later")
        retry=input("type Again to play again:\n>>")
        if(retry.capitalize()=='Again'):
            game_frame()
        else:
            exit()
print("____________________________")
print("**GUESS THE NUMBER GAME**")
print("\n\n")
game_frame()

