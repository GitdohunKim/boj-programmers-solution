import sys
speed_input = sys.stdin.readline


def some(seq):
    for e in seq:
        if e:
            return e
    return False


def cross(set_a, set_b):
    return [a + b for a in set_a for b in set_b]


class Solver:
    def __init__(self):
        self.digits = '123456789'
        self.rows = 'ABCDEFGHI'
        self.cols = self.digits
        self.squares = cross(self.rows, self.cols)
        self.unit_list = ([cross(self.rows, c) for c in self.cols] +
                     [cross(r, self.cols) for r in self.rows] +
                     [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])
        self.units = dict((s, [u for u in self.unit_list if s in u]) for s in self.squares)
        self.peers = dict((s, set(sum(self.units[s], [])) - {s}) for s in self.squares)
        self.__board = [list(speed_input()) for _ in range(9)]

    def grid_values(self):
        chars = []
        for l in self.__board:
            temp = [c for c in l if c in self.digits or c in '0.']
            chars += temp
        return dict(zip(self.squares, chars))

    def parse_grid(self):
        values = dict((s, self.digits) for s in self.squares)
        for s, d in self.grid_values().items():
            if d in self.digits and not self.assign(values, s, d):
                return False
        return values

    def assign(self, values, s, d):
        other_values = values[s].replace(d, '')
        if all(self.eliminate(values, s, d2) for d2 in other_values):
            return values
        else:
            return False

    def eliminate(self, values, s, d):
        if d not in values[s]:
            return values
        values[s] = values[s].replace(d, '')
        if len(values[s]) == 0:
            return False
        elif len(values[s]) == 1:
            d2 = values[s]
            if not all(self.eliminate(values, s2, d2) for s2 in self.peers[s]):
                return False
        for u in self.units[s]:
            dplaces = [s for s in u if d in values[s]]
            if len(dplaces) == 0:
                return False
            elif len(dplaces) == 1:
                if not self.assign(values, dplaces[0], d):
                    return False
        return values

    def search(self, values):
        if values is False:
            return False
        if all(len(values[s]) == 1 for s in self.squares):
            return values
        n, s = min((len(values[s]), s) for s in self.squares if len(values[s]) > 1)
        return some(self.search(self.assign(values.copy(), s, d)) for d in values[s])

    def __display(self, values):
        for r in self.rows:
            print(' '.join(values[r + c] for c in self.cols))

    def solve(self):
        self.__display(self.search(self.parse_grid()))


def main():
    Solver().solve()


if __name__ == '__main__':
    main()
