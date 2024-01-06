input = open(0).readline

def square(i, j):
    return (i // 3) * 3 + j // 3

def fill_bit(i, j, n, bit_board):
    bit_board[i * 9 + j] = 0b1111111110
    bit = 1 << n
    for ii in range(9):
        bit_board[ii * 9 + j] |= bit
    for jj in range(9):
        bit_board[i * 9 + jj] |= bit
    i = i // 3 * 3
    j = j // 3 * 3
    for ii in range(3):
        for jj in range(3):
            bit_board[(i + ii) * 9 + j + jj] |= bit
    return bit_board

def check(i, j, n, check_rcs):
    if check_rcs[i] & (1 << n) or check_rcs[9 + j] & (1 << n) or check_rcs[18 + square(i, j)] & (1 << n):
        return False, check_rcs
    check_rcs[i] |= 1 << n
    check_rcs[9 + j] |= 1 << n
    check_rcs[18 + square(i, j)] |= 1 << n
    return True, check_rcs

def fill(i, j, n, board, bit_board, check_rcs):
    board[i * 9 + j] = n
    bit_board = fill_bit(i, j, n, bit_board)
    ok, check_rcs = check(i, j, n, check_rcs)
    return ok, board, bit_board, check_rcs

def fill_one_blank(board, bit_board, check_rcs):
    fill_count = 0
    for n in range(1, 10):
        for i in range(9):
            count = 0
            for j in range(9):
                if bit_board[i * 9 + j] & (1 << n):
                    count += 1
                else:
                    fj = j
            if count == 8:
                fill_count += 1
                ok, board, bit_board, check_rcs = fill(i, fj, n, board, bit_board, check_rcs)
                if not ok:
                    return False, board, bit_board, check_rcs
        for j in range(9):
            count = 0
            for i in range(9):
                if bit_board[i * 9 + j] & (1 << n):
                    count += 1
                else:
                    fi = i
            if count == 8:
                fill_count += 1
                ok, board, bit_board, check_rcs = fill(fi, j, n, board, bit_board, check_rcs)
                if not ok:
                    return False, board, bit_board, check_rcs
        for i in range(3):
            for j in range(3):
                count = 0
                for ii in range(3):
                    for jj in range(3):
                        ni = i * 3 + ii
                        nj = j * 3 + jj
                        if bit_board[ni * 9 + nj] & (1 << n):
                            count += 1
                        else:
                            fi, fj = ni, nj
                if count == 8:
                    fill_count += 1
                    ok, board, bit_board, check_rcs = fill(fi, fj, n, board, bit_board, check_rcs)
                    if not ok:
                        return False, board, bit_board, check_rcs
    if fill_count:
        ok, board, bit_board, check_rcs = fill_one_blank(board, bit_board, check_rcs)
        if not ok:
            return False, board, bit_board, check_rcs
    return True, board, bit_board, check_rcs

def solve(z, board, bit_board, check_rcs):
    if z == 81:
        for i in range(9):
            print(*board[i * 9 : i * 9 + 9], sep='')
        return True, board, bit_board, check_rcs
    if board[z] != 0:
        return solve(z + 1, board, bit_board, check_rcs)
    i = z // 9
    j = z % 9
    for n in range(1, 10):
        if check_rcs[i] & (1 << n) == 0 and check_rcs[9 + j] & (1 << n) == 0 and check_rcs[18 + square(i, j)] & (1 << n) == 0:
            _, nboard, nbit_board, ncheck_rcs = fill(i, j, n, [*board], [*bit_board], [*check_rcs])
            ok, nboard, nbit_board, ncheck_rcs = solve(z + 1, nboard, nbit_board, ncheck_rcs)
            if ok:
                return True, nboard, nbit_board, ncheck_rcs
    return False, board, bit_board, check_rcs

def main():
    board = [0] * 81
    bit_board = [0] * 81
    check_rcs = [0] * 27
    for i in range(9):
        for j, num in enumerate(map(int, input().rstrip())):
            if num != 0:
                ok, board, bit_board, check_rcs = fill(i, j, num, board, bit_board, check_rcs)
    ok, board, bit_board, check_rcs = fill_one_blank(board, bit_board, check_rcs)
    solve(0, board, bit_board, check_rcs)

main()