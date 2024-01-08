import sys
from collections import deque

def input_int():
    return int(sys.stdin.readline())

def input_str():
    return sys.stdin.readline().rstrip()

def get_rbh_positions(board, row_size, col_size):
    r_pos, b_pos, h_pos = (-1, -1), (-1, -1), (-1, -1)

    for row_idx in range(row_size):
        for col_idx in range(col_size):
            if board[row_idx][col_idx] == 'R':
                r_pos = (row_idx, col_idx)
            elif board[row_idx][col_idx] == 'B':
                b_pos = (row_idx, col_idx)
            elif board[row_idx][col_idx] == 'O':
                h_pos = (row_idx, col_idx)

            if r_pos != (-1, -1) and b_pos != (-1, -1) and h_pos != (-1, -1):
                return r_pos, b_pos, h_pos

    return r_pos, b_pos, h_pos

def move_marble_pos_step(board, pos, direction, h_pos):
    step = 1
    while True:
        if board[pos[0] + direction[0] * step][pos[1] + direction[1] * step] == '#':
            return (pos[0] + direction[0] * (step - 1), pos[1] + direction[1] * (step - 1)), step - 1

        if (pos[0] + direction[0] * step, pos[1] + direction[1] * step) == h_pos:
            return (pos[0] + direction[0] * step, pos[1] + direction[1] * step), step

        step += 1

def pos_when_overlap(pos, moved_r_step, moved_b_step, direction):
    if moved_r_step > moved_b_step:
        return (pos[0] - direction[0], pos[1] - direction[1]), pos
    else:
        return pos, (pos[0] - direction[0], pos[1] - direction[1])

def search(board, queue, h_pos, visited):
    while queue:
        cur_r_pos, cur_b_pos, roll_cnt = queue.popleft()

        if roll_cnt > 10:
            return -1

        for direction in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            moved_r_pos, moved_r_step = move_marble_pos_step(board, cur_r_pos, direction, h_pos)
            moved_b_pos, moved_b_step = move_marble_pos_step(board, cur_b_pos, direction, h_pos)

            if moved_r_pos == h_pos and moved_b_pos != h_pos:
                return roll_cnt

            if moved_r_pos == moved_b_pos and moved_r_pos != h_pos:
                moved_r_pos, moved_b_pos = pos_when_overlap(moved_r_pos, moved_r_step, moved_b_step, direction)

            if moved_r_pos != h_pos and moved_b_pos != h_pos:
                if not visited[moved_r_pos[0]][moved_r_pos[1]][moved_b_pos[0]][moved_b_pos[1]]:
                    queue.append((moved_r_pos, moved_b_pos, roll_cnt + 1))
                    visited[moved_r_pos[0]][moved_r_pos[1]][moved_b_pos[0]][moved_b_pos[1]] = True

    return -1

if __name__ == "__main__":
    row_size, col_size = map(int, input_str().split())
    board = [list(input_str()) for _ in range(row_size)]

    r_pos, b_pos, h_pos = get_rbh_positions(board, row_size, col_size)

    queue = deque()
    queue.append((r_pos, b_pos, 1))

    visited = [[[[False for _ in range(col_size)] for _ in range(row_size)] for _ in range(col_size)] for _ in range(row_size)]
    visited[r_pos[0]][r_pos[1]][b_pos[0]][b_pos[1]] = True

    result = search(board, queue, h_pos, visited)
    print(result)
