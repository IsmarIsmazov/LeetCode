class Solution(object):
    def countOfSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        map_word = {
            "a": 0,
            "e": 0,
            "i": 0,
            "o": 0,
            "u": 0
        }
        j = 0 
        for wor in word:
            if wor in map_word:
                map_word[wor] += 1
            else: 
                j += 1

        if j < k:
            return 0
        print(map_word)
        if len(set(map_word.values())) == 1 and j in set(map_word.values()) if j > 0 else True:
            return next(iter(map_word.values()))
        else:
            return 0
    
obj = Solution()
print(obj.countOfSubstrings("ieaouqqieaouqq", 1))

