# Union Of Two Sorted Arrays:

def union_of_arrays(arr1, arr2):
    i = 0
    j = 0
    
    while i<len(arr1) and j<len(arr2):
        
        if arr1[i] == arr1[i-1] and i>0:
            i += 1
        
        elif arr2[j] == arr2[j-1] and j>0:
            j += 1
            
        elif arr1[i] < arr2[j]:
            print(arr1[i], end=" ")
            i += 1
            
        elif arr2[j] < arr1[i]:
            print(arr2[j], end=" ")
            j += 1
            
        else: # arr1[i] == arr2[j]
        # print anyone else no issue
            print(arr1[i], end=" ")
            i += 1
            j += 1
            
    while i < len(arr1):
        if i > 0 and arr1[i] != arr1[i-1]:
            print(arr1[i], end=" ")
        i += 1
                
    while j < len(arr2):
        if j > 0 and arr2[j] != arr2[j-1]:
            print(arr2[j], end=" ")
        j += 1

if __name__ == "__main__":
    arr1 = [2, 20, 20, 40]
    arr2 = [1, 10, 20]
    union_of_arrays(arr1, arr2)