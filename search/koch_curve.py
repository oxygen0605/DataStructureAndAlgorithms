import math as mt
n = int(input())

def local_koch(i, x1, y1, x2, y2):
    
    if i == n:
        return 
    else:
        dx = x2 - x1
        dy = y2 - y1
        if(dx < 0): print("here: ", i, x2, x1)

        xs = x1 + dx/3
        ys = y1 + dy/3
        xu = x1 + dx/2
        yu = y1 + xu/mt.sqrt(3)
        xt = x1 + 2*dx/3
        yt = y1 + 2*dy/3

        print('{:.8f}'.format(xs), '{:.8f}'.format(ys))
        print('{:.8f}'.format(xu), '{:.8f}'.format(yu))
        print('{:.8f}'.format(xt), '{:.8f}'.format(yt))
        
        local_koch(i+1, x1, y1, xs, ys)
        local_koch(i+1, xs, ys, xu, yu)
        local_koch(i+1, xu, yu, xt, yt)
        local_koch(i+1, xt, yt, x2, y2)

x1 = 0.0
y1 = 0.0
x2 = 100.0
y2 = 0.0

print('{:.8f}'.format(x1), '{:.8f}'.format(y1))
local_koch(0, x1, y1, x2, y2)
print('{:.8f}'.format(x2), '{:.8f}'.format(y2))

        
        

        
        
