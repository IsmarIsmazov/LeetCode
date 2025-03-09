class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def sieve(n):
            is_prime = [True] * (n + 1)
            is_prime[0] = is_prime[1] = False
            for i in range(2, int(n ** 0.5) + 1):
                if is_prime[i]:
                    for j in range(i * i, n + 1, i):
                        is_prime[j] = False
            return [x for x in range(n + 1) if is_prime[x]]

        primes = sieve(right) 
        primes = [p for p in primes if p >= left]  

        if len(primes) < 2:
            return [-1, -1]

        min_diff = float('inf')
        ans = [-1, -1]
        for i in range(len(primes) - 1):
            if primes[i + 1] - primes[i] < min_diff:
                min_diff = primes[i + 1] - primes[i]
                ans = [primes[i], primes[i + 1]]

        return ans

obj = Solution()
print(obj.closestPrimes(10, 19))