import sys
from itertools import combinations

input = sys.stdin.readline

def chicken_distance(city, chicken_positions, selected_chickens):
    total_distance = 0
    for house in city['houses']:
        min_chicken_distance = float('inf')
        for selected_chicken in selected_chickens:
            chicken_distance = abs(house[0] - selected_chicken[0]) + abs(house[1] - selected_chicken[1])
            min_chicken_distance = min(min_chicken_distance, chicken_distance)
        total_distance += min_chicken_distance
    return total_distance

def main():
    n, m = map(int, input().split())
    city = {'houses': [], 'chickens': []}

    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(n):
            if row[j] == 1:
                city['houses'].append([i, j])
            elif row[j] == 2:
                city['chickens'].append([i, j])

    result = float('inf')

    for selected_chickens in combinations(city['chickens'], m):
        result = min(result, chicken_distance(city, city['chickens'], selected_chickens))

    print(result)

if __name__ == "__main__":
    main()
