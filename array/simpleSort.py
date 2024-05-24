desorded_arr = [2,3,10,1,421,42]

def order(arr):
    order = []
    while arr:
        lowest = arr[0]
        for element in arr:
            if element < lowest:
                lowest = element
        
        order.append(lowest)
        arr.remove(lowest)

    return order


desorded_arr = order(desorded_arr)
copy = desorded_arr
print(copy)
copy2 = desorded_arr[:]
print(copy2)


        