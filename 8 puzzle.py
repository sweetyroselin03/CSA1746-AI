from collections import deque

# Goal: 1 2 3 / 4 5 6 / 7 8 0
goal = "123456780"

# Get blank tile position
def get_blank(state):
    i = state.index('0')
    return i // 3, i % 3  # row, col

# Swap tiles and return new state
def swap(state, i1, i2):
    s = list(state)
    s[i1], s[i2] = s[i2], s[i1]
    return ''.join(s)

# Get all possible moves from current state
def get_moves(state):
    r, c = get_blank(state)
    i = r * 3 + c
    moves = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            j = nr * 3 + nc
            moves.append(swap(state, i, j))
    return moves

# BFS solver
def solve(start):
    queue = deque()
    visited = set()
    queue.append((start, []))

    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)

        path = path + [state]
        if state == goal:
            return path

        for next_state in get_moves(state):
            queue.append((next_state, path))
    return None

# Starting board
start_board = "123406758"  # Flattened version of [[1,2,3],[4,0,6],[7,5,8]]
solution = solve(start_board)

# Display result
if solution:
    for step, state in enumerate(solution):
        print(f"Step {step}:")
        for i in range(0, 9, 3):
            print(state[i:i+3])
        print()
else:
    print("No solution found.")
