# arr=[1,3,0,3,0,0,3,6,0,0,7]
# j=0
# for i in range(len(arr)):
#     if arr[i]!=0:
#         arr[i],arr[j]=arr[j],arr[i]
#         j+=1
# print(arr)

# arr=[1,3,0,3,0,0,3,6,0,7]
# k=7
# for i in range(len(arr)):
#     if(arr[i]==k):
#         print(i)


# def union(arr1, arr2):
#     s = set()    
#     for i in range(len(arr1)):
#         s.add(arr1[i])

#     for i in range(len(arr2)):
#         s.add(arr2[i])

#     result = list(s)
#     return result


# arr1 = [10, 2, 30, 4]
# arr2 = [25, 1, 7]

# print(union(arr1, arr2))


def findUnion(arr1, arr2):
        # List to store union elements
        Union = []

        # Initialize pointers
        i, j = 0, 0
        n, m = len(arr1), len(arr2)

        # Iterate while both pointers are within array bounds
        while i < n and j < m:
            # If element in arr1 is smaller
            if arr1[i] < arr2[j]:
                # Add if empty or not duplicate
                if not Union or Union[-1] != arr1[i]:
                    Union.append(arr1[i])
                i += 1
            # If element in arr2 is smaller
            elif arr2[j] < arr1[i]:
                # Add if empty or not duplicate
                if not Union or Union[-1] != arr2[j]:
                    Union.append(arr2[j])
                j += 1
            else:
                # Elements are equal, add once if not duplicate
                if not Union or Union[-1] != arr1[i]:
                    Union.append(arr1[i])
                i += 1
                j += 1

        # Append remaining elements from arr1
        while i < n:
            if not Union or Union[-1] != arr1[i]:
                Union.append(arr1[i])
            i += 1

        # Append remaining elements from arr2
        while j < m:
            if not Union or Union[-1] != arr2[j]:
                Union.append(arr2[j])
            j += 1

        # Return the union list
        return Union


# Driver code
 
arr1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
arr2 = [2, 3, 4, 4, 5, 11, 12]

print(findUnion(arr1, arr2))
    