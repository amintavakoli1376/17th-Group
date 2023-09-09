import turtle
import random



# Create the Sudoku board
def generate_sudoku():
    board = [[0 for _ in range(9)] for _ in range(9)]
    def solve_sudoku(row, col):
        if col == 9:
            if row == 8:
                return True
            row += 1
            col = 0

        if board[row][col] != 0:
            return solve_sudoku(row, col + 1)

        for num in random.sample(range(1, 10), k=9):
            if is_valid(row, col, num):
                board[row][col] = num
                if solve_sudoku(row, col + 1):
                    return True
                board[row][col] = 0

    def is_valid(row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False

        return True

    solve_sudoku(0, 0)
    return board


screen = turtle.Screen()
screen.setup(700, 700)
screen.title("Sudoku Table")

# Draw Sudoku Table
def draw_table(board):
    turtle.hideturtle()
    turtle.speed(0)
    turtle.pensize(5)

    # Draw Main Square
    for _ in range(4):
        turtle.forward(297)
        turtle.right(90)

    turtle.pensize(3)
    for i in range(3):
        for _ in range(4):
            turtle.forward(99)
            turtle.right(90)
            i += i

        turtle.forward(99)

    # Draw 3*3 Square
    turtle.penup()
    turtle.goto(0, -99)
    turtle.pendown()

    for i in range(3):
        for _ in range(4):
            turtle.forward(99)
            turtle.right(90)
            i += i

        turtle.forward(99)

    turtle.penup()
    turtle.goto(0, -198)
    turtle.pendown()

    for i in range(2):
        for _ in range(4):
            turtle.forward(99)
            turtle.right(90)
            i += i

        turtle.forward(99)

    turtle.pensize(1)
    turtle.penup()
    turtle.home()
    turtle.pendown()

    # Draw 9*9 Square
    for i in range(9):
        for _ in range(4):
            turtle.forward(33)
            turtle.right(90)
            i += i

        turtle.forward(33)

    turtle.penup()
    turtle.goto(0, -33)
    turtle.pendown()

    for i in range(9):
        for _ in range(4):
            turtle.forward(33)
            turtle.right(90)
            i += i

        turtle.forward(33)

    turtle.penup()
    turtle.goto(0, -66)
    turtle.pendown()

    for i in range(9):
        for _ in range(4):
            turtle.forward(33)
            turtle.right(90)
            i += i

        turtle.forward(33)

    turtle.penup()
    turtle.goto(0, -99)
    turtle.pendown()

    for i in range(9):
        for _ in range(4):
            turtle.forward(33)
            turtle.right(90)
            i += i

        turtle.forward(33)

    turtle.penup()
    turtle.goto(0, -132)
    turtle.pendown()

    for i in range(9):
        for _ in range(4):
            turtle.forward(33)
            turtle.right(90)
            i += i

        turtle.forward(33)

    turtle.penup()
    turtle.goto(0, -165)
    turtle.pendown()

    for i in range(9):
        for _ in range(4):
            turtle.forward(33)
            turtle.right(90)
            i += i

        turtle.forward(33)

    turtle.penup()
    turtle.goto(0, -198)
    turtle.pendown()

    for i in range(9):
        for _ in range(4):
            turtle.forward(33)
            turtle.right(90)
            i += i

        turtle.forward(33)

    turtle.penup()
    turtle.goto(0, -231)
    turtle.pendown()

    for i in range(9):
        for _ in range(4):
            turtle.forward(33)
            turtle.right(90)
            i += i

        turtle.forward(33)

    turtle.penup()
    turtle.goto(0, -264)
    turtle.pendown()

    for i in range(9):
        for _ in range(4):
            turtle.forward(33)
            turtle.right(90)
            i += i

        turtle.forward(33)

    # Write the numbers in the Sudoku table
    turtle.penup()
    turtle.goto(20, -25)
    turtle.pendown()
    turtle.color("blue")
    turtle.pensize(1)
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                turtle.write(board[i][j], align="center", font=("Arial", 16, "bold"))
            turtle.penup()
            turtle.forward(33)
        turtle.backward(297)
        turtle.right(90)
        turtle.forward(33)
        turtle.left(90)

    turtle.done()

board = generate_sudoku()
draw_table(board)
