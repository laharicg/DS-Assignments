def rotation():
    arr=[int(x) for x in input().split(',')]
    result = [0]*len(arr)
    k=int(input("How many steps?"))
    for i in range(len(arr)):
        if i+k < len(arr):
            result[i+k] = arr[i]
        else:
            new_index = (i+k) % len(arr)
            result[new_index] = arr[i]
return result
print(rotation())