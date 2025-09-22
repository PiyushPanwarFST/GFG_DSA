class Solution:
    def SelectionSort(self,arr):
        n = len(arr)
        for i in range(n-1):
            min_ind = i
            for j in range(i+1, n):
                if arr[j] < arr[min_ind]:
                    min_ind = j
            arr[min_ind], arr[i] = arr[i], arr[min_ind]
        print(arr)

if __name__ == "__main__":
    sol = Solution()
    # print(sol.arr)
    sol.SelectionSort([64, 34, 25, 12, 22, 11, 90])