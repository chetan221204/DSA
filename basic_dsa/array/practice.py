# def largest(arr):
#     n=len(arr)
#     max_digit=float('-inf')
#     smax=0
#     for i in range(n):
#         if(arr[i]>max_digit):
#             max_digit=arr[i]
#     for i in range(n):
#         if(arr[i]>smax and arr[i]!=max_digit):
#             smax=arr[i]
#     return smax

# arr=[1,2,3,4,5,56]
# print(largest(arr))


# def largest(arr):
#     n=len(arr)
#     largest=float('-inf')
#     slargest=0
#     for i in range(n):
#         if (arr[i]>largest):
#             slargest=largest
#             largest=arr[i]

#         elif(arr[i]<largest and arr[i]>slargest):
#             slargest=arr[i]

#     return slargest

# arr=[1,2,3,4,5,56]
# print(largest(arr))


# arr=[1,2,3,4,5]
# all_true=True
# for i in range(1,len(arr)):
#     if arr[i]>arr[i-1]:
#         { 

#         }
#     else:
#         all_true=False
# print(all_true)

# def dublicate(arr):
#     i=0
#     for j in range(1,len(arr)):
#         if(arr[j]!=arr[i]):
#             arr[i+1]=arr[j]
#             i+=1
#     return (arr[:i+1])

# arr=[1,1,2,2,3,3]
# print(dublicate(arr))

# def rotate(arr):
#     n=len(arr)
#     first=arr[0]
#     for i in range(n-1):
#         arr[i]=arr[i+1]

#     arr[n-1]=first   

#     return arr

# arr=[1,2,3,4,5]
# print(rotate(arr))


# def reverse(arr,start,end):
#     while start <end:
#         arr[start] ,arr[end]=arr[end],arr[start]
#         start +=1
#         end-=1

# def rotate(arr,k):

#     n=len(arr)
#     # k=k%n
#     reverse(arr,0,k-1)
#     reverse(arr,k,n-1)
#     reverse(arr,0,n-1)

#     return arr

# arr=[1,2,3,4,5]
# print(rotate(arr,2))


# def zeros(arr):
    
#     j=0
#     for i in range(len(arr)):
#         if arr[i]!=0:
#             arr[i],arr[j]=arr[j],arr[i]
#             j+=1
#     return arr
    
# arr=[1,2,0,0,3,0,0,4,5]
# print(zeros(arr))


# arr=[1,2,3,4,5,6,7]
# k=5
# for i in range(len(arr)):
#     if(arr[i]==k):
#         print(i)


