n = int(input())
S = list(map(int, input().split()))

q = int(input())
T = list(map(int, input().split()))

S.sort()
cnt=0
for t in T:
    left = 0
    right = len(S)
    while(left < right):
        mid = (left + right ) //2
        if(t == S[mid]):
            cnt += 1
            break
        elif(t < S[mid]):
            right = mid
            continue
        elif(t > S[mid]):
            left  = mid+1
            continue

print(cnt)