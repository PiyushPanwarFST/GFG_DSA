class Solution:
    def avgMean(self, arr):
        sum = 0
        for i in arr:
            sum += i
        return sum // len(arr)
    
    def medain(self, arr):
        arr.sort()
        n = len(arr)
        if n % 2 == 0:
            return (arr[n // 2 - 1] + arr[n // 2]) / 2
        else:
            return arr[n // 2]
    
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 5]
    print(sol.avgMean(arr))  # Output: 3.0
    print(sol.medain(arr))   # Output: 3