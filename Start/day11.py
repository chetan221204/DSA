# a=[10,22,12,3,0,6]
# ans=[]
# for i in range(len(a)):
#     leader=True
#     for j in range(i+1,len(a)):
#         if(a[j]>a[i]):
#             leader=False
#     if(leader==True):
#         ans.append(a[i])

# print(ans)


# arr= [10, 22, 12, 3, 0, 6]

# ans=[]
# max_val=arr[-1]
# ans.append(arr[-1])
# for i in range(len(arr)-2,-1,-1):
#     if(arr[i]>max_val):
#         ans.append(arr[i])
#         max_val=arr[i]

# ans.reverse()

# print(ans)



# def Linear_Search(arr,k):
#     for i in range(len(arr)):
#         if arr[i]==k:
#             return True
#     return False
# arr=[102,4,100,1,101,3,2,1,1]
# max_count=1
# for i in range(len(arr)):
#     count=1
#     k=arr[i]+1
#     while(Linear_Search(arr,k)==True):
#         k+=1
#         count+=1
        
#     max_count=max(max_count,count)
# print(max_count)


def longestConsecutive(nums):
    s = set(nums)   # remove duplicates
    longest = 0

    for num in s:
         
        if num - 1 not in s:
            current = num
            count = 1

            while current + 1 in s:
                current += 1
                count += 1

            longest = max(longest, count)

    return longest 


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums))



 