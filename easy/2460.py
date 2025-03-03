class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1] and nums[i] != 0:
                nums[i] *= 2
                nums[i+1] = 0
        
        result = [num for num in nums if num != 0] 
        result.extend([0] * (len(nums) - len(result)))  
        
        return result
        # for i in range(len(nums)-1):
        #     if nums[i] == nums[i+1]:
        #         nums[i] *= 2
        #         nums[i+1] = 0
        # return [i for i in nums if i != 0]
    
obj = Solution()
print(obj.applyOperations([1,2,2,1,1,0]))