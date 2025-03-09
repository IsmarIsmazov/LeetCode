class Solution:
    def KandN(self, num, k):
        for i in range(int(k)):
            num = num - k
            k -= 1
            if num <= 0:
                break
        if num <= 0:
            return "YES"
        else:
            return "NO"

obj = Solution()

print(obj.KandN(56000000000000, 100000000))


# x: int = "asds"
# print(x)