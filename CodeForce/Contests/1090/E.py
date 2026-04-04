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
        
        a_list = input_data[idx : idx + n]
        idx += n
        
        # Сразу переводим в числа и убираем дубликаты
        A = set(int(x) for x in a_list)
        if len(A) == 1:
            out.append(0)
            continue
            
        max_xor = 0
        # 10^9 < 2^30, поэтому достаточно проверять с 29-го бита
        for i in range(29, -1, -1):
            max_xor <<= 1
            target = max_xor | 1
            prefixes = {x >> i for x in A}
            found = False
            for p in prefixes:
                if (p ^ target) in prefixes:
                    found = True
                    break
            if found:
                max_xor = target
                
        out.append(max_xor)
        
    for res in out:
        sys.stdout.write(str(res) + '\n')


if __name__ == "__main__":
    solve()
