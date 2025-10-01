def countInversion(arr,l,h):
    res = 0
    if (l < h):
        m = (l+h)//2
        res += countInversion(arr,l,m)
        res += countInversion(arr,m+1,h)
        res += countMerge(arr,l,m,h)
    return res

def countMerge(arr, l, m, h):
    left = arr[l : m+1]
    right = arr[m+1 : h+1]
    res, i, j, k = 0, 0, 0, l
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            k += 1
            i += 1
            
        else:
            arr[k] = right[j]
            k += 1
            j += 1
            res += len(left) - i
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    
    return res

if __name__ == "__main__":
    arr = [2,5,8,11,3,6,9,13]
    l = 0
    h = len(arr) - 1
    print("Number of inversions:", countInversion(arr,l,h))