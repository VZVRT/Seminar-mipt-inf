#N1
'''def fib (n):
    if n==0 or n==1:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(5))'''
#N2
'''num=int(input('Число:'))
for i in range(1,num+1):
    if (num%i==0):
        print(i)'''
#N3
'''def gcd(a, b):
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return b
a,b=map(int,input().split())
print(gcd(a,b))
#N4
def triangle(h,depth=1,symbol='C'):
    if h%2!=0 and depth==h//2+1:
        print(symbol*depth)
        return
    if h % 2 == 0 and depth == h // 2:
        print(symbol * depth)
        print(symbol * depth)
        return
    print(symbol*depth)
    triangle(h, depth=depth+1)
    print(symbol * depth)
triangle(14)'''
#N5
'''def n5():
    n, m = map(int, input().split())
    a = [[0] * m for _ in range(n)]
    i, j, d = 0, 0, 0
    moves = ((0, 1,), (1, 0,), (0, -1,), (-1, 0,),)
    for k in range(1, n * m + 1):
        a[i][j] = k
        for l in range(4):
            newD = (d + l) % 4
            di, dj = moves[newD]
            newI, newJ = i + di, j + dj
            if 0 <= newI < n and 0 <= newJ < m and a[newI][newJ] == 0:
                i, j, d = newI, newJ, newD
                break
    for row in a:
        print(*row)
n5()'''








