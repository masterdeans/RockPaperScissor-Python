import random

user1 = input("1st Player Name: ")
user2 = input("Computer Name: ")

u1_count = 0
int(u1_count)
u2_count = 0
int(u2_count)

ScoreRange = int(input("Enter Range Score: "))

print("===========================")
print("Rock, Paper, Scissors!")
print("Let the battle begin! \n ", user1, " vs ", user2, "!")
print(user1, " Score: ",u1_count, " : ",user2," Score: ",u2_count,"")

while (True):
    
    print("===========================")
    print("Choose")
    print("1. Rock")
    print("2. Scissors")
    print("3. Paper")

    RPSarray = {'1': 1, '2': 2, '3': 3}
    p1_choose = str(input("Player 1 choose: "))
    p1 = RPSarray.get(p1_choose)

    rand = random.randint(1,3)
    
    print(user2,": ", rand)
    if rand == p1:
        print("draw!")
        print(user1, " Score: ",u1_count, " : ",user2," Score: ",u2_count,"")
        
    if rand == 2 and p1 == 1 or p1 == 3 and rand == 1 or p1 == 3 and rand == 2:
        print(user1, " wins!")
        u1_count = u1_count + 1
        print(user1, " Score: ",u1_count, " : ",user2," Score: ",u2_count,"")
        if u1_count == ScoreRange or u2_count == ScoreRange:
            print("===========================")
            print("Final Score: Player 1: ",user1," = ", u1_count, " : Player 2: ",user2, " = ", u2_count,"")
            print("Congratulations, " ,user1,"!")
            
            if str(input("Do you want to Continue?: [y] Yes [n] No: ")) == "y":
                ScoreRange = int(input("Enter Range Score: "))
                u1_count = 0
                u2_count = 0
                continue
            else:
                print("Game Over!")
                break
        else:
            continue
            
    if rand == 1 and p1 == 2 or p1 == 1 and rand == 3 or rand == 3 and p1 == 2:
        print(user2 , "wins!")
        u2_count = u2_count + 1
        print(user1, " Score: ",u1_count, " : ",user2," Score: ",u2_count,"")
        
        if u1_count == ScoreRange or u2_count == ScoreRange:
            print("===========================")
            print("Final Score: Player 1: ",user1," = ", u1_count, " : Player 2: ",user2, " = ", u2_count,"")
            print("Congratulations, " ,user2,"!")
            
            if str(input("Do you want to Continue?: [y] Yes [n] No: ")) == "y":
                ScoreRange = int(input("Enter Range Score: "))
                u1_count = 0
                u2_count = 0
                continue
            else:
                print("Game Over!")
                break
        else:
            continue

        
        
    

    

