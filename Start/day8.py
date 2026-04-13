# arr=[-2,-3,4,-1,-2,1,5,-3]
arr = [1, -2, 3, 5, -1, 2]
maxi=float('-inf')
sum=0
start = 0
end = 0
s = 0
for i in range(len(arr)):
    sum=sum+arr[i]
    if(sum>maxi):
        maxi = sum
        start = s
        end = i
    if(sum<0):
        sum = 0
        s = i + 1

print(maxi)
print(arr[start:end+1])