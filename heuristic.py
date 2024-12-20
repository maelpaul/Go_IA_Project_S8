import Goban

def libertiesAndCountHeuristic(board, color):
    black_score = 0
    white_score = 0

    black_liberties = 0
    white_liberties = 0

    black_stones = 0
    white_stones = 0

    black_influence = 0
    white_influence = 0

    for i in range(9):
        for j in range(9):
            
            stone_color = board[board.flatten((i,j))]
            if stone_color != Goban.Board._EMPTY:
                stone_liberties = 0
                if i > 0 and board[board.flatten((i-1,j))] == Goban.Board._EMPTY:
                    stone_liberties += 1
                if j > 0 and board[board.flatten((i,j-1))] == Goban.Board._EMPTY:
                    stone_liberties += 1
                if i < 8 and board[board.flatten((i+1,j))] == Goban.Board._EMPTY:
                    stone_liberties += 1
                if j < 8 and board[board.flatten((i,j+1))] == Goban.Board._EMPTY:
                    stone_liberties += 1
                if stone_color == Goban.Board._BLACK:
                    black_liberties += stone_liberties
                    black_stones +=1

                else:
                    white_liberties += stone_liberties
                    white_stones += 1

                black_influence_weight = 0
                white_influence_weight = 0
                for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                    ni, nj = i+di, j+dj
                    if 0 <= ni <= 8 and 0 <= nj <= 8:
                        stone_color = board[board.flatten((ni,nj))]
                        if stone_color == Goban.Board._BLACK:
                            black_influence_weight += 1
                        elif stone_color == Goban.Board._WHITE:
                            white_influence_weight += 1
                if black_influence_weight > white_influence_weight:
                    black_influence += 1
                elif white_influence_weight > black_influence_weight:
                    white_influence += 1



                
    white_score += white_liberties + white_stones + white_influence
    black_score += black_liberties + black_stones + black_influence
            
    if color == Goban.Board._BLACK:
        return black_score - white_score
    else:
        return white_score - black_score

def secondHeuristic(board, color):
    moves = board.legal_moves()
    result = 0
    if board.is_game_over():
        return libertiesAndCountHeuristic(board, color)
    
    for move in moves:
        board.push(move)
        result += libertiesAndCountHeuristic(board,color)
        board.pop()
    
    return result + libertiesAndCountHeuristic(board, color)

def quick_heuristic(board, color):
    (black, white) = board.compute_score()
    if color == Goban.Board._BLACK:
        return black - white
    else:
        return white - black    
