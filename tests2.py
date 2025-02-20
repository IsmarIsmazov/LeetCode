class Solution:
    def gameNum(self, inp):
        n,p,m,d = map(int,inp.split())
        return n <= p*(2**d)-m


obj = Solution()
print(obj.gameNum("1 2 3 4"))

