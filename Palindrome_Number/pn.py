"""
Programmer  :   EOF
E-mail      :   jasonleaster@gmail.com
Date        :   2015.04.06
File        :   pn.py
"""

class Solution:
    def isPalindrome(self, x):
        string = str(x)
        length = len(string)
        for i in range(0, length):
            if string[i] != string[length - i - 1] :
                return False
        
        return True

#----------- just for testing ----------


s = Solution()
if s.isPalindrome(123321) :
    print "is palindrome"

