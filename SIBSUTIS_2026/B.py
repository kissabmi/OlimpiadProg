import sys


def solve():
    data = sys.stdin.read().split()
    idx = 0
    
    n = int(data[idx])
    m = int(data[idx + 1])
    idx += 2
    
    morty_order = [int(data[idx + i]) for i in range(m)]
    idx += m
    
    rick_parents = [0, 0] + [int(data[idx + i]) for i in range(n - 1)]
    idx += n - 1
    
    morty_parents = [int(data[idx + i]) for i in range(m)]
    idx += m
    
    rick_children = [[] for _ in range(n + 1)]
    morty_children = [[] for _ in range(n + 1)]
    
    for i in range(m):
        morty_num = morty_order[i]
        parent = morty_parents[i]
        morty_children[parent].append(morty_num)
    
    for rick in range(2, n + 1):
        parent = rick_parents[rick]
        rick_children[parent].append(rick)
    
    def get_morty_range(node):
        morty_list = []
        morty_list.extend(morty_children[node])
        for rick_child in rick_children[node]:
            morty_list.extend(get_morty_range(rick_child))
        return morty_list
    
    def check(node):
        child_ranges = []
        
        for morty in morty_children[node]:
            child_ranges.append((morty, morty))
        
        for rick_child in rick_children[node]:
            if not check(rick_child):
                return False
            morty_in_subtree = get_morty_range(rick_child)
            if morty_in_subtree:
                child_ranges.append((min(morty_in_subtree), max(morty_in_subtree)))
        
        if not child_ranges:
            return True
        
        child_ranges.sort()
        
        for i in range(len(child_ranges) - 1):
            if child_ranges[i][1] >= child_ranges[i + 1][0]:
                return False
        
        return True
    
    if check(1):
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()
