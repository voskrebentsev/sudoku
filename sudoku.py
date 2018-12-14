##Function CHECKERS

def check_row(matrix, row):
    dt = {}
    for n in matrix[row]:
        if n != 0:
            if n not in dt:
                dt[n] = 1
            else:
                return False
    return True

def check_col(matrix, col):
    dt = {}
    for i in range(len(matrix)):
        if matrix[i][col] != 0:
            if matrix[i][col] not in dt:
                dt[matrix[i][col]] = 1
            else:
                return False
    return True

#function helper for squarecheck that determine the center of square that should be checked
def center_num(num):
    if num < 3 :
        num = 1
    elif num < 6:
        num = 4
    else:
        num = 7
    return num

def check_square(matrix, col, row):
    col = center_num(col)
    row = center_num(row)
    dt = {}
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if matrix[i][j] != 0:
                if matrix[i][j] not in dt:
                    dt[matrix[i][j]] = 1
                else:
                    return False
    return True

def full_check(matrix, row, col):
    if check_square(matrix, col, row) and check_col(matrix, col) and check_row(matrix, row):
        return True
    return False

def full_matrix_check(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not full_check(matrix, i, j):
                return False
    return True
#main function that filling matrix with numbers

def filler(matrix, y=0, x=0):
    if x > 8:
        if y == 8:
            return True
        else:
            x = 0
            y += 1
    if matrix[y][x] != 0:
        return filler(matrix, y, x + 1)
    else:
        num = 1
        while (num < 10):
            matrix[y][x] = num
            if full_check(matrix, y, x):
                if filler(matrix, y, x + 1):
                    return True
            num += 1
        matrix[y][x] = 0
        return False

def matrix_print(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


matrix = [[0,4,0,3,0,9,7,5,1],
          [0,0,7,5,4,6,2,8,3],
          [5,0,0,0,0,0,4,6,9],
          [0,0,0,0,0,0,1,4,6],
          [0,8,6,1,0,0,9,3,5],
          [0,0,1,6,0,0,8,2,7],
          [0,0,5,8,6,2,3,9,4],
          [8,6,4,9,3,7,5,1,0],
          [3,2,9,4,1,5,6,7,0]]

matrix2 = [[0]*9 for i in range(9)]

matrix3 = [[6,4,8,3,0,9,7,5,1],
          [9,1,7,5,4,6,2,8,3],
          [5,3,2,7,8,1,4,6,9],
          [7,9,3,2,5,8,1,4,6],
          [2,8,6,1,0,4,9,3,5],
          [4,5,1,6,0,3,8,2,7],
          [1,7,5,8,6,2,3,9,4],
          [8,6,4,9,3,7,5,1,0],
          [3,2,9,4,1,5,6,7,0]]

matrix4 =  [[0,6,0,8,5,4,0,0,0],
            [0,0,5,0,1,0,0,0,0],
            [4,0,0,0,0,7,1,0,0],
            [0,0,0,2,0,0,7,9,8],
            [3,0,0,0,6,9,0,0,0],
            [7,0,0,0,0,0,2,0,0],
            [0,0,0,0,0,0,0,4,0],
            [8,2,0,0,0,0,3,5,0],
            [0,0,0,4,8,1,0,0,0]]
#print(full_matrix_check(matrix))
filler(matrix4)
matrix_print(matrix4)
#print(filler(matrix3))
#matrix_print(matrix3)
#filler(matrix2)
#matrix_print(matrix2)
