class Solution:
    # inf has been imported in driver code
    def immediateGreater(self,arr,n,x):
        arr.sort()
            
        for i in arr:
            if i > x:
                return  i
            
        return -1

if __name__ == "__main__":
    sol = Solution()
    arr = [8, 100, 20, 40, 3, 7]
    x = 10
    print(sol.immediateGreater(arr, len(arr), x))  # Output: 20
