
n = int(input())
S = list(map(int, input().split()))

q = int(input())
T = list(map(int, input().split()))

cnt=0
for t in T:
    for s in S:
        if t == S:
            cnt += 1
            break

print(cnt)