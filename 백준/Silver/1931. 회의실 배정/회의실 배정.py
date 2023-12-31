import io, os

def main():
    n, *m = map(int, open(0).read().split())
    v = sorted(e << 32 | s for s, e in zip(m[::2], m[1::2]))
    last = 0
    print(sum(map(bool, ((last := x >> 32) for x in v if (x & 0xFFFFFFFF) >= last))), flush=True)
    os._exit(0)

if __name__ == '__main__':
    main()