def solution(board, h, w):
    count = 0 
    color = board[h][w] 
    directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
    
    if not board or not board[0]:
        return 0

    for dir_h, dir_w in directions:
        mov_h = h + dir_h 
        mov_w = w + dir_w
        
        if 0 <= mov_h < len(board) and 0 <= mov_w < len(board[0]):
            count += (color == board[mov_h][mov_w])
    
    return count
