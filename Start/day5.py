# def two_sum_indices(arr,target):
#     seen = {}
#     for i in range(len(arr)):

#         num=arr[i]
#         need=target-num
#         if need in seen:
#             return [seen[need],i]
#         seen[num]=i         

        
# arr = [2, 6, 5, 8, 11]
# target = 14
# print( two_sum_indices(arr,target))
 


# def two_sum(arr,target):
#     start=0
#     end=len(arr)-1
#     while start < end:
#         if((arr[start]+arr[end])==target):
#             return [arr[start],arr[end]]
#         elif(arr[start]+arr[end]>target):
#             end-=1
#         # elif(arr[start]+arr[end]<target):
#         else:
#             start+=1
        


# arr = [2, 6, 5, 8, 11]
# target = 14
# print( two_sum(arr,target))
 

# arr=[1,0,2,0,1,2]
# count0,count1,count2=0,0,0
# for i in range(len(arr)):
#     if(arr[i]==0):
#         count0+=1
#     elif(arr[i]==1):
#         count1+=1
#     else:
#         count2+=1

# for i in range(count0):
#     arr[i]=0
# for i in range(count0,count0 + count1):
#     arr[i]=1
# for i in range(count0+count1,len(arr)):
#     arr[i]=2

# print(count0,count1,count2)
# print(arr)


# arr=[0,1,1,0,1,2,1,2,0,0,0]
# n=len(arr)
# low=0
# mid=0
# high=n-1
# while mid <=high:
#     if(arr[mid]==0):
#         arr[low],arr[mid]=arr[mid],arr[low]
#         low+=1
#         mid+=1
#     elif(arr[mid]==1):
#         mid+=1
#     elif(arr[mid]==2):
#         arr[mid],arr[high]=arr[high],arr[mid]
#         high-=1
# print(arr)


 
# def majorityElement(nums):
#     n = len(nums)
    
#     # Hash map to store element counts
#     mp = {}
    
#     # Count occurrences of each element
#     for num in nums:
#         if num in mp:
#             mp[num] += 1
#         else:
#             mp[num] = 1
    
#     """ Iterate through the map to
#     find the majority element"""
#     for num, count in mp.items():
#         if count > n // 2:
#             return num
    
#     # Return -1 if no majority element is found
#     return -1
# arr = [2, 2, 1, 1, 1, 2, 2]
# print(majorityElement(arr))



# def mostelement(arr):
#     n=len(arr)
#     map={}
#     for num in arr:
#         if num in map:
#             map[num]+=1
#         else:
#             map[num]=1
#     for num,count in map.items():
#         if count>n//2:
#             return num
# arr = [2, 2, 1, 1, 1, 2, 2]
# print(mostelement(arr))




arr=[7,7,5,7,5,1,5,7,5,5,7,7,5,5,5,5]
count =0

for i in range(len(arr)):
    if(count==0):
        count=1
        ele=arr[i]
    elif(arr[i]==ele):
        count+=1
    else:
        count-=1
count1=0
for i in range(len(arr)):
    if(arr[i]==ele):
        count1+=1
    print(ele)

print(ele,"->",count)
 