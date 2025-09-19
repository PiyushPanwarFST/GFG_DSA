class Solution:
    def findFloor(self, arr, x):
        n = len(arr)
        low = 0
        high = n - 1
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] <= x:
                ans = mid
                low = mid + 1
            elif arr[mid] > x:
                high = mid - 1
            else:
                return -1
        return ans


if __name__ == "__main__":
    sol = Solution()
    arr = [1, 2, 8, 10, 10, 12, 19]
    x = 5
    print(sol.findFloor(arr, x))  # Output: 1
    x = 20
    print(sol.findFloor(arr, x))  # Output: 6
    arr = [1, 2, 8, 10, 10, 12, 19]
    x = 0
    print(sol.findFloor(arr, x))  # Output: -1