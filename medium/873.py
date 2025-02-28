class Solution(object):
    def lenLongestFibSubseq(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        index = {x: i for i, x in enumerate(arr)}
        n = len(arr)
        dp = {}
        max_len = 0

        for k in range(n):
            for j in range(k):
                x = arr[k] - arr[j]
                if x < arr[j] and x in index:  
                    i = index[x]
                    dp[j, k] = dp.get((i, j), 2) + 1
                    max_len = max(max_len, dp[j, k])

        return max_len if max_len >= 3 else 0
        

        # ind = 0
        # list_arr = []
        
        # arr.reverse()

        # while arr:
        #     print(arr)
        #     arr.pop()
        #     ...


        # list_arr = []
        # ind = -1
        # print(arr)
        # for i in arr:
        #     if ind < 0:
        #         list_arr.append(i)
        #     else:
        #         list_arr.append(i+arr[ind])
        #     ind += 1
        #     print(ind)
        # #     print(ind)

        # # print(list_arr)
        # return len(list_arr)\
        
obj = Solution()
print(obj.lenLongestFibSubseq([1,2,3,4,5,6,7,8]))