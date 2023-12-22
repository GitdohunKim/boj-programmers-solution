def solution(board):

    num_o, num_x = 0, 0
    for row in board:
        for cell in row:
            if cell == "O":
                num_o += 1
            elif cell == "X":
                num_x += 1
    if not (num_o == num_x or num_o == num_x + 1):
        return 0

    win_case = [
        *[[(i, j) for i in range(3)] for j in range(3)],
        *[[(j, i) for i in range(3)] for j in range(3)],
        [(i, i) for i in range(3)],
        [(i, 2-i) for i in range(3)],
    ]
    num_wins_o, num_wins_x = 0, 0
    for win in win_case:
        cells = [board[row][col] for (row, col) in win]
        if cells == ["O", "O", "O"]:
            num_wins_o += 1
        elif cells == ["X", "X", "X"]:
            num_wins_x += 1
    if num_wins_o > 0 and num_wins_x > 0:
        return 0
    if num_wins_o > 0 and num_o == num_x:
        return 0
    if num_wins_x > 0 and num_o == num_x + 1:
        return 0

    return 1
