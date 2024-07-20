import random
while(exit!='q'):
 print("Enter Your Choice:")
 print("0 for Rock")
 print("1 for paper")
 print("2 for Scissors")
 user_choice = int(input())

 if user_choice > 2 or user_choice < 0:
    print("You Have Entered Invalid Choices")
    
 computer_choice = random.randint(0,2)
 print("computer chose:",computer_choice)

 if(computer_choice == user_choice):
    print("It's a draw")
    exit=input("to exit plz enter 'q'")

 elif computer_choice == 0 and user_choice == 2:
    print("You Lose")
    exit=input("to exit plz enter 'q'")

 elif computer_choice == 2 and user_choice == 0:
    print("you win")
    exit=input("to exit plz enter 'q'")

 elif computer_choice > user_choice:
    print("You Lose")
    exit=input("to exit plz enter 'q'")

 elif computer_choice < user_choice:
    print("You Win")
    exit=input("to exit plz enter 'q'")
    
