import sys
input = sys.stdin.readline

# m은 트리 전체 구간의 합
def locate(m, idx):
	# 왼쪽 구간의 누적합
    acc_num = 0
    k = idx
    # 누적합을 구함
    while k > 0:
        acc_num += fenwick_tree[k]
        k -= k & -k 

    k = idx
    # 트리에 삽입
    while k <= n:
        fenwick_tree[k] += 1 
        k += k & -k 
    # 오른쪽 구간의 누적합을 리턴
    return m - acc_num
    
n = int(input())
fenwick_tree = [0]*(n+1)
loc = {}
count = 0
for i, a in enumerate(map(int, input().rstrip().split())):
    loc[a] = i+1
    
for i, b in enumerate(map(int, input().rstrip().split())):
    count += locate(i, loc[b])
    
print(count)