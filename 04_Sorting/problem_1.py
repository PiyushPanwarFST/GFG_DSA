class Solution:
    def bubbleSort(self,arr):
        n = len(arr)
        for i in range(n-1):
            for j in range(n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.bubbleSort([64, 34, 25, 12, 22, 11, 90]))