class Solution:   
    def peakElement(self, arr):
        n = len(arr)
        low = 0
        high = n - 1

        while low < high:
            mid = (low + high) // 2

            if arr[mid] < arr[mid+1]:
                low = mid + 1
            
            else:
                high = mid

        return low
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.peakElement([1, 2, 4, 5, 7, 8, 9]))  # Output: True (since there is a peak element)
    print(sol.peakElement([1, 2, 3]))        # Output: False (no peak element)