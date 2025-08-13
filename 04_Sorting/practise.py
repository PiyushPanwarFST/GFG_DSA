#  Sorting Portion start:


# def binarySearch(arr, x):
#     low = 0
#     high = len(arr) - 1
#     mid = low+ high // 2

#     for i in range(low, high + 1):
#         if arr[mid] == x:
#             return mid
#         elif arr[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
#         mid = low + (high - low) // 2
#     return -1

# if __name__ == "__main__":
#     arr = [2, 3, 4, 10, 40]
#     x = 10
#     result = binarySearch(arr, x)
#     if result != -1:
#         print(f"Element is present at index {result}")
#     else:
#         print("Element is not present in array")


# def binarySearch(arr, k):
#     start = 0
#     end = len(arr) - 1
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] == k:
#             if mid == len(arr) - 1 or arr[mid] != arr[mid + 1]:
#                 return mid
#             else:
#                 start = mid + 1
#         elif arr[mid] < k:
#             start = mid + 1
#         else:
#             end = mid - 1   
#     return -1

# print(binarySearch([1, 2, 2, 2, 3, 4], 2))  # Output: 4
# print(binarySearch([1, 2, 3, 4, 5], 6))  # Output: -1
# print(binarySearch([1, 2, 3, 4, 5], 1))  # Output: 1


def countOnes(arr):
    n = len(arr)
    l, r = 0, n - 1
    first_one = n  # default: no 1 found
    while l <= r:
        m = (l + r) // 2
        if arr[m] == 1:
            first_one = m
            r = m - 1  # left side me bhi 1 ho sakta hai
        else:
            l = m + 1
    return n - first_one

print(countOnes([1, 1, 1, 1, 1, 0, 0, 0]))