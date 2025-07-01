def minimax_search(state, depth, player):
    if depth == 0 or game_over(state):
        return evaluate(state), None

    if player == "X":  # Maximizing player
        best_score = float('-inf')
        best_move = None
        for move in get_possible_moves(state):
            new_state = make_move(state, move, player)
            score, _ = minimax_search(new_state, depth - 1, "O")
            if score > best_score:
                best_score = score
                best_move = move
        return best_score, best_move

    else:  # Minimizing player
        best_score = float('inf')
        best_move = None
        for move in get_possible_moves(state):
            new_state = make_move(state, move, player)
            score, _ = minimax_search(new_state, depth - 1, "X")
            if score < best_score:
                best_score = score
                best_move = move
        return best_score, best_move
