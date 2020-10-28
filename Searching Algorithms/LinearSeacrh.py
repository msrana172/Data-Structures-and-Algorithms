def LinearSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
aList = [1, 2, 3, 4, 5, 6]        
x = 8
print("Return Index of the value : ",LinearSearch(aList, x))
