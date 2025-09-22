# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst-case time complexity is quite high.

# If there are n(4) elements when we will have n-1(3) passes because the last element will be automatically sorted okay which includes the index [0,1,2].

# so for n No. of passes we have external loop haveing the range upto (n-1) becuase althrough haveing 3 passes but still need to upto only (2- index) & for comparing adjacent elements we have internal loop have range (n-i-1) becuase if last element is sorted we don't have to compare it again.

# def bubbleSort(l):
#     n = len(l)

#     for i in range(n-1):

#         for j in range(n - i-1):
#             if l[j] > l[j + 1]:
#                 l[j], l[j + 1] = l[j + 1], l[j]


# l = [10, 8, 20, 5]

# bubbleSort(l)

# print(*l)

# Optimized way of Bubble Sort if our list is already sorted then it will not go for further passes, we directly marked True that it is sorted no need for further passes.

# def bubbleSort(l):
#     n = len(l)

#     for i in range(n-1):
#         swapped = False

#         for j in range(n-i-1):
#             if l[j]>l[j+1]:
#                 l[j],l[j+1] = l[j+1],l[j]

#                 swapped = True

#         if swapped == False:
#             return

# l = [10, 8, 20, 5]

# bubbleSort(l)

# print(*l)
