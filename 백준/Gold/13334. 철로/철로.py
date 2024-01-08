from sys import stdin
import heapq

def main():
    n = int(stdin.readline())
    data = [sorted(map(int, stdin.readline().split())) for _ in range(n)]
    train_road_length = int(stdin.readline())

    roads = [road for road in data if road[1] - road[0] <= train_road_length]
    roads.sort(key=lambda x: x[1])

    answer = 0
    q = []

    for road in roads:
        s, e = road
        while q and q[0][0] < e - train_road_length:
            heapq.heappop(q)

        heapq.heappush(q, road)
        answer = max(answer, len(q))

    print(answer)

if __name__ == "__main__":
    main()
