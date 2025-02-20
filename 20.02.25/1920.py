class Solution(object):
    def findDifferentBinaryString(self, nums):
        """
        :type nums: List[str]
        :rtype: str
        """
        result = ""
        for i in range(len(nums)):
            result += "0" if nums[i][i] == "1" else "1"
        return result



obj = Solution()
print(obj.findDifferentBinaryString(["01", "10"]))