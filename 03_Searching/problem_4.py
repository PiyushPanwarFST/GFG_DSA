class Solution:
    def countOnes(self, arr):
        n = len(arr)
        low, high = 0, n-1
        answer = -1
        
        while low<=high:
            mid = (low + high)//2
            
            if arr[mid] == 1:
                answer = mid
                low = mid + 1
            
            else:
                high = mid - 1
        
        return answer + 1
                
if __name__ == "__main__":
    sol = Solution()
    arr =  [1, 1, 1, 1, 0, 0]
    print(sol.countOnes(arr))  # Output: 4
