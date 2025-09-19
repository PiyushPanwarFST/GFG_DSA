# class Solution:
#     def moreFrequent(self, arr, x, y):
#             count_x = arr.count(x)
#             count_y = arr.count(y)
#             print(f"Count of {x}: {count_x}, Count of {y}: {count_y}")
#             if count_x == count_y:
#                 return  min(x, y)
#             else:
#                 if count_x > count_y:
#                     return x
#                 else:
#                     return y
        
# if __name__ == "__main__":
#     sol = Solution()
#     arr = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5]
#     x = 4
#     y = 5
#     print(sol.moreFrequent(arr, x, y))  # Output: 1


# def g_word(l1):
#     return [x.upper() for x in l1 if x.startswith('g')]

# print(g_word(['giraffe', 'elephant', 'giraffe', 'giraffe', 'giraffe', 'giraffe', 'giraffe']))  # Output: ['GIRAFFE', 'GIRAFFE', 'GIRAFFE', 'GIRAFFE', 'GIRAFFE']


# l = [10, 20, 5, 50]
# def get_max(l):
#     max = l[0]
#     for x in l:
#         if x > max:
#             max = x
#     return max

# print(get_max(l))  # Output: 50


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr = [10, 10, 10]
# def get_2nd_largest(arr):
#     max = arr.max()
#     second_max = arr[0]
#     for x in arr:
#         if x > second_max and x < max:
#             second_max = x
#     return second_max


# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# def sorted(arr):
#     first = arr[0]
#     i = 1
#     while first < arr[i]:
#         first = arr[i]
#         i += 1
#         if i > len(arr):
#             return True
#     return False

# print(sorted(arr))  # Output: True or False based on the sorted order of the

# def is_reverse(arr):
#     n = len(arr)
#     # ans = []
#     # for e in range(n-1, -1, -1):
#     #     ans.append(arr[e])
#     # return ans
#     s = 0
#     e = n - 1
#     while s < e:
#         arr[s], arr[e] = arr[e], arr[s]
#         s += 1
#         e -= 1
#     return arr

# print(is_reverse(arr))  # Output: [9, 18, 7, 6, 5, 4, 3, 2, 1] (reversed array)

# arr = [1,1, 2, 3, 4, 5, 6, 7, 8, 9]

# def duplicate(arr):
#     # Using a set to find unique elements
#     res = set(arr)
#     return res

# print(duplicate(arr))  # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9} (set of unique elements)




# def rotatteLeft(arr):
#     n = len(arr)
#     last = arr[0]
#     for i in range(0,n):
#         if(i == n-1):
#             arr[n-1] = last
#         else:
#             arr[i] = arr[i+1]
#     return arr
    
# print(rotatteLeft(arr))  # Output: [20, 30, 40, 50, 10] (array after left rotation)

# def roatation(arr, d):
#     arr = arr[d:] + arr[:d]
#     return arr

# print(roatation(arr, 2))  # Output: [30, 40, 50, 10, 20] (array after rotation by d positions)
# arr = [10, 20, 30, 40, 50]
# def reverse(arr):
#     return arr[::-1]

# print(reverse(arr))  # Output: [50, 40, 30, 20, 10] (reversed array)

# def printNos(n):
#         if n <= 0:
#             return
#         printNos(n - 1)
#         print(n, end=' ')

# printNos(10)

# def fact(N):
#     total = N
#     if N == 0 or N == 1:
#         return 1
#     else:
#         total *= fact(N - 1)
#     return total

# print(fact(5))  # Output: 120 (factorial of 5)

# def fact(N):
#     if N == 0 or N == 1:
#         return 1
#     else:
#         return N * fact(N - 1)


# def sum_of_digits(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + sum_of_digits(n // 10)
    
# print(sum_of_digits(2))  # Output: 10 (1 + 2 + 3 + 4 = 10)


# def palindrome(str):
#     if len(str) == 1:
#         return True
#     return str == palindrome(str.pop())

# print(palindrome("madam"))  # Output: True (since "madam" is a palindrome)