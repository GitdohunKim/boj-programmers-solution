def make_nine(arr, N, num):
    while N % 10 != 9:
        for i in str(N):
            arr[int(i)] += num
        N -= 1
    return N

def distribute_digits(arr, N, num):
    N = make_nine(arr, N, num)
    if N < 10:
        for i in range(N + 1):
            arr[i] += num
    else:
        for i in range(10):
            arr[i] += (N // 10 + 1) * num
    arr[0] -= num
    return N // 10

def main():
    N = int(input())
    arr = [0] * 10
    num = 1

    while N > 0:
        N = distribute_digits(arr, N, num)
        num *= 10

    for i in range(10):
        print(arr[i], end=' ')

if __name__ == "__main__":
    main()
