def hoarePartition(arr, l, h):
    pivot = arr[l]
    i = l - 1
    j = h + 1
    
    while True:
        # Left se pehla element dhoondho jo pivot se bada ya barabar hai
        i = i + 1
        while arr[i] < pivot:
            i = i + 1
            
        # Right se pehla element dhoondho jo pivot se chhota ya barabar hai
        j = j - 1
        while arr[j] > pivot:
            j = j - 1
            
        # Agar pointers cross kar gaye, toh partition poora ho gaya
        if i >= j:
            return j
            
        # Galat jagah par mile elements ko swap karo
        arr[i], arr[j] = arr[j], arr[i]

# Example
arr = [5, 3, 8, 4, 2, 7, 1, 10]
split_index = hoarePartition(arr, 0, len(arr) - 1)

print("Partitioned Array:", arr)
print("Split Index:", split_index) 
# Output might be:
# Partitioned Array: [1, 3, 2, 4, 8, 7, 5, 10]
# Split Index: 3 
# (Elements <= 5 are on the left of index 3, and elements >= 5 are on the right)