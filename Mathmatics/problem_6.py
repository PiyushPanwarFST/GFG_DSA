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