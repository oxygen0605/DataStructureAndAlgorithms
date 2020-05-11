# ref: https://qiita.com/drken/items/23a4f604fa3f505dd5ad

def rec(i, x, a):
    # base case
    if i == 0:
        if x == 0: return True
        else: return False
    
    # a[i-1]を選ばなかった時　または　a[i-1]を選んだとき
    if rec(i-1, x, a) or rec(i-1, x-a[i-1], a):
        return True

    # どちらもダメだった時
    return False

def rec_memo(i, x, a, dp):
    # base case
    if i == 0:
        if x == 0: return True
        else: return False
    
    # check memo
    if dp[i][x] != -1: return dp[i][x]

    if rec_memo(i-1, x, a, dp) is True:
        dp[i][x] = True
        return dp[i][x]
    
    if rec_memo(i-1, x-a[i-1], a, dp) is True:
        dp[i][x] = True
        return dp[i][x]
    
    dp[i][x] = False
    return dp[i][x]

if __name__ == "__main__":
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    if rec(n, x, arr):
        print("Yes")
    else:
        print("No")

    dp = [[-1 for j in range(1000)] for i in range(n+1)]
    if rec_memo(n, x, arr, dp):
        print("Yes")
    else:
        print("No")