def longest(arr):
    s=set()
    for i in range(len(arr)):
        s.add(arr[i])
    return s
arr=[102,4,100,1,101,3,2,1,1]
print(longest(arr))