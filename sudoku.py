import sys

def parse_sudoku(s):
    #Converts a sudoku in string form to a 2D list of integers.
    sudoku = []
    s = [int(i) for i in s]
    for i in range(9):
        sudoku.append(s[i*9:i*9+9])
    return sudoku

def solve(sudoku, index):
    #The main solving method. Recursively checks if a given field must be filled and if it does uses the guess method to guess.
    if sudoku[index // 9][index % 9] != 0:
        solve(sudoku, index + 1)
    else:
        guess(sudoku, index)

def guess(sudoku, index):
    #guesses a number for a field and checks its validity. If its a possible value, it starts solving the next field, else it will guess again
    row = index // 9
    col = index % 9
    for i in range(1,10):
        sudoku[row][col] = i
        if check(sudoku, row, col):
            check_solved(sudoku, index)
            solve(sudoku, index + 1)
    sudoku[row][col] = 0    

def check_solved(sudoku, index):
    #Checks whether or not the end had been reached.
    if index == 80:
        print(sudoku)
        sys.exit(1)

def check(sudoku, row, col):
    #Checks the validity of a guess.
    return  check_row(sudoku, row) and check_column(sudoku, col) and check_box(sudoku, row, col)

def check_row(sudoku, row):
    #Checks a single row.
    return check_list(sudoku[row])

def check_column(sudoku, col):
    #Checks a single column.
    return check_list([row[col] for row in sudoku])

def check_box(sudoku, row, col):
    #Checks a single box.
    box = []
    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for i in range(box_row, box_row+3):
        for j in range(box_col, box_col+3):
            box += [sudoku[i][j]]
    return check_list(box)

def check_list(lst):
    #Checks a list for double occurences of integers.
    lst = [n for n in lst if n != 0]
    return len(set(lst)) == len(lst)

def main():
    sudoku = parse_sudoku(sys.argv[1])
    solve(sudoku,0)

if __name__ == '__main__':
  main()