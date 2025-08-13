class Solution:   
    def peakElement(self, arr):
        n = len(arr)
        # edges as potential peaks
        if arr[0] > arr[1]:
            return 0
        if arr[n-1] > arr[n-2]:
            return n - 1
        for i in range(1, len(arr)-1):
            if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
                return i
        return 0
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.peakElement([1, 2, 4, 5, 7, 8, 9]))  # Output: True (since there is a peak element)
    print(sol.peakElement([1, 2, 3]))        # Output: False (no peak element)