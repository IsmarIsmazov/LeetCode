class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        I=1
        V=5
        X=10
        L=50
        C=100
        D=500
        M=1000

        res = ""
        while num > 0:
            if num >= M:
                res += "M" * (num // M)
                num -= M * (num // M)
            if num >= D:
                res += "D" * (num // D)
                num -= D * (num // D)
            if num >= C:
                res += "C" * (num // C)
                num -= C * (num // C)
            if num >= L:
                res += "L" * (num // L)
                num -= L * (num // L)
            if num >= X:
                res += "X" * (num // X)
                num -= X * (num // X)
            if num >= V:
                res += "V" * (num // V)
                num -= V * (num // V)
            if num >= I:
                res += "I" * (num // I)
                num -= I * (num // I)
        return res


obj = Solution()

print(obj.intToRoman(3749))