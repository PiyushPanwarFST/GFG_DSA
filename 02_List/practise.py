class Solution:
    def moreFrequent(self, arr, x, y):
            count_x = arr.count(x)
            count_y = arr.count(y)
            print(f"Count of {x}: {count_x}, Count of {y}: {count_y}")
            if count_x == count_y:
                return  min(x, y)
            else:
                if count_x > count_y:
                    return x
                else:
                    return y
        
if __name__ == "__main__":
    sol = Solution()
    arr = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5]
    x = 4
    y = 5
    print(sol.moreFrequent(arr, x, y))  # Output: 1