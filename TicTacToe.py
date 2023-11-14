import random
import math
counter = 9
winner = None
location = {1: " ", 2: " ", 3: " ",
            4: " ", 5: " ", 6: " ",
            7: " ", 8: " ", 9: " "}
cases = [0,1,2,3]


def preboard():
    for x in location:
        print("|" + str(x), end="")
        if x % 3 == 0:
            print("|\n", end="")

def board():
    for x in location:
        print("|" + location[x], end="")
        if x % 3 == 0:
            print("|\n",end="")

class Player:
    def __init__(self, letter):
         self.letter = letter

    def turn(self):
        self.loc = 0
        flag = False
        while self.loc == 0 or flag == False :
            self.loc = int(input("Enter the location"))
            if location[self.loc] == " ":
                location[self.loc] = self.letter
                flag = True
            elif location[self.loc] == "X" or location[self.loc] == "O":
                print("Choose a different location")
        board()

    def check_winner(self, winner = None):
        row_index = int(self.loc) % 3
        if row_index == 0: row_index = 3
        row = [row_index, (row_index + 3), (row_index + 6)]
        col_index = math.ceil(self.loc / 3)
        col = [(col_index * 3), (col_index * 3) - 1, (col_index * 3) - 2]
        if (all(location[x] == self.letter for x in row)):
            winner = True
        elif(all(location[x] == self.letter for x in col)):
            winner = True
        elif self.loc % 2 == 1:
            if (location[1]==self.letter) and (location[5]==self.letter) and (location[9]==self.letter):
                winner = True
            elif (location[7]==self.letter) and (location[5]==self.letter) and (location[3]==self.letter):
                winner = True
        return winner

class RandComp:
    def __init__(self,letter):
        self.letter = letter
    def turn(self):
        self.loc = 0
        flag = False
        while self.loc == 0 or flag == False:
            self.loc = random.randint(1,9)
            if location[self.loc] == " ":
                location[self.loc] = self.letter
                flag = True
            elif location[self.loc] == "O":
                flag == False
        board()

    def check_winner(self,winner = None):
        row_index = self.loc % 3
        if row_index == 0:row_index = 3
        row = {row_index, row_index + 3, row_index + 6}
        col_index = math.ceil(self.loc / 3)
        col = {(col_index * 3), (col_index * 3) - 1, (col_index * 3) - 2}
        if (all(location[x] == self.letter for x in row)):
            winner = False
        elif (all(location[x] == self.letter for x in col)):
            winner = False
        elif self.loc % 2 == 1:
            if (location[1] == self.letter) and (location[5] == self.letter) and (location[9] == self.letter):
                winner = False
            elif (location[7] == self.letter) and (location[5] == self.letter) and (location[3] == self.letter):
                winner = False
        return winner

class SmartComp:#error in turn
    def __init__(self,letter):
        self.letter = letter #0 for lose, 1 for draw and 3 for win
    def check_winner(self, winner=None):
        row_index = self.loc % 3#make changes
        if row_index == 0: row_index = 3
        row = {row_index, row_index + 3, row_index + 6}
        col_index = math.ceil(self.loc / 3)#make changes
        col = {(col_index * 3), (col_index * 3) - 1, (col_index * 3) - 2}
        if (all(location[x] == self.letter for x in row)):
            winner = False
        elif (all(location[x] == self.letter for x in col)):
            winner = False
        elif self.loc % 2 == 1:
            if (location[1] == self.letter) and (location[5] == self.letter) and (location[9] == self.letter):
                winner = False
            elif (location[7] == self.letter) and (location[5] == self.letter) and (location[3] == self.letter):
                winner = False
        return winner
    def store(self,x,max):
        #create a dictionary and store max values for specific x's and then choose the x with max MAX value
        if max>cases[1]:
            cases.append(x)
            cases.append(max)
        elif max == cases[1] :
            cases.append(x)
            cases.append(max)
    def choose(self):
        if len(cases)>2 :
            x=cases[random.choice([0,2])]
        else:
            x=cases[0]
        return x
    def check_winner_opp(self,winner = None):
        row_index = int(self.loc) % 3
        if row_index == 0: row_index = 3
        row = [row_index, (row_index + 3), (row_index + 6)]
        col_index = math.ceil(self.loc / 3)
        col = [(col_index * 3), (col_index * 3) - 1, (col_index * 3) - 2]
        if (all(location[x] == self.letter for x in row)):
            winner = True
        elif (all(location[x] == self.letter for x in col)):
            winner = True
        elif self.loc % 2 == 1:
            if (location[1] == self.letter) and (location[5] == self.letter) and (location[9] == self.letter):
                winner = True
            elif (location[7] == self.letter) and (location[5] == self.letter) and (location[3] == self.letter):
                winner = True
        return winner

    def turn(self,max=0,winner=None):
        for self.loc in range(1,10):
            winner=self.check_winner()
            if winner == False:
                max += 3
            elif winner == None:
                max += 1
            for y in range(1,10):
                winner = self.check_winner_opp()
                if winner == True:
                    max -= 3
                elif winner == None:
                    max -= 1
                for z in range(1,10):
                    winner = self.check_winner()
                    if winner == False:
                        max += 3
                    elif winner == None:
                        max += 1
                    self.store(self.loc,max)#yet to be made
        self.loc=self.choose()#choose the max vakue of max from store
        #now we have the best move in memory just have to input it
        location[self.loc] = "O"
        board()

# main start of the game
type_of_game = input("A)SINGLE PLAYER\nB)2 PLAYER GAME")
if type_of_game == 'a' or type_of_game == 'A':
    difficulty = input("A)EASY\nB)HARD")
    preboard()
    if difficulty == 'A' or difficulty == 'a':
        # user vs random computer
        # user starts
        player1 = Player("X")
        player2 = RandComp("O")
        while winner == None and counter != 0:
            player1.turn()
            counter -= 1
            winner = player1.check_winner()
            if winner == True:
                print("Congratulations you won!!")
            elif winner == None and counter != 0:
                player2.turn()
                counter -= 1
                winner = player2.check_winner()
            if winner == False:
                print("Hehehe you lose!;)")
        if winner == None:
            print("It\'s a tie")
    elif difficulty == 'B' or difficulty == 'b':
        #user vs smart computer
        # user starts
        player1 = Player("X")
        player2 = SmartComp("O")
        while winner == None and counter != 0:
            player1.turn()
            counter -= 1
            winner = player1.check_winner()
            if winner == True:
                print("Congratulations you won!!")
            elif winner == None and counter != 0:
                player2.turn()
                counter -= 1
                winner = player2.check_winner()
            if winner == False:
                print("Hehehe you lose!;)")
        if winner == None:
            print("It\'s a tie")
    else:
        print("wrong input")

elif type_of_game == 'B' or type_of_game == 'b':
    #user1 vs user2
    #user 1 starts
    preboard()
    player1 = Player("X")
    player2 = Player("O")
    while winner == None and counter != 0:
        player1.turn()
        counter -= 1
        winner = player1.check_winner()
        if winner == True:
            print(f"Congratulations {player1.letter} won!!")
        if winner == None and counter != 0:
            player2.turn()
            counter -= 1
            winner = player2.check_winner()
            if winner == True:
                print(f"Congratulations {player2.letter} won!!")
else:
    print("wrong input")