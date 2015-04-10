"""
Programmer  :   EOF
E-mail      :   jasonleaster@gmail.com
Date        :   2015.04.07
File        :   pp.py
"""

class Solution:
    def partition(self, s):

        length = len(s)
        middle = length/2
        if length != 1 :

            str_1 =  self.partition(s[0 : middle])

            if self.isPalindrome(str_1):
                print str_1, " ",

            str_2 =  self.partition(s[middle : length])
        
            if self.isPalindrome(str_2):
                print str_2,

            print 

            return str_1 + str_2
        else:
            return s

    def isPalindrome(self, x):
        string = str(x)
        length = len(string)
        for i in range(0, length):
            if string[i] != string[length - i - 1] :
                return False
        
        return True

#--------------- just for testing ---------
s = Solution()
s.partition("aab")
