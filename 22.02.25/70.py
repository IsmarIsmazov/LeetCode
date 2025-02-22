class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
        a, b = 1, 2
        for _ in range(3, n + 1):
            a, b = b, a + b 
        return b
        # ins = 0
        # while ins <= n:
        #     if n < 0:
        #         return 0
        #     if n == 1:
        #         return 1
        #     if n == 2:
        #         return 2
        #     else:
        #         n = n - 1 + n - 2
        #     ins += 1
