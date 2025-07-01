def is_safe(queens, row, col):
    for r in range(row):
        c = queens[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True

def print_board(queens):
    for row in range(8):
        for col in range(8):
            print("Q" if queens[row] == col else ".", end=" ")
        print()
    print()

def solve(queens=[], row=0):
    if row == 8:
        print_board(queens)
        return True 
    for col in range(8):
        if is_safe(queens, row, col):
            if solve(queens + [col], row + 1):
                return True  
    return False

solve()
