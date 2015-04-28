import math

class Solution:
    def countPrimes(self, n):
        if n < 2:
            return 0

        primes = [True for i in range(0, n)]
        
        sqt_n = int(math.sqrt(n))
        for i in range(2, sqt_n + 1):
            if primes[i] is True:
                for j in range(i * i, n, i):
                    primes[j] = False

        sum_value = 0
        for i in range(2, n):
            if primes[i] is True:
                sum_value += 1

        return sum_value

#--------------just for testing ------------

s = Solution()
print s.countPrimes(5)
print s.countPrimes(0)
print s.countPrimes(2)
print s.countPrimes(3)
print s.countPrimes(100)
