#N1
# def year(n):
#     if n%4==0 and n%100!=0 or n%400==0:
#         return 'YES'
#     else:
#         return 'NO'
# print(year(2044))
#N2
# a = int(input())
# b = int(input())
# c = int(input())
# if (a+b)>c and (b+c)>a and (a+c)>b and a>0 and b>0 and c>0:
#     print('YES')
# else:
#     print('NO')
#N3
# a=float(input())
# b=float(input())
# c=float(input())
# d=(b**2)-4*a*c
# l=2*a
# if a==0 and b==0 and c!=0:
#     print('False')
# if a==0 and b==0 and c==0:
#     print('True')
# if a==0 and b!=0:
#     x1=(-c/b)
#     print(x1)
# else:
#     if d==0:
#         x1=(-b/2*a)
#         print(x1)
#     elif d>0:
#         x1=((-b+(d**0.5))/l)
#         x2=((-b-(d**0.5))/l)
#         print(x1,x2)
#N4
# a1 = int(input())
# a2 = int(input())
# b1 = int(input())
# b2 = int(input())
# if abs(a1-b1)==abs(a2-b2) or (a1==b1) or (a2==b2):
#     print('YES')
# else:
#     print('NO')
#N5
# input()
# a, b, t=list(input().split()), input(), 0
# for i in a:
#     if i==b:
#         t+=1
# print(t)
#N6
# input()
# stroka, res=list(input().split()), 0
# for i in stroka:
#     if int(i)>0:
#         res+=1
# print(res)
#N7
# input()
# a=list(input().split())
# for i in range (len(a)-1):
#     a[len(a)-1-i], a[len(a)-2-i]= a[len(a)-2-i], a[len(a)-1-i]
# print(*a)
#N8
# input()
# f=list(input().split())
# maximum=0
# for i in range(len(f)):
#     if int(f[i])>maximum:
#         maximum=int(f[i])
# print(maximum)
#N9
#input()
# m = []
# s = list(input().split())
# for x in s:
#     m.append(int(x))
# def sort(s):
#     if len(s) <= 1:
#         return s
#     start = s[0]
#     right = list(x for x in s if x > start)
#     central = list(x for x in s if x == start)
#     left = list(x for x in s if x < start)
#     A = sort(left) + central + sort(right)
#     return A
# print(sort(m)[0], sort(m)[1])