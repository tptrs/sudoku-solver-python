import sys

def parse_sudoku(s):
    sudoku = []
    for i in range(81):
        if i % 9 == 0:
            sudoku.append([int(s[i])])
        else:
            sudoku[i // 9] += [int(s[i])]
    return sudoku

def guess(sudoku, index):
    row = index // 9
    col = index % 9
    if sudoku[row][col] != 0:
        guess(sudoku, index + 1)
    else:
        for i in range(1,10):
            sudoku[row][col] = i
            if check(sudoku, row, col):
                if index == 80:
                    print(sudoku)
                    sys.exit(1)
                guess(sudoku, index + 1)
        sudoku[row][col] = 0

def check(sudoku, row, col):
    return  check_row(sudoku, row) and check_column(sudoku, col) and check_box(sudoku, row, col)

def check_row(sudoku, row):
    return check_list(sudoku[row])

def check_column(sudoku, col):
    return check_list([row[col] for row in sudoku])

def check_box(sudoku, row, col):
    box = []
    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for i in range(box_row, box_row+3):
        for j in range(box_col, box_col+3):
            box += [sudoku[i][j]]
    return check_list(box)

def check_list(lst):
    for i in range(1,10):
        if lst.count(i) > 1:
            return False
    return True

def main():
    sudoku = parse_sudoku(sys.argv[1])
    guess(sudoku,0)

if __name__ == '__main__':
  main()