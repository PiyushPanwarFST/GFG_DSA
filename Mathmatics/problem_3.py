class Solution:
    #You need to complete this function
    def factorial(self,N):
        fact = 1
        while N > 0:
            fact = fact*N
            N = N - 1
        return fact