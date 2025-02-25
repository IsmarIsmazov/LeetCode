class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        odd_count = 0
        even_count = 1
        current_sum = 0
        total_odd_subarrays = 0

        for num in arr:
            current_sum += num

            if current_sum % 2 == 0:
                total_odd_subarrays += odd_count
                even_count += 1
            else: 
                total_odd_subarrays += even_count
                odd_count += 1

            total_odd_subarrays %= MOD

        return total_odd_subarrays