"""
Programmer : EOF
Date : 2015.03.31
File   :  reverse_interger.py
"""

class Solution:
    # @return an integer
    def reverse(self, x):
		buffer =[]
		
		INT_MAX = 0x7fffffff

		INT_MIN = (-INT_MAX - 1)
		
		if x > INT_MAX or x < INT_MIN :
		    return 0

		if x > 0 :
			tmp = x
			counter = 1
			while tmp > 0 :
				counter += 1
				buffer.append(tmp % 10);
				tmp /= 10

			tmp = 0
			for i in range(0, len(buffer)) :
				tmp *= 10
				tmp += buffer[i]

			if tmp > INT_MAX or tmp < INT_MIN :
				return 0
		    
			return tmp

		elif x < 0 :
			tmp = -x
			counter = 1
			while tmp > 0 :
				counter += 1
				buffer.append(tmp % 10);
				tmp /= 10

			tmp = 0
			for i in range(0, len(buffer)) :
				tmp *= 10
				tmp += buffer[i]

			if tmp > INT_MAX or tmp < INT_MIN :
				return 0
		        
			return -tmp

		else:
			return 0

#--------------------------just for testing ----------------------------

s = Solution()

print s.reverse(123)

