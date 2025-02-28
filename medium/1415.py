class Solution(object):
    def getHappyString(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.happy = []
        self.generate(n, "")
        self.happy.sort()
        print(self.happy)
        return self.happy[k - 1] if k <= len(self.happy) else ""


    def generate(self, n, current):
        if len(current) == n:
            self.happy.append(current)
            return

        for char in "abc":
            if not current or current[-1] != char:
                self.generate(n, current + char)

obj = Solution()
print(obj.getHappyString(3, 9))