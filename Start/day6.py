# def maxSubArray(arr): 
#    maxi = float('-inf')
#    for i in range(len(arr)):  
#        for j in range(i, len(arr)):
#            sum = 0           
#            for k in range(i, j + 1):
#                sum += arr[k]
#            maxi = max(maxi, sum)           
#    return maxi
# arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# maxSum = maxSubArray(arr)
# print("The maximum subarray sum is:", maxSum)



def maxsub(arr):
    maxi=float('-inf')
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum=0
            for k in range(i,j+1):
                sum+=arr[k]
            maxi=max(maxi,sum)
    return maxi
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxsub(arr))