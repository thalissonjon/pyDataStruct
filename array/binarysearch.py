arr = [-1, 0, 3, 5, 9, 12]

def binarysearch(arr, value):
    l, r = 0, len(arr)-1

    while l<=r:
        m = (l + r)//2
        print(f'valor de m: {m}')
        print(f'valor de l: {r}')
        print(f'valor de r: {r}')
        print('----------')
        if value > arr[m]:
            l = m+1
        elif value < arr[m]:
            r = m-1
        
        else:
            return m
        
    return False


print(binarysearch(arr, 5))