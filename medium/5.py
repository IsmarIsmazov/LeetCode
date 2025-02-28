class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right] 
        
        res = ""
        for i in range(len(s)):
            odd_palindrome = expand_around_center(i, i)
            even_palindrome = expand_around_center(i, i + 1)

            if len(odd_palindrome) > len(res):
                res = odd_palindrome
            if len(even_palindrome) > len(res):
                res = even_palindrome
        
        return res
        
        # res = ""
        # for i in range(len(s)):
        #     left = i - 1
        #     right = i + 1
        #     while left >= 0 and right < len(s) and s[left] == s[right]:
        #         if (right - left + 1) > len(res):
        #             res = s[left:right + 1]
        #         left -= 1
        #         right += 1
        # return res

obj = Solution()
print(obj.longestPalindrome("babad"))