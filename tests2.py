# class Solution:
#     def gameNum(self, inp):
#         n,p,m,d = map(int,inp.split())
#         return n <= p*(2**d)-m


# obj = Solution()
# print(obj.gameNum("1 2 3 4"))


n = 20
summ = 1000
amount_itog = summ * (n / 100)


amount_itog2 = summ * ((100 - n) / 100)
print(amount_itog)
print(amount_itog2)