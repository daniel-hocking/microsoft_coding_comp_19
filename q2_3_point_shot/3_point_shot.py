# get input
N = int(input())
aTmp = input()
M = int(input())
bTmp = input()

aList = [int(x) for x in aTmp.split()]
bList = [int(x) for x in bTmp.split()]
aList.sort()
bList.sort()


max_a = N * 2
max_b = M * 2
max_diff = max_a - max_b
cur_a = float("-inf")
cur_b = float("-inf")

for i in range(N):
    cur_a = ((N - i) * 3) + (i * 2)
    current = aList[i]
    if current < bList[0]:
        cur_b = M * 3
    elif current > bList[M - 1]:
        cur_b = M * 2
    else:
        j = 0
        while current > bList[j]:
            j += 1
        cur_b = ((M - j) * 3) + (j * 2)
    cur_diff = cur_a - cur_b
    if cur_diff > max_diff or (cur_diff == max_diff and cur_a > max_a):
        max_diff = cur_diff
        max_a = cur_a
        max_b = cur_b
print(f'{max_a} {max_b}')
