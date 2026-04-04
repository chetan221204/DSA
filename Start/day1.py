# def Largest_Element(arr):
#     n=len(arr)
#     max_digit=arr[0]
#     for i in range(n):
#         if(arr[i]>max_digit):
#             max_digit=arr[i]

#     # return max_digit
#     s_largest=0
#     for i in range(n):
#         if(arr[i]>s_largest and arr[i]!=max_digit):
#             s_largest=arr[i]
#     return s_largest

# arr=[12,43,12,65,2,6,99]
# print(Largest_Element(arr))

# def smallest(arr):
#     n=len(arr)
#     low = arr[0]
#     for i in range(n):
#         if(arr[i]<low):
#             low=arr[i]
#     # return low

#     s_smallest=arr[0]
#     for i in range(n):
#         if(arr[i]<s_smallest and arr[i]!=low):
#             s_smallest=arr[i]
#     return s_smallest

# arr=[12,43,12,65,2,6,99]
# print(smallest(arr))


# def S_Largest(arr):
#     n=len(arr)
#     largest=float('-inf')  #INT_MAX
#     # largest=arr[0]
#     s_largest=0
#     for i in range(1,n):
#         if (arr[i]>largest):
#             s_largest=largest
#             largest=arr[i]
#         elif(arr[i]<largest and arr[i]>s_largest):
#             s_largest=arr[i]
#     return s_largest

# def ssmallest(arr):
#     n=len(arr)
#     smallest=float('+inf')
#     ssmallest=float('+inf')
#     for i in range(n):
#         if(arr[i]<smallest ):
#             ssmallest=smallest
#             smallest=arr[i]
#         elif(arr[i]!=smallest and arr[i]<ssmallest):
#             ssmallest=arr[i]

#     return ssmallest


# arr=[2,54,23,65,33]
# print(S_Largest(arr))
# print(ssmallest(arr))


# def sorted(arr):
#     n=len(arr)

#     for i in range(1,n):
#         if (arr[i]>=arr[i-1] ):
#             {

#             }
#         else:
#             return False    
#     return True

# arr=[1,2,3,4,5,6]
# print(sorted(arr))

# No dublicate in a array


# def dublicate(arr):
#     n=len(arr)
#     i=0
#     for j in range(1,n):
#         if(arr[j]!=arr[i]):
#             arr[i+1]=arr[j]
#             i+=1
#     print(arr[:i+1])
#     return i+1

        
# arr=[1,1,1,1,2,2,3,3,3,3,3,4]
# print(dublicate(arr))
