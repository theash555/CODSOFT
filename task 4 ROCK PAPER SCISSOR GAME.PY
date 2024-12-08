import random
print('WELCOME TO ROCK-SCISSOR-PAPER')
print("Enter \n 1 for ROCK \n 2 for SCISSOR \n 3 for PAPER")

1 == "ROCK"
2 == "SCISSOR"
3 == "PAPER"
def game(score, comp):
    
    Your_choice = int(input("Enter your choice:"))  

    Computer_choice = random.choice([1,2,3])

    print(f"Your choice is {Your_choice} and Compuer's choice is {Computer_choice}")

    if(Your_choice == 1 and Computer_choice == 2):
        print(" YOU WIN")
        score= score+1
        return int(score) , int(comp)

    elif(Your_choice == 1 and Computer_choice == 1):
        print("GAME DRAW")
        return int(score) , int(comp)

    elif(Your_choice == 1 and Computer_choice == 3):
        print("YOU LOOSE")
        comp+=1
        return int(score) , int(comp)

    elif(Your_choice == 2 and Computer_choice == 1):
        print("YOU LOOSE")
        comp+=1
        return int(score) , int(comp)

    elif(Your_choice == 2 and Computer_choice == 2):
        print("GAME DRAW")
        return int(score) , int(comp)

    elif(Your_choice == 2 and Computer_choice == 3):
        print("YOU WIN")
        score+=1
        return int(score) , int(comp)

    elif(Your_choice == 3 and Computer_choice == 1):
        print("YOU WIN")
        score+=1
        return int(score) , int(comp)

    elif(Your_choice == 3 and Computer_choice == 2):
        print("YOU LOOSE")
        comp+=1
        return int(score) , int(comp)

    elif(Your_choice == 3 and Computer_choice == 3):
        print("GAME DRAW")
        return int(score) , int(comp)

    else:
        print("Enter Valid Number.")

play= True
score=0
comp=0
while play==True:
    score, comp= game(score=score, comp=comp)
    
    choice= int(input(f"Do you want to continue\n  1 for Continue \n 2 for exit"))
    if choice== 1:
        score, comp= game(score=score, comp=comp)
    else:
        print(f"Total Score: {score}, computer score: {comp}")
        break