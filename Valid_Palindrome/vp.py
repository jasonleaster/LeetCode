"""
Programmer  :   EOF
e-mail      :   jasonleaster@gmail.com
Date        :   2015.04.07
File        :   vp.py
"""

import string

class Solution:

    def isPalindrome(self, s):
        length = len(s)
        left    = 0
        right   = length - 1
        while left < right:

            if self.isCharacter(s[left]) is False:
                left += 1
                continue

            if self.isCharacter(s[right]) is False:
                right -= 1
                continue

            if string.lower(s[left]) != string.lower(s[right]):
                return False

            left  +=  1
            right -=  1

        return True

    def isCharacter(self, c):
        if c is None:
            return False

        if (c <= 'z' and c >= 'a') or \
           (c <= 'Z' and c >= 'A') or \
           (c <= '9' and c >= '0'):
            return True

        return False

#---------------- just for testing --------------

s = Solution()
string_1 = "abcba"
print string_1
if s.isPalindrome(string_1) :
    print "is Palindrome"

string_1 = "ab"
print string_1
if s.isPalindrome(string_1) :
    print "is Palindrome"

string_1 = "1a2"
print string_1
if s.isPalindrome(string_1) :
    print "is Palindrome"
