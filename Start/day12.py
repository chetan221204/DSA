# def reverse(arr,start,end):
#     while start <end:
#         arr[start],arr[end]=arr[end],arr[start]
#         start+=1
#         end-=1
# def rotate(arr,k):
#     n=len(arr)
#     reverse(arr,0,k-1)
#     reverse(arr,k,n-1)
#     reverse(arr,0,n-1)

#     # reverse(arr,0,n-1)
#     # reverse(arr,0,k-1)
#     # reverse(arr,k,n-1)  
#     return arr
# arr=[1,2,3,4,5]
# print(rotate(arr,2))       
 

# arr=[1,1,2,2,3,3,34,4,4,5,5]
# yo=set(arr)
# print(yo) 


# def dublicate(arr):
#     n=len(arr)
#     i=0
#     for j in range(1,n):
#         if(arr[j]!=arr[i]):
#             arr[i+1]=arr[j]
#             i+=1
#     return (arr[:i+1])


# arr=[1,1,2,2,3,3,34,4,4,5,5]
# print(dublicate(arr))


arr=[1,3,0,3,0,0,3,6,0,0,7]
j=0
for i in range(len(arr)):
    if(arr[i]!=0):
        arr[i],arr[j]=arr[j],arr[i]
        j+=1

print(arr)