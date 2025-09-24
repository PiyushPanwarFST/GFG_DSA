a = [10, 15, 20]
b = [5, 6, 6, 30, 40]

def merge(a, b):
    i = 0
    j = 0
    c = []

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        elif a[i] > b[j]:
            c.append(b[j])
            j += 1
    return c + a[i:] + b[j:]

print(merge(a, b))