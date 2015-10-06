"""
Programmer  :   EOF
Date        :   2015.04.15
File        :   lcp.py
E-mail      :   jasonleaster@gmail.com
"""

"""
Varible Description:
    @ret_string :   We store the string to be returned into this varible
    @length     :   Find the min length of the inputed string in the list

"""

class Solution:
    def longestCommonPrefix(self, strs):
        ret_string = ""

        if len(strs) == 0:
            return ret_string
        else:
            length = len(strs[0])

        for i in range(0, len(strs)):
            if length > len(strs[i]):
                length = len(strs[i])

        if len(strs) != 1:
            for j in range(0, length):
                """
                    We check the element from back to front.
                    If we can't get the first string in the 
                    inputed list of string, we can tell that 
                    we the comman prefix break there.
                """
                i = len(strs) - 1
                while i >= 1:
                    if strs[i][j] != strs[i-1][j] :
                        break
                    i -= 1

                if i == 0:
                    ret_string += strs[i][j]
                else:
                    break

        return ret_string

#-------- just for testing ----------

s = Solution()
strings = ["acb", "bca"]
print s.longestCommonPrefix(strings)

strings = ["a", "b"]
print s.longestCommonPrefix(strings)

strings = ["a"]
print s.longestCommonPrefix(strings)

strings = ["abcd", "ab", "abc"]
print s.longestCommonPrefix(strings)
