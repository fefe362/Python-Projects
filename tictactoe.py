import random

print("Welcome to Tic Tac Toe!")
print("You will play against the computer.")
print("Whoever manages to fill in a row, column or diagonal of the grid with the same symbol wins!")

print("You need to choose a position on the grid to mark your move, according to the numbering, see the grid: ")
print("_ _ _")
print("_ _ _")
print("_ _ _")

print("Choose a number from 1 to 9 for your move, according to the grid below: ")
print("1 2 3")
print("4 5 6")
print("7 8 9")

def print_grid(grid): #shows the current state of the grid using the for loop, in the range where the list starts (at 0) and ends (at 9)
    print("the grid status is\n")
    for index in range(len(grid)):  
        print(grid[index], end=" ")
        if index == 2 or index == 5 or index == 8:
            print("")
        
def check_grid(grid, player): #shows all the winning and drawing possibilities of the game
    #testing lines
    if grid[0] == player and grid[1] == player and grid[2] == player:
        if player == "X":
            return 1
        else:
            return 2
    if grid[3] == player and grid[4] == player and grid[5] == player:
        if player == "X":
            return 1
        else:
            return 2
    if grid[6] == player and grid[7] == player and grid[8] == player:
        if player == "X":
            return 1
        else:
            return 2
    
    #testing columns
    if grid[0] == player and grid[3] == player and grid[6] == player:
        if player == "X":
            return 1
        else:
            return 2
    if grid[1] == player and grid[4] == player and grid[7] == player:
        if player == "X":
            return 1
        else:
            return 2
    if grid[2] == player and grid[5] == player and grid[8] == player:
        if player == "X":
            return 1
        else:
            return 2
    
    #testing diagonals
    if grid[0] == player and grid[4] == player and grid[8] == player:
        if player == "X":
            return 1
        else:
            return 2
    if grid[2] == player and grid[4] == player and grid[6] == player:
        if player == "X":
            return 1
        else:
            return 2
    
    return 0

quantity_choices = 0


grid = ["_"] * 9

while True:

    choise = int(input("What is your choise? "))  #transformation of the position "_" into an integer to be used as an index in the grid list

    while grid[choise-1] != "_":  #position in list other than integer
        print("Your choice was invalid!")
        print_grid(grid)
        choise = int(input("What is your choise? "))

    grid[choise-1] = "X"
    quantity_choices += 1 #counting the number of choices is necessary to end the while loop in case of old

    winner = check_grid(grid, "X")

    if winner != 0: #someone won 
        break
    
    if quantity_choices == 9: #old case
        break

    print_grid(grid)

    choise_computer = random.randint(1, 9)

    while grid[choise_computer-1] != "_":
        choise_computer = random.randint(1, 9)

    grid[choise_computer-1] = "O" 
    quantity_choices += 1

    winner = check_grid(grid, "O")

    if winner != 0:  #someone won
        break
    print_grid(grid)

if winner == 1:
    print("Congratulations, you won!")
elif winner == 2:
    print("You lost. The computer won.")
else:
    print("It got old, nobody won.")

print_grid(grid)