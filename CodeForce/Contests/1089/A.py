import sys
def solve():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        print(*(range(n, 0, -1)))
    

if __name__ == "__main__":
    solve()