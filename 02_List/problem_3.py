#User function Template for python3

class Solution:
    def immediateSmaller(self,arr,n,x):
        arr.sort(reverse=True)
        for i in arr:
            if i < x:
                return i
            
        return -1
    
if __name__ == "__main__":
    sol = Solution()
    arr = [8, 100, 20, 40, 3, 7]
    x = 10
    print(sol.immediateSmaller(arr, len(arr), x))  # Output: 8