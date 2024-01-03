from itertools import permutations

def main():
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    for answer in sorted(set(permutations(nums, m))):
        print(*answer, sep=' ')

if __name__ == '__main__':
    main()
