
# ref: https://qiita.com/drken/items/23a4f604fa3f505dd5ad


def fibo(n: int)-> int:
    # base case
    if n == 0: return 0
    if n == 1: return 1

    # rec call
    return fibo(n-1) + fibo(n-2)

def fibo_memo(n: int, memo: list)-> int:
    # base case
    if n == 0: return 0
    if n == 1: return 1
    
    if memo[n] is not -1: return memo[n]
    memo[n] = fibo(n-1) + fibo(n-2)

    return memo[n]

if __name__ == "__main__":
    MAX = 30

    # O(2^n)
    l_rec = []
    for i in range(MAX):
        l_rec.append(fibo(i))
    print(l_rec)

    l_rec = []
    l_memo = [-1 for i in range(MAX)]
    for i in range(MAX):
        l_rec.append(fibo_memo(i, l_memo))
    print(l_rec)

    # O(n)
    l_f = [0, 1]
    for i in range(2, MAX):
        l_f.append(l_f[i-1] + l_f[i-2])
    print(l_f)