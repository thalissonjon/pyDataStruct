arr = [22, 11, 88, 66, 55, 77, 33, 44]

def mergesort(arr):
    if len(arr) > 1:
        leftarr = arr[:len(arr)//2]
        rightarr = arr[len(arr)//2:]

        mergesort(leftarr)
        mergesort(rightarr)

        # merge
        i = 0 # esq idx
        j = 0 # dir idx
        k = 0 # merged idx

        while i < len(leftarr) and j < len(rightarr):
            if leftarr[i] < rightarr[j]:
                arr[k] = leftarr[i]
                i += 1
            else:
                arr[k] = rightarr[j]
                j += 1
            k += 1
        
        while i < len(leftarr):
            arr[k] = leftarr[i]
            i += 1
            k += 1
        
        while j < len(leftarr):
            arr[k] = rightarr[j]
            j += 1
            k += 1


mergesort(arr)
print(arr)