import sys

def find_closest_triplet(solution):
    N = len(solution)
    answer = [float('inf')] * 3

    if solution[0] >= 0:
        return solution[:3]
    elif solution[-1] <= 0:
        return solution[-3:]
    else:
        for i in range(N - 2):
            s, e = i + 1, N - 1
            
            while s < e:
                value = solution[i] + solution[s] + solution[e]
                if abs(sum(answer)) > abs(value):
                    answer = [solution[i], solution[s], solution[e]]
                if value < 0:
                    s += 1
                elif value > 0:
                    e -= 1
                else:
                    return answer
    return answer

def main():
    input = sys.stdin.readline
    N = int(input())
    solution = sorted(map(int, input().split()))
    answer = find_closest_triplet(solution)
    print(*answer)

if __name__ == "__main__":
    main()
