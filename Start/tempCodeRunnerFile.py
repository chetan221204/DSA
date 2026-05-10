def nCr(n,r):
    result=1
    for i in range(r):
        result=result*(n-i)
        result=result//(i+1)
    return result
def line(k):
    for r in range(k):
        print(nCr(k-1,r))
        
(line(5))