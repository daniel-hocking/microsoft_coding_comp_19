from functools import reduce

def calc_gcd(i, j):
    # find factors for all number with no factors
    f = None
    for x in range(i, j+1):
        if not nums[x]:
            continue
        if factors[x] == None:
            # must find factors
            factors[x] = calc_factors(nums[x])
        # get factors for first instance
        if f == None:
            f = factors[x]
        else:        
            f = [a for a in f if a in factors[x]]
        if len(f) == 0:
            return 1
    
    if not len(f):
        return 0

    return max(f)

def calc_factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

N = int(input())
nums = [abs(int(x)) for x in input().split()]
Q = int(input())

factors = [None]*N

while True:
    try:
        query = input()
    except:
        exit(0)
    query = query.split()
    action = int(query[0])
    i = int(query[1])
    j = int(query[2])
    if action == 1:
        # find gcds from i to j inclusive
        print(calc_gcd(i, j))
    else:
        # update index i with x
        nums[i] = abs(j)
        factors[i] = None
