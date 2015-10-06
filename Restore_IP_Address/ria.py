import sys
sys.path.append("../")
import crash_python

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.dfs(s, 0, 0, "", result)
        return result
        
    def dfs(self, s, start, step, ip, result):

        end = len(s)
        if start == end and step == 4:
            result.append(ip[:-1]) #remove the last '.' from the last decimal
            return

        if (end - start) > (4 - step)*3  or (end - start) < (4-step):
            return
        
        num = 0
        for i in xrange(start, start+3):
            if i == end:
                break

            num = num * 10 + int(s[i])
            if num <= 255:
                ip += s[i]
                # Recursion
                self.dfs(s, i+1, step+1, ip+'.', result)
                
            if num == 0:
                break

# ------------------
number = "255011135"
s = Solution()
print s.restoreIpAddresses(number)
