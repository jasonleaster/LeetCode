"""
Programmer  :   EOF
Date        :   2015.04.11
File        :   rti.py
E-mail      :   jasonleaster@gmail.com
"""

class Solution:
    # @return an integer
    def romanToInt(self, s):
        base = {"I":1,   "IV":4,   "V":5,   "IX":9 , \
                "X":10,  "XL":40,  "L":50,  "XC":90, \
                "C":100, "CD":400, "D":500, "CM":900,\
                "M":1000}

        ret_num = 0
        length = len(s)
        i      = 0
        while i < length :
            if s[i:i+2] in base:
                ret_num += base[s[ i:i+2] ]
                i += 2
            elif s[i] in base:
                ret_num += base[s[i]]
                i += 1

        return ret_num

#----------- just for testing -----------

s = Solution()
print s.romanToInt("MCXLXC")
