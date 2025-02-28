class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target in nums:
            indexs = nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            indexs = nums.index(target)
        return indexs


obj = Solution()
print(obj.searchInsert([1, 3, 5, 6], 2))