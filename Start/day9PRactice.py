# a=5
# fact=1
# for i in range(1,a+1):
#     fact=fact*i
#     print(fact) 

# a=5
# fact=1
# while a!=0:
#     fact=fact*a
#     a=a-1
# print(fact)

def fact(n):
    if(n==0 or n==1):
        return 1
    return n*fact(n-1)

print(fact(4))