class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_word = s.split()
        last_word = list_word[-1]
        length = len(last_word)
        return length