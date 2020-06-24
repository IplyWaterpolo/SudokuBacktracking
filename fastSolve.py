import time
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solve(bo): #recursive backtracking
#once we reach end of board, solution has been found
#we can print up here in order to see all steps
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo): #solve gets called within itself, which is why it is recursive
                return True
        
            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    #check column
    for i in range(len(bo[0])):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #check 3x3 modules or boxes
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    #loop through 9 elems in box

    for i in range(box_y*3, box_y*3 + 3): #finds index of number we're on multiplying box pos by 3 and adding 3
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True


def format(bo):
    for i in range(len(bo)):
        if i %3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - -") 
        for j in range(len(bo[0])): #Length of each row
            if j %3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]), " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) #row and column
    
    return None #if there's no blank sqrs return none
            
print("BOARD BEFORE:")
print("")
format(board)
print("BOARD AFTER:")
print("")
solve(board)
format(board)
time.sleep(10)
