import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        li = [0] + list(map(int, input().split()))
        d = [0] * (n + 1)

        for i in li:
            d[i] += 1
        
        left = [i for i in range(1, n + 1) if not d[i]]

        for i in left:
            d[li[i]] -= 1
            if not d[li[i]]:
                left.append(li[i])

        print(len(left))

if __name__ == "__main__":
    sys.setrecursionlimit(10000000)
    main()
