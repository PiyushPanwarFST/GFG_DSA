def intersection_of_arrays(a, b):
    i = 0
    j = 0
    
    while i<len(a) and j<len(b):
        
        if i>0 and a[i] == a[i-1]:
            i += 1
            # continue
        
        elif a[i] < b[j]:
            i += 1
            
        elif a[i] > b[j]:
            j += 1
          
        # Main comparison to find common elements
        elif a[i] == b[j]:
            
            # Agar element common hai, tab check karo ki kahin yeh duplicate toh nahi
            # if (i == 0 or a[i] != a[i-1]):
            print(a[i], end=" ")
            
            # Common element milne ke baad, dono pointers ko aage badhao
            i += 1
            j += 1

if __name__ == "__main__":
    a = [3,5,10,10,15,15,20]
    b = [5,10,10,15,30]
    # a = [5, 10, 15]
    # b = [5, 15]
    intersection_of_arrays(a, b)