class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        last_pos = [-1] * 3
        total = 0

        for pos in range(len(s)):
            last_pos[ord(s[pos]) - ord("a")] = pos


            total += 1 + min(last_pos)

        return total