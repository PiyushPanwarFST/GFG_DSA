a = [10,15,20,11,13]
low = 0
high = 4
mid = 2

def merge_subarray(a, low, mid, high):
    i = low
    j = mid + 1
    c = []

    while i <= mid and j <= high:
        if a[i] < a[j]:
            c.append(a[i])
            i += 1
        elif a[i] > a[j]:
            c.append(a[j])
            j += 1

    while i <= mid:
        c.append(a[i])
        i += 1

    while j <= high:
        c.append(a[j])
        j += 1
    
    return c

print(merge_subarray(a, low, mid, high))