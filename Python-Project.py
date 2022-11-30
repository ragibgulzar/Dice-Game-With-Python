import random

score=0
print("_______________________\n")
print("Welcome To Dice Game🎲")
print("_______________________\n")
while True:
    guess_number=int(input(">>>Enter Your Guess 🤔:  "))
    random_number=random.randint(1,6)                        
    if 1<=guess_number<=6:                                  
        if guess_number==random_number:
            print("\nRolling 🎲...")
            print(f'🎲 = {random_number}')
            print("Congratulations You won!!! \n")
            print("------------------------")
            print("For Exit --->Type 0")
            score+=1
        else:
            print("\nRolling 🎲...")
            print(f'🎲 = {random_number}')
            print("You Lost but don't give up keep trying!\n")
            print("------------------------")
            print("For Exit --->Type 0")
    elif guess_number==0:
        print("                         ")
        print("_______________________\n")
        print("-------> Your Score is",score)
        print("_______________________\n")
        break
    else:
        print("_______________________\n")
        print("                         ")
        print("Enter a valid number from 1 to 6")
        print("                         ")
        print("_______________________\n")
        continue
