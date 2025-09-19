# peak element with linear search

class Solution:
    def peakElement(self, arr):
        n = len(arr)

        for i in range(0, n):
            if n==1:
                return 0
            if i == 0 and arr[i] > arr[i+1]:
                return i
            elif i == n-1 and arr[i] > arr[i-1]:
                return i
            elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                return i
        return -1
    
if __name__ == "__main__":
    sol = Solution()
    # Test cases wihout peak elements (False cases)
    print("\nTest cases without peak elements:")
    print(sol.peakElement([1, 2, 4, 5, 7, 8, 3]))  

