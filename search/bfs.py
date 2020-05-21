"""
input:
4
1 2 2 4
2 1 4
3 0
4 1 3
"""
import numpy as np
from collections import deque
INF = 100000000

def bfs(root: int, M: list):
    q = deque([root])
    n = len(M)
    d = np.full(n, INF)
    d[root] = 0
    while len(q) > 0:
        u = q.popleft()
        for v in range(n):
            if M[u][v] == 0: continue
            if d[v] != INF: continue
            d[v] = d[u] + 1
            q.append(v)
    return d
    
if __name__ == "__main__":
    n = int(input())
    M = np.zeros((n, n),dtype=np.int) #隣接行列
    
    for _  in range(n):
        a = list(map(int, input().split()))
        u = a[0]
        k = a[1]
        for v in a[2:]:
            M[u-1][v-1] = 1
    
    print(M)#隣接行列
    res = bfs(0,M)

    for i, depth in enumerate(res):
        print(i+1, depth)
        
    
    
    
    
