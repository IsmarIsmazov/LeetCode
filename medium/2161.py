class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        less, equal, greater = [], [], []
        
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                greater.append(num)
        
        return less + equal + greater


obj = Solution()
print(obj.pivotArray([9,12,5,10,14,3,10], 10))
