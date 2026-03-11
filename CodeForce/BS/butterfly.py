def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


def solve():
    collections = []

    with open("collect.in", "r") as f:
        n = int(f.readline())
        collections = [int(x) for x in f.readline().strip().split()]
        m = int(f.readline())
        check = [int(x) for x in f.readline().strip().split()]

    with open("collect.out", "w") as f:
        for i in range(m):
            if binary_search(collections, check[i]):
                f.write("YES\n")
            else:
                f.write("NO\n")

    # print(collections)
    # print(check)


if __name__ == "__main__":
    solve()
