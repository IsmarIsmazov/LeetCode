class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        summa = int(a, 2) + int(b, 2)

        binary_sum = bin(summa)[2:]
        return binary_sum
