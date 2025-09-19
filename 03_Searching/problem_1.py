# Given an array, arr[] sorted in ascending order and an integer k. Return true if k is present in the array, otherwise, false.

# Examples:

# Input: arr[] = [1, 2, 3, 4, 6], k = 6
# Output: true

# Exlpanation: Since, 6 is present in the array at index 4 (0-based indexing), output is true.
# Input: arr[] = [1, 2, 4, 5, 6], k = 3
# Output: false

# Exlpanation: Since, 3 is not present in the array, output is false.
# Input: arr[] = [2, 3, 5, 6], k = 1
# Output: false

# Solution:

#User function Template for python3

class Solution:
    ##Complete this function
    def searchInSorted(self,arr, k):
        start = 0
        end = len(arr) - 1
        
        while start <= end:
            
            mid = (start + end) // 2
            
            if arr[mid] == k:
                return True
                
            elif arr[mid] > k:
                end = mid - 1
            
            elif arr[mid] < k:
                start = mid + 1
                
            else:
                return False

if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3, 4, 6]
    k = 6
    print(sol.searchInSorted(arr, k))  # Output: True