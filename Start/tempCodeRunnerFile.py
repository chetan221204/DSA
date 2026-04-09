def maxSubArray(nums): 
   
   maxi = float('-inf')
   for i in range(len(nums)):
        
       for j in range(i, len(nums)):
           sum = 0
           
           for k in range(i, j + 1):
               sum += nums[k]
           maxi = max(maxi, sum)
           
   return maxi

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxSum = maxSubArray(arr)
print("The maximum subarray sum is:", maxSum)