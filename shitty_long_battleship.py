from random import randint

# This is the multiple square per ship version, where you play against a computer #
# The computer is a moron and only chooses randomly, though #
# Also, this version only has one ship #
##### Functions up here #####

# Prints the board.
def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board)-1)

def random_col(board):
    return randint(0, len(board[0])-1)

def check_board_position(board,board_size,ship_coordinates):
    row = ship_coordinates[0]
    col = ship_coordinates[1]
    if (row not in range(0,board_size)) or (col not in range(0,board_size)):
        position = "offboard"
    elif board[row][col] == "X":
        position = "hit"
    elif board[row][col] == "O":
        position = "miss"
    else:
        position = "good"
    return position

def look_left(coordinates):
    new_row = coordinates[0]
    new_col = coordinates[1] - 1
    new_coordinates = [new_row, new_col]
    return new_coordinates

def look_right(coordinates):
    new_coordinates = [coordinates[0], (coordinates[1] + 1)]
    return new_coordinates

def look_up(coordinates):
    new_coordinates = [coordinates[0] - 1, (coordinates[1])]
    return new_coordinates

def look_down(coordinates):
    new_coordinates = [coordinates[0] + 1, (coordinates[1])]
    return new_coordinates    

def computers_guess(board):
    while True:
	guess_row = random_row(board)
	guess_col = random_col(board)
	if board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "O":
	    continue 
	else:
	    break
    row_col = [guess_row, guess_col]
    return row_col

def computers_find(board,board_size,ship_coordinates):
    while True:
        print "ship length is " + str(len(ship_coordinates))
        if len(ship_coordinates) == 1:  
            direction = randint(0,3)
            if direction == 0: #Look Left
                new_coordinates = look_left(ship_coordinates[0])
            elif direction == 1: #Look Right
                new_coordinates = look_right(ship_coordinates[0])
            elif direction == 2: #Look Up
                new_coordinates = look_up(ship_coordinates[0])
            else: #Look Down
                new_coordinates = look_down(ship_coordinates[0])
            check = check_board_position(board, board_size,new_coordinates)        
            if check == "good":
                return new_coordinates
            else: 
                continue
        elif (ship_coordinates[0][0] == ship_coordinates[1][0]):
            x = 0
            end = False
            new_coordinates = look_left(ship_coordinates[-1])
            while (x < 20):
                check = check_board_position(board, board_size,new_coordinates)
                if check == "miss":
                    new_coordinates = look_right(new_coordinates)
                    end = True
                elif check == "offboard":
                    new_coordinates = look_right(new_coordinates)
                elif check == "hit":
                    if end == False:
                        new_coordinates = look_left(new_coordinates)
                    else:
                        new_coordinates = look_right(new_coordinates)
                elif check == "good":
                    return new_coordinates
                else:
                    print "check is:"
                    print check
                    print new_coordinates
                    help = raw_input("what do you want to do?")
                    return new_coordinates
                x = x + 1
        elif (ship_coordinates[0][1] == ship_coordinates[1][1]):
            x = 0
            end = False
            new_coordinates = look_up(ship_coordinates[-1])
            while (x < 20):
                check = check_board_position(board,board_size,new_coordinates)
                if check == "miss":
                    new_coordinates = look_down(new_coordinates)
                    end = True
                elif check == "offboard":
                    new_coordinates = look_down(new_coordinates)
                elif check == "hit":
                    if end == False:
                        new_coordinates = look_up(new_coordinates)
                    else:
                        new_coordinates = look_down(new_coordinates)
                elif check == "good":
                    return new_coordinates
                x = x + 1
        elif (x >= 20):
            print ("Something's Wrong")
            return new_coordinates
        else:
            print ("Everything's Wrong")
            print ("Ship Length is " + str(len(ship_coordinates)))
            print "Ship Coordinates:"
            print ship_coordinates
            print ship_coordinates[0][0]
            print ship_coordinates[0][1]
            print ship_coordinates[1][0]
            print ship_coordinates[1][1]
            return new_coordinates

def get_board_row(size):
    while True:
        try:
            choice = int(raw_input("Choose a Row:"))-1
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
            #Gave a dickish answer. Try again...
        if choice not in range(0,size):
	    print("Choose a row between 1 and " + str(size))
            continue
        else:
            #Seems cool
            return choice

def get_board_col(size):
    while True:
        try:
            choice = int(raw_input("Choose a Column:"))-1
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
            #Gave a dickish answer. Try again...
        if choice not in range(0,size):
	    print("Choose a column between 1 and " + str(size))
            continue
        else:
            #Seems cool
            return choice

def ship_direction(size,row_start,col_start,shipsize):
    ship = []
    first_spot = [row_start,col_start]
    while True:
        direction = raw_input("Do you want your ship to go left, right, up, or down?").lower()
        print direction
        if direction == "l" or direction == "left":
            col_end = col_start - shipsize + 1
            if (col_end < 0) or (col_end > size):
                print "You can't go left, you'll fall off the board!"
                continue
            else:
                for i in range(col_end, col_start):
                    new_spot = [row_start,i]
                    ship.append(new_spot)
                ship.append(first_spot)          
                return ship
        elif direction == "r" or direction == "right":
            col_end = col_start + shipsize 
            if (col_end < 0) or (col_end > size):
                print "You can't go right, you'll fall off the board!"
                continue
            else:
                ship.append(first_spot) 
                for i in range(col_start+1, col_end):
                    new_spot = [row_start,i]
                    ship.append(new_spot)             
                return ship
        elif direction == "u" or direction == "up":
            row_end = row_start - shipsize + 1
            if (row_end < 0) or (row_end > size):
                print "You can't go up, you'll fall off the board!"
                continue
            else:
                for i in range(row_end, row_start):
                    new_spot = [i,col_start]
                    ship.append(new_spot)
                ship.append(first_spot)            
                return ship
        elif direction == "d" or direction == "down":
            row_end = row_start + shipsize 
            if (row_end < 0) or (row_end > size):
                print "You can't go down, you'll fall off the board!"
                continue
            else:
                ship.append(first_spot) 
                for i in range(row_start+1, row_end):
                    new_spot = [i,col_start]
                    ship.append(new_spot)       
                return ship
        else:
            print "Try harder. It's just typing, you can do it!"
            continue

def comp_direction(size,row_start,col_start,shipsize):
    while True:
        ship = []
        first_spot = [row_start,col_start]
        direction = randint(0,3)
        if direction == 0: # Left
            col_end = col_start - shipsize + 1
            if (col_end < 0) or (col_end > size):
                continue
            else:
                for i in range(col_end, col_start):
                    new_spot = [row_start,i]
                    ship.append(new_spot)
                ship.append(first_spot)             
                return ship
        elif direction == 1: # Right
            col_end = col_start + shipsize 
            if (col_end < 0) or (col_end > size):
                continue
            else:
                ship.append(first_spot) 
                for i in range(col_start+1, col_end):
                    new_spot = [row_start,i]
                    ship.append(new_spot)
                return ship
        elif direction == 2: # Up
            row_end = row_start - shipsize + 1
            if (row_end < 0) or (row_end > size):
                continue
            else:
                for i in range(row_end, row_start):
                    new_spot = [i,col_start]
                    ship.append(new_spot)
                ship.append(first_spot)    
                return ship
        elif direction == 3: # Down
            row_end = row_start + shipsize 
            if (row_end < 0) or (row_end > size):
                continue
            else:
                ship.append(first_spot) 
                for i in range(row_start+1, row_end):
                    new_spot = [i,col_start]
                    ship.append(new_spot)        
                return ship
        else:
            continue


##### Creating the boards #####
computer_board = []
my_board = []

while True:
    try:
        board_size = int(raw_input("Choose a board size:"))
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
        #Gave a dickish answer. Try again...
    if board_size not in range(5,21):
	print("Choose a row between 5 and 20")
        continue
    else:
        #Seems cool
        break 
for x in range(board_size):
    computer_board.append(["*"] * board_size)

for x in range(board_size):
    my_board.append(["*"] * board_size)

##### Choosing the Battleship Locations #####

# Choosing the user's battleship
shipsize = 4
print("Place your battleship!")
print_board(my_board)
print "Choose a location:"
my_ship_row = get_board_row(board_size)
my_ship_col = get_board_col(board_size)
my_full_ship = ship_direction(board_size,my_ship_row,my_ship_col,shipsize)



#Choosing the computer's battleship
comp_ship_row = random_row(computer_board)
comp_ship_col = random_col(computer_board)
comp_full_ship = comp_direction(board_size,comp_ship_row,comp_ship_col,shipsize)

# Putting the battleships on the board and printing the boards for viewing:

for spots in my_full_ship:
    my_board[spots[0]][spots[1]] = "B"
print "My board:"
print_board(my_board)

#Commented out below so you can play properly, but kept so that you can troubleshoot (& view computer's ship)
#for spots in comp_full_ship:
#    computer_board[spots[0]][spots[1]] = "B"
print "Computer's Board:"
print_board(computer_board)

##### Gameplay! #####
print "Let's Play Battleship!"
turn = 1
shipknown = False
ship_coordinates = []
while True:
    print "Turn ", turn
    # The player makes a guess
    my_guess_row = int(raw_input("Guess Row:"))-1
    my_guess_col = int(raw_input("Guess Col:"))-1
    my_coordinates = [my_guess_row,my_guess_col]
    if my_coordinates in comp_full_ship:
        print "Oh No! You hit my battleship!"
        computer_board[my_guess_row][my_guess_col] = "X"
        comp_full_ship.remove(my_coordinates)
        if len(comp_full_ship) == 0:
            print_board(computer_board)
            print "You sunk my ship! I'll get you for this... next time!"
            break
    else:
        if (my_guess_row not in range(0,board_size)) or (my_guess_col not in range(0,board_size)):
            print "Check your aim! That's not even in the ocean."
        elif(computer_board[my_guess_row][my_guess_col] == "O" or computer_board[my_guess_row][my_guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "Haha, You missed my battleship!"
            computer_board[my_guess_row][my_guess_col] = "O"
    # The computer makes a guess
    if shipknown == False:
        computer_coordinates = computers_guess(my_board)
    else:
        computer_coordinates = computers_find(my_board,board_size,ship_coordinates)
    comp_guess_row = computer_coordinates[0]
    comp_guess_col = computer_coordinates[1]
    print("I chose row "+str(comp_guess_row+1)+" and column "+str(comp_guess_col+1))
    if computer_coordinates in my_full_ship:
        print "Haha! I hit your your battleship!"
        my_board[comp_guess_row][comp_guess_col] = "X"
        ship_coordinates.append(computer_coordinates)
        my_full_ship.remove(computer_coordinates)
        shipknown = True
        if len(my_full_ship) == 0:
            print_board(my_board)
            print "I sunk your ship. Looks like I WIN!"
            shipknown = False
            ship_coordinates = []
            break
    elif my_board[comp_guess_row][comp_guess_col] == "O" or my_board[comp_guess_row][comp_guess_col] == "X":
	print "Crap, I chose that one already!"
    else:
        print "I missed your battleship..."
        my_board[comp_guess_row][comp_guess_col] = "O"
    turn = turn + 1
    print "My board:"
    print_board(my_board)
    print "Computer's board:"
    print_board(computer_board)
