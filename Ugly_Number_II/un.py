import sys
sys.path.append("../")
import crash_python

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1] * n
        x = k = 1
        i2 = i3 = i5 = 0
        v2 = 2
        v3 = 3
        v5 = 5
        while k != n:
            x = min(v2, v3, v5)
            ugly[k] = x
            if x == v2:
                i2 += 1
                v2 = ugly[i2] * 2
            if x == v3:
                i3 += 1
                v3 = ugly[i3] * 3
            if x == v5:
                i5 += 1
                v5 = ugly[i5] * 5
            k += 1
        return x
#-----------------------

s = Solution()
print s.nthUglyNumber(10)
