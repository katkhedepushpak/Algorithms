def best(W, l):
    n = len(l)
    best = [[0]*(n+1) for i in range(W+1)]
    back = [[0]*(n+1) for i in range(W+1)]
    for P in range(1, n+1):
        for X in range(W+1):
            maxi = 0
            c = 0
            for k in range(1, l[P-1][-1]+1):
                CW = k*l[P-1][0]
                if CW <= X:
                    t = best[X-CW][P-1] + k*l[P-1][1]
                    if t > maxi:
                        maxi = t
                        c = k
            best[X][P] = maxi
            if maxi != 0:
                back[X][P] = c
            else:
                back[X][P] = 0
    X = W
    P = n
    qty = [0] * n
    while back[X][P] > 0:
        qty[P-1] = back[X][P]
        X -= back[X][P] * l[P-1][0]
        P -= 1
    return (best[-1][-1], qty)


W, l = 92, [(1, 6, 6), (6, 15, 7), (8, 9, 8), (2, 4, 7), (2, 20, 2)]
ans = best(W, l)
print(ans)