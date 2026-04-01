# Largest No in a array
def find_max():
    arr=[1,2,3,4,5]
    max_digit=0
    start=arr[0]
    i=0

    while i <len(arr):
        if arr[i] > max_digit:
            max_digit=arr[i]
            
        i +=1
    return (max_digit)

print(find_max())
        