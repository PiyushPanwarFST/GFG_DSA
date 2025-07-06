import math

class Solution:
    def digitsInFactorial(self,num):
        if num == 0 or num == 1:
            return 1
        
        count = 0
        for i in range(2, num+1):
            count += math.log10(i)
        
        return math.floor(count) + 1