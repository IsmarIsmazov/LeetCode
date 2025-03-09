class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        ind = 1
        plus = 0
        for i in range(n):
            ind += plus
            plus +=4
        return ind

        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 5

        # for i in range(3, n + 1):
        #     n = (n * 2) - 2

        # return n
    
obj = Solution()
print(obj.coloredCells(3))