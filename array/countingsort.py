arr = [1,0,3,1,3,1]

def countingsort(arr):
    # maximum value
    max = arr[0]
    for i in arr:
        if i>max:
            max = i
    
    # arr with range 0 to max
    auxArr = [] 
    i=0
    while i<=max: # <= to add element 0 
        auxArr.append(0)
        i+=1
    
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
    
    #shift to the right
    
    print(auxArr)

countingsort(arr)