

class Solution:
    def insertAtEnd(self, arr, val):
       return arr.insert(len(arr), val)
    
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 3]
    val = 4
    sol.insertAtEnd(arr, val)
    print(arr)  # Output: [1, 2, 3, 4]