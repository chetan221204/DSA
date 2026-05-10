# def nCr(n,r):
#     result=1
#     for i in range(r):
#         result=result*(n-i)
#         result=result//(i+1)
#     return result
# def line(k):
#     for r in range(k):
#         print(nCr(k-1,r),end=" ")
        
# (line(5))
# print(nCr(4,3,))
 
# ans=1
# n=5
# print((ans),end=" ")
# for i in range(1,n):
#     ans=ans*(n-i)
#     ans=ans//(i)
#     print((ans),end=" ")


def nCr(n, r):
    result = 1
    for i in range(r):
        result = result * (n - i)
        result = result // (i + 1)
    return result

def pascal_triangle(rows):
    for n in range(rows):
        for r in range(n + 1):
            print(nCr(n, r), end=" ")
        print()

pascal_triangle(3)