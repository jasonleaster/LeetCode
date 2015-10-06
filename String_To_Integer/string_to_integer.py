"""
Programmer  :   EOF
Date        :   2015.04.01
File        :   string_to_integer.py

"""

class Solution():

    def is_digital(self, c) :
        if len(c) == 0 :
            return False

        if '9' >= c and c >= '0':
            return True

        return False
            
    def atoi(self, string) :

        INT_MAX = 2147483647
        INT_MIN = -INT_MAX - 1
        
        length = len(string)

        if length == 0 :
            return 0

        num = 0
        found_tag = False
        positive = True
        blank_cleared = False

        for i in range(0, len(string)):

            if blank_cleared is False  and string[i] == ' ':
                "Do nothing"
                
            elif blank_cleared is True and string[i] == ' ':
                break

            elif string[i] == '+' or string[i] == '-':
                blank_cleared = True
                if found_tag is False :
                    found_tag = True

                    if string[i] == '-' :
                        positive = False
                else:
                    return 0

            elif self.is_digital(string[i]) is True:
                blank_cleared = True
                num *= 10
                num += int(string[i]) - int('0')
            else:
                break

        if positive is False :
            num *= -1

        if num > INT_MAX :
            return INT_MAX
        elif num < INT_MIN :
            return INT_MIN
        else :
            return num


s = Solution()

print s.atoi("+   123hello45")
print s.atoi("-12345")
print s.atoi("12345")
print s.atoi("    +004500")
print s.atoi("    +0 04500")
