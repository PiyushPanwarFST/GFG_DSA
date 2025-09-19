# Given a sorted array of integers of size N and a number X. Find the leftmost index of X in the array arr[].

# Input:
# N = 10
# arr[] = {1, 1, 2, 2, 3, 4, 5, 5, 6, 7}
# X = 1
# Output: 0 
# Explanation: Because the element 1 appears twice and its left most occurrence is at index 0.

class Solution:
    def leftIndex (self, N, arr, X):
        start = 0
        end = N - 1
        
        while start <= end:
            mid = (start + end) // 2
            
            if arr[mid] > X:
                end = mid - 1
            
            elif arr[mid] < X:
                start = mid + 1
            
            else:
                if arr[mid] != arr[mid - 1] or mid == 0:
                    return mid
                else:
                    end = mid - 1
        return -1
    
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 1, 2, 2, 3, 4, 5, 5, 6, 7]
    N = 10
    X = 1
    print(sol.leftIndex(N, arr, X))  # Output: 0

                
                    
                
        
        