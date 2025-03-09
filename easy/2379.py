class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        min_operations = blocks[:k].count('W')
        current_operations = min_operations

        for i in range(k, len(blocks)):
            if blocks[i - k] == 'W':
                current_operations -= 1
            if blocks[i] == 'W':
                current_operations += 1

            min_operations = min(min_operations, current_operations)

        return min_operations
obj = Solution()
print(obj.minimumRecolors("WBBWWBBWBW", 7))