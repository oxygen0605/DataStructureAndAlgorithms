
# Open Hash法 アクセススピードはO(1)

L = 14
M = 1046527
H = ["null" for i in range(M)]

def getChar(c: str)-> int:
    ret = 0
    if c == "A": ret = 1
    elif c == "C": ret = 2
    elif c == "G": ret = 3
    elif c == "T": ret = 4
    return ret

# 文字列から数値へ変換してKeyを生成する
def getKey(s: str)-> int:
    sum = 0
    p = 1
    for c in s:
        sum += p * (getChar(c))
        p *= 5
    return sum
        
def h1(key: int)-> int:
    return key % M        

def h2(key: int)-> int:
    return 1 + (key % (M-1))

def find(s: str)-> int:
    key = getKey(s)
    i = 0
    while(1):
        h = (h1(key) + i * h2(key)) % M
        if (H[h] == s):
            return 1
        elif(H[h] == "null"):
            return 0
        else:
            i += 1

def insert(s: str)-> int:
    key = getKey(s)
    i = 0
    while(1):
        h = (h1(key) + i * h2(key)) % M
        if (H[h] == s):
            return 1
        elif(H[h] == "null"):
            H[h] = s
            return 0
        else:
            i += 1


if __name__ == "__main__":
    
    n = int(input())
    for i in range(n):
        com, key = input().split()

        if com == "insert":
            insert(key)
        elif com == "find":
            if find(key):
                print("yes")
            else:
                print("no")

    
    
