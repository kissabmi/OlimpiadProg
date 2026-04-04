import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    idx = 1
    out = []
    
    for _ in range(t):
        n = int(input_data[idx])
        idx += 1
        
        diff = [0] * (n + 2)
        
        for j in range(1, n + 1):
            p_j = int(input_data[idx])
            idx += 1
            
            if p_j <= j:
                diff[j] += 1
                diff[n + 1] -= 1
            else:
                diff[j] += 1
                diff[p_j] -= 1
                
        current_chairs = 0
        max_chairs = 0
        for k in range(1, n + 1):
            current_chairs += diff[k]
            if current_chairs > max_chairs:
                max_chairs = current_chairs
                
        out.append(str(max_chairs))
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()
