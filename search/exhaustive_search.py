
n = int(input())
A = list(map(int, input().split()))

q = int(input())
M = list(map(int, input().split()))

S = [0 for _ in range(len(A))]

res = 0
def solve(i, m):
    if m == 0:
        return True
    else:
        if i<=n-1:
                   #A[i]を使用しなかった場合 #A[i]を使用した場合
            return solve(i+1, m) or solve(i+1, m-A[i])
        else:
            return False
        
for m in M:
    if solve(0,m):
        print("yes")
    else:
        print("no")

    