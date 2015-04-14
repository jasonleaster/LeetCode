"""
Programmer  :   EOF
Date        :   2015.04.11
File        :   3sum.py
E-mail      :   jasonleaster@gmail.com

Description :
    This is the first version which I used and try to solve
3Sum problem. It's work correctly but have a bad time complexity.

"""

class Solution:
    # @return a list of lists of length3, [[val1, val2, val3]]
    ret_list = []

    def threeSum(self, num):
        length = len(num)
        for i in range(0, length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if num[i] + num[j] + num[k] == 0:
                        
                        tmp = self.sequence(num[i], num[j], num[k])

                        if self.same_solution(tmp) is True:
                            continue
                        else:
                            self.ret_list += [tmp]

        return self.ret_list

    # make sure that in @self.ret_list e1 < e2 < e3
    def sequence(self, a, b, c):
        ret = []
        if a < b:
            if a < c:
                ret += [a]
                if b < c:
                    ret += [b, c]
                else:
                    ret += [c, b]
            else:
                ret += [c, a, b]
        else: # a > b in this situation
            if b < c:
                ret += [b]
                if a < c:
                    ret += [a, c]
                else:
                    ret += [c, a]
            else:
                ret += [c, b, a]

        return ret

    def same_solution(self, sv):

        if len(self.ret_list) != 0 :
            row = len(self.ret_list)
            col = len(self.ret_list[0])

            for i in range(0, row):
                for j in range(0, col):
                    if self.ret_list[i][j] != sv[j]:
                        break;

                if j == col-1:
                    return True

        return False


#------------- just for testing ----------

s = Solution()
Date = [-1, 0, 1, 2, -1, -4]
print s.threeSum(Date)
