"""
Programmer  :   EOF
Date        :   2015.04.14
File        :   zigzag.py
E-mail      :   jasonleaster@gmail.com

"""

class Solution:
    def convert(self, s, nRows):
        length = len(s)
        ret_string = ""
        i   = 0
        row = 0 
        counter = 0
        if nRows != 1:
            while row < nRows:
                i = row
                col = 0
                while i < length and counter < length:
                    ret_string += s[i]

                    if row == 0 or row == nRows -1:
                        i += (nRows - 1)*2
                    elif col % 2 == 0:
                        i += (nRows - row -1)*2
                    else:
                        i += row*2
                    col     += 1
                    counter += 1
                row += 1
        else:
            return s

        return ret_string
#----------- just for testing ----------

s = Solution()
print s.convert("AB", 2)
print s.convert("PAYPALISHIRING", 3)
print s.convert("PAYPALISHIRING", 4)
