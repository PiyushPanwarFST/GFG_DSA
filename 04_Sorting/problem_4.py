class Solution:
    
    def inversionCount(self, arr):
        n = len(arr)
        low = 0
        high = n - 1
        
        return self.sortSubarray(arr, low, high)
        
    def sortSubarray(self, arr, low, high):
        res = 0
        
        if low < high:
            mid = (low + high) // 2
            
            res += self.sortSubarray(arr, low, mid)
            res += self.sortSubarray(arr, mid+1, high)
            res += self.mergeSubarray(arr, low, mid, high)
            
        return res
        
    def mergeSubarray(self, arr, low, mid, high):
        
        res = 0
        left = arr[low: mid+1]
        right = arr[mid+1: high+1]
        
        i = 0
        j = 0
        k = low
        
        while i < len(left) and j < len(right):
            
            if left[i] <= right[j]:
                arr[k] = left[i]
                k += 1
                i += 1
                
            else:
                arr[k] = right[j]
                k += 1
                j += 1
                
                res += len(left) - i
        
        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1
            
        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1
            
        return res
            
if __name__ == "__main__":
    arr = [2,5,8,11,3,6,9,13]
    obj = Solution()
    print("Number of inversions:", obj.inversionCount(arr))