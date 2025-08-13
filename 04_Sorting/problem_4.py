class Solution:
    def countOnes(self, arr):
        n = len(arr)
        low, high = 0, n-1
        
        while low<=high:
            mid = (low + high)//2
            
            if arr[mid] == 0:
                high = mid - 1
            
            elif mid == n-1 or arr[mid + 1] != 1:
                return mid + 1
            
            else:
                low = mid + 1
        return 0
                
            
if __name__ == "__main__":
    sol = Solution()
    arr = [0, 0, 1, 1, 1, 1]
    print(sol.countOnes(arr))  # Output: 4
    arr = [0, 0, 0, 0]
    print(sol.countOnes(arr))  # Output: 0
    arr = [1, 1, 1, 1]
    print(sol.countOnes(arr))  # Output: 4
    arr = [0, 1, 1, 1, 1]
    print(sol.countOnes(arr))  # Output: 4