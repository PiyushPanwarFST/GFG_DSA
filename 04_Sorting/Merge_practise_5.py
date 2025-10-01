# Partition of Given Array:

def partition_of_array(arr, p):
    n = len(arr)
    arr[p], arr[n-1] = arr[n-1], arr[p]
    
    temp = []
    
    for x in arr:
        if x <= arr[n-1]:
            temp.append(x)
    
    for x in arr:
        if x > arr[n-1]:
            temp.append(x)
            
    for i in range(len(arr)):
        arr[i] = temp[i]

if __name__ == "__main__":
    arr = [3,8,6,12,10,7]
    p = 5  
    print("Original array:", arr)
    partition_of_array(arr, p)
    print("After partition:", arr)
