class Solution:
    def smallestNumber(self, pattern: str):
        self.result = []

        self.build_sequence(0, 0, pattern)
        return "".join(self.result[::-1])

    def build_sequence(
        self, current_index: int, current_count: int, pattern: str
    ) -> int:
        if current_index != len(pattern):
            if pattern[current_index] == "I":
                self.build_sequence(
                    current_index + 1, current_index + 1, pattern
                )
            else:
                current_count = self.build_sequence(
                    current_index + 1, current_count, pattern
                )

        self.result.append(str(current_count + 1))
        return current_count + 1


    
        # nums = []
        # patterns_lenght = len(pattern)
        # current_index = 0
        # current_count = 0
        # for i in pattern:
        #     if current_index != patterns_lenght:
        #         if pattern[current_index] == 'I':
        #             current_count += 1
        #         else:
        #             current_count -= 1
        #         current_index += 1

        #     nums.append(str(current_count + 1))

        # number = 1
        # for i in pattern:
        #     if i == 'I':
        #         if number not in nums:
        #             nums.append(number)
        #             number += 1
        #     elif i == 'D':
        #         if number not in nums:
        #             nums.append(number)
        #             number -= 1
        #         else:
        #             number
        return nums

obj = Solution()
print(obj.smallestNumber("IID"))