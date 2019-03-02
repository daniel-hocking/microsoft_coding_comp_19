def find_paths(steps):
    zb = 1
    zadc = 0
    max_zb = 10**9 + 7

    for i in range(1, steps + 1):
        nzb = zadc * 3
        nzadc = zadc * 2 + zb
        zb = nzb
        zadc = nzadc
        if nzb > max_zb:
            zb %= max_zb
            zadc %= max_zb

    return zb
    
steps = int(input())
total = find_paths(steps)
print(total)
