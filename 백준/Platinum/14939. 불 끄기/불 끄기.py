import sys

def solution():
    board = [int(''.join(map(lambda x: '1' * (x == 'O') or '0', [*input().rstrip()])), 2) for _ in range(10)]
    m = 1 << 10

    def count_bits(num):
        return bin(num).count('1')

    for turn in range(m):
        i = turn
        cnt = count_bits(turn)
        prev = board[0] ^ i ^ ((i << 1) & (m - 1)) ^ (i >> 1)
        current = board[1] ^ i

        for k in range(1, 10):
            i = prev
            cnt += count_bits(i)
            current ^= i ^ ((i << 1) & (m - 1)) ^ (i >> 1)
            if k + 1 < 10:
                prev, current = current, board[k + 1] ^ i

        if current == 0:
            print(cnt)
            return
    else:
        print(-1)

if __name__ == "__main__":
    solution()
