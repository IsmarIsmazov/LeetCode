class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        xmap = {
            "(": ")",
            "[": "]",
            "{": "}",

        }


        stack = []

        for char in s:
            if char in xmap:
                stack.append(char)
            else:
                if not stack or xmap[stack.pop()] != char:
                    return False

        return not stack
        # result = ""
        # if len(s) > 1:
        #     for i in s:
        #         indexs = s.index(i)
        #         if i in xmap and s[indexs+1] == xmap.get(i):
        #             result += i + xmap[i]

        # if result != "":
        #     return True
        # else:
        #     return False




obj = Solution()
print(obj.isValid("){"))