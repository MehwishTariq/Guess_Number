 #import random library to use random function
import random as rd

#user_defined function to return the random number
def pc_no():
    return str(rd.randrange(0,10))  #built_in random function in random library

#function that takes user guess
def user_no():
    print("Guess the number: ")
    return input()

#function for the main play
def play():
    i=0
    pcNo=pc_no()
    print(pcNo) #can be cut as to not show the random number
    
    while (i<3): #number of guesses a user can do 
        userNo=user_no()
    #conditions checking the user guess with PC guess    
        if userNo < pcNo:
            print("The number is too low!")
        elif userNo > pcNo:
            print("The number is too large!")
        elif userNo == pcNo:
            print("Congratulations you guessed it right!")   
            play_again()
            
        i=i+1  
        #condition to play the game again after winning or losing 
        if i==3 and userNo!=pcNo:
             print("\nYou lose! :( ")
             play_again()
          
#user_defined function for the play again condition
def play_again():
    print("\n Do you want to play again? write 'y' or 'n'")   
    ans=input()
    if ans=='Y' or ans=='y':
        play()
    elif ans=='n' or ans=='N':
        print("GoodBye!") 
#only one calling of function    
play()