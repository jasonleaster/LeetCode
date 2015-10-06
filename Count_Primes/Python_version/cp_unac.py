"""
Programmer  :   EOF
Date        :   2015.04.28
File        :   cp_unac.py
E-mail      :   jasonleaster@gmail.com

"""
import math

class Solution:
    def countPrimes(self, n):
        if n <= 2:
            return 0
        elif n == 3:
            return 1

        primes = [0 for i in range(0, n)]
 
        primes[0] = 2
        primes[1] = 2
        primes[2] = 3

        for i in range(4, n):
            for j in range(1, primes[0]+1):
                if i % primes[j] == 0:
                    break
            if j == primes[0]:
                primes[j + 1] = i
                primes[0] += 1

        return primes[0] 

#--------------just for testing ------------

s = Solution()
print s.countPrimes(100)
print s.countPrimes(5)
print s.countPrimes(0)
print s.countPrimes(2)
print s.countPrimes(3)
