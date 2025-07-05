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


# def factorial(num):
#     fact = 1
#     while num > 0:
#         fact = fact * num
#         num = num - 1
#     return fact

# print(factorial(5))



# def gcd(a, b):
#     gcd_val = 1
#     for i in range(2, min(a, b) + 1):
#         if a % i == 0 and b % i == 0:
#             gcd_val = i
#     return gcd_val

# print(gcd(36,48))



# def gcd(a, b):
#     while b > 0:
#         a, b = b, a % b
#     return a

# a = 12
# b = 15
# print(gcd(a,b))



# a = 4
# b = 6

# def LCM(a, b):
#     max_num = max(a, b)
#     while True:
#         if max_num % a == 0 and max_num % b == 0:
#             return max_num
#         max_num += 1
          
# print(LCM(a,b))


# def HCF(a,b):
#     small = min(a,b)
#     for i in range(small, 0, -1):
#         if a%i == 0 and b%i == 0:
#             return i
        
# print(HCF(12, 18))

# def LCM(a,b):
#     big = max(a,b)
#     while True:
#         if big%a == 0 and big%b == 0:
#             return big
#         big += 1
        
# print(LCM(12,18))



# prime Number question:

# def isPrime(n):

#     if n == 1:
#         return False
    
#     for i in range(2, n):
#         if n % i == 0:
#             return False
        
#     return True

# if __name__ == '__main__':
#     n = 4
#     print(True) if isPrime(n) else print(False)




# All divisors of a Number:

# approach 1

# n = 30

# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)

# # approach 2

# n = 30
# x = 1

# while x <= int(n**0.5):
#     if n % x == 0:
#         print(x)
#         if x != n/x:
#             print(n/x)
#     x += 1


def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    
    
def exactly3Divisors(n):
        count = 0
        for i in range(2, int(n**0.5)+1):
            if is_prime(i) and i*i <= n:
                count += 1
        return count

print(exactly3Divisors(6)) 
print(exactly3Divisors(9))  

