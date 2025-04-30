# x = 4534
# def count_digits(x):
#     count = 0
#     while(x != 0):
#         x = x//10
#         count += 1
#     return count

# print(count_digits(x))




# x = int(input("Enter x: "))

# res = 0
# while x>0:
#     x = x//10
#     res += 1
# print(res)
    


# num = str(23436)
# for i in num[::-1]:
#     print(i, end="")



# def palindrome(temp):
#     rev = 0
#     original = temp
#     while temp != 0:
#         ld = temp%10
#         rev = rev*10 + ld
#         temp = temp//10
#     return rev == original

# temp = 23456
# print(palindrome(temp))


def factorial(num):
    fact = 1
    while num > 0:
        fact = fact * num
        num = num - 1
    return fact

print(factorial(5))