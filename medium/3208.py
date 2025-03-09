class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        n = len(colors)
        if k > n:
            return 0  

        extended_colors = colors + colors[:k - 1]
        count = 0
        valid_count = 0  

        for i in range(1, k):
            if extended_colors[i] != extended_colors[i - 1]:
                valid_count += 1
        
        if valid_count == k - 1:
            count += 1

        for i in range(1, n):
            if extended_colors[i] != extended_colors[i - 1]:
                valid_count -= 1
            if extended_colors[i + k - 1] != extended_colors[i + k - 2]:
                valid_count += 1
            
            if valid_count == k - 1:
                count += 1

        return count


        # n = len(colors)
        # if k > n:
        #     return 0  

        # extended_colors = colors + colors[:k - 1]
        # count = 0
        # valid = True

        # for i in range(1, k):
        #     if extended_colors[i] == extended_colors[i - 1]:
        #         valid = False
        #         break

        # if valid:
        #     count += 1

        # for i in range(1, n):
        #     if extended_colors[i + k - 2] == extended_colors[i + k - 1]:  
        #         valid = False
        #     if extended_colors[i - 1] == extended_colors[i]:  
        #         valid = True  

        #     if valid:
        #         count += 1

        # return count




        # n = len(colors)
        # if k > n:
        #     return 0  

        
        # extended_colors = colors + colors[:k - 1]
        # count = 0

        
        # def is_alternating(subarray):
        #     for i in range(1, len(subarray)):
        #         if subarray[i] == subarray[i - 1]: 
        #             return False
        #     return True

        # for i in range(n):
        #     if is_alternating(extended_colors[i:i + k]):
        #         count += 1

        # return count

obj = Solution()
print(obj.numberOfAlternatingGroups([1,1,0,1], 4))