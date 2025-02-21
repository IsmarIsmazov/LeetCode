class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        list_num = []
        for i in digits:
            list_num.append(str(i))
        num = int("".join(list_num)) + 1
        return [int(i) for i in str(num)]

obj = Solution()
print(obj.plusOne([9]))