def solution(name):
    name_len = len(name)
    move = name_len - 1
    change = sum(min(ord(c) - ord('A'), ord('Z') - ord(c) + 1) for c in name)

    for i in range(name_len):
        next_i = i + 1
        while next_i < name_len and name[next_i] == 'A':
            next_i += 1

        move = min(move, i + name_len - next_i + min(i, name_len - next_i))

    return move + change
