import sys
sys.path.append("../")
import crash_python

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = [0]
        for i in xrange(n):
            for j in xrange(len(ans)-1, -1, -1):
                ans.append(1 << i | ans[j])

        return ans

# ----- test ------
s = Solution()
print s.grayCode(3)
