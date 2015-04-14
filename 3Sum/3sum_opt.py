"""
Programmer  :   EOF
Date        :   2015.04.11
File        :   3sum_opt.py
E-mail      :   jasonleaster@gmail.com

Description :
    This is the second version which I used and try to solve
3Sum problem. I used dictionary and try to improve the performance.
It's work correctly but also have a bad time complexity.

"""

"""
Varible Description :

    @ret_list   :   We store the answer which the problem asked for into this varible
    @dic        :   This is a dictionary. I use this to store the inputed numbers.
    @time       :   This is also a dictionary which store the times that the number
                    appear in the inputed data.


"""

class Solution:
    # @return a list of lists of length3, [[val1, val2, val3]]
    ret_list = []
    dic  = {}
    time = {}

    def threeSum(self, num):
        length = len(num)

        #   Initialize the @dic and @time
        for i in range(0, length):
            if num[i] not in self.dic:
                self.dic[num[i]]  = num[i]
                self.time[num[i]] = 1
            else:
                self.time[num[i]] += 1

        # Kernel part of this algorithm
        for i in range(0, length):
            for j in range(i + 1, length):
                
                #It's a old trick to use the inverse number as the index
                if -(num[i] + num[j]) in self.dic:
                    
                    tmp = self.sequence(num[i], num[j], -(num[i] + num[j]))

                    if self.same_solution(tmp) is True:
                        continue
                    elif self.illegal_solution(tmp) is True:
                        continue
                    else:
                        """
                            If we get there, we get a legally solution and store it into @ret_list
                        """
                        self.ret_list += [tmp]

        return self.ret_list

    # make sure that data in @self.ret_list e1 < e2 < e3
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

    def illegal_solution(self, sv):
        k = len(sv)
        cp_time = self.time.copy()
        while k > 0:
            if cp_time[ sv[k-1] ] != 0:
                cp_time[ sv[k-1] ] -= 1
            else:
                return True
            k -= 1

        return False



#------------- just for testing ----------

s = Solution()
Date = [-1, 0, 1, 2, -1, -4]
print s.threeSum(Date)
