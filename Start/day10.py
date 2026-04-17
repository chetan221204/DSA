# arr = [7, 1, 5, 3, 6, 4]
# profit=0
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#         maxi=arr[j]-arr[i]
#         profit=max(profit,maxi)

# print(profit)


# arr = [7, 1, 5, 3, 6, 4]
# min_num=float('inf')
# max_profit=0
# for i in arr:
#     if(i<min_num):
#         min_num=i
#     else:
#         max_profit=max(max_profit,i-min_num)
# print(max_profit)


# arr=[3,-2,1,-5,2,-4]
# start=0
# end=1
# for i in range(len(arr)):
#     if(start>1)


# def rearrange_by_sign(A):
#         n = len(A)
#         ans = [0] * n  # Initialize result array with zeros

#         pos= 0  # Even indices for positive numbers
#         neg = 1  # Odd indices for negative numbers

#         for i in range(n):
#             if A[i] < 0:
#                 # Place negative at odd index
#                 ans[neg] = A[i]
#                 neg += 2
#             else:
#                 # Place positive at even index
#                 ans[pos] = A[i]
#                 pos += 2

#         return ans

# A = [-3,1,-2,-5,2,4]
# print(rearrange_by_sign(A) )


# arr=[3,-2,1,-5,2,-4]
# n=len(arr)
# ans=[0]*n
# start=0
# end=1
# for  i in range(n):
#     if(arr[i]<0):
#         ans[end]=arr[i]
#         end +=2
#     else:
#         ans[start]=arr[i]
#         start+=2
# print(ans)

arr=[3,-2,1,-5,2,-4]
# arr=[3,-2,1,-5,2,-4,-2,-4]
n=len(arr)
pos=[]
nev=[]
for i in range(n):
    if(arr[i]<0):
        nev.append(arr[i])
    else:
       pos.append(arr[i])
# for i in range(len(pos)):
#     arr[2*i]=pos[i]
#     arr[2*i+1]=nev[i]
k=len(nev)
j=len(pos)
if(len(pos)>len(nev)):
    for i in range(len(nev)):
        arr[2*i]=pos[i]
        arr[2*i+1]=nev[i]
    index=k*2
    for i in range(k,j):
        arr[index]=pos[i]
        index+=1    
if(len(nev)>len(pos)):
    for i in range(j):
        arr[i*2]=pos[i]
        arr[i*2+1]=nev[i]
    index=j*2
    for i in range(j,k):
        arr[index]=nev[i]
        index+=1    

print(pos)
print(nev)
print(arr)