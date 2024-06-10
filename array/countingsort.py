arr = [1,0,3,1,3,1]
# arr = [14, 50, 10, 7, 31, 91, 25, 56, 27, 34]

def countingsort(arr):
    # maximum value
    max = arr[0]
    for i in arr:
        if i>max:
            max = i
    
    # arr with range 0 to max
    auxArr = [0] * max 
    print(auxArr)
    # i=0
    # while i<=max: # <= to add element 0 
    #     auxArr.append(0)
    #     i+=1
    
    # element count
    for i in arr:
        auxArr[i] += 1

    # sum to next
    lastNumber = 0
    i=0
    while i!=len(auxArr):
        auxArr[i] += lastNumber 
        lastNumber = auxArr[i]
        i+=1
    
    orderedarr = [0] * len(arr)
    # print(auxArr)

    for i in range(len(arr)-1, -1, -1):
        value = arr[i]
        pos = auxArr[value]-1
        orderedarr[pos] = value

        auxArr[value] -= 1
        
    
    print(orderedarr)
    
    

countingsort(arr)