import sys
input = sys.stdin.readline

def gcm(num1, num2):    # 최대 공약수
    val = 1 

    for i in range(2, num2+1):
        if(num1%i == 0 and num2%i == 0):
            val = i

    return val


def lcm(num1, num2):    # 최소 공배수
    val = num1 * num2

    if(gcm(num1, num2) != 0):
        val //= gcm(num1, num2)
    
    return val


a, b = map(int, input().split())

print(gcm(a, b))
print(lcm(a, b))