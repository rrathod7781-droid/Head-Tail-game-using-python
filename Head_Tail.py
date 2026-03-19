#Creating Head-Tails game
import random as r

class game: 
    list1 = ["head", "tail"]
    def  choose(self):
        self.user1 = input("Enter your choice (Head/Tail): ").lower() 
        if(self.user1 == "head"):
            self.user2 = "tail"
        elif(self.user1 == "tail"):
            self.user2 = "head"
        else:
            print("Plz enter valid input (Head/Tail)")
            return self.choose()
    def playing(self):
        self.computer = r.choice(self.list1) 
        print("Tossing the coin...") 
        print("It is : ", self.computer) 
        if (self.user1 == self.computer):
            print("User1 wins❤️")
            return 1
        elif(self.user2 == self.computer):
            print("User2 wins🎉") 
            return 2

games = [] #Here,I created a empty list to store the game objects
user1_score = 0
user2_score = 0
rounds = int(input("Enter how many rounds you want to play: "))
for i in range(1, rounds+1):
    print(f"\nRound {i}")

    g = game()
    g.choose()
    count = g.playing()
    games.append(g)

    if (count == 1):
        user1_score += 1
    elif (count == 2):
        user2_score += 1
    print(f"Score: User1 {user1_score} \nUser2 {user2_score}")

if (user1_score > user2_score):
    print("\nUser1 wins the game!🏆🎉")
elif (user2_score > user1_score):
    print("User2 wins the game!🏆🎉")
else:
    print("\nIt's a tie!🤝")