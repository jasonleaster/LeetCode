"""
Programmer  :   EOF
Code date   :   2015.03.02
file        :   sn3.py
e-mail      :   jasonleaster@gmail.com

Code description :
    Given an array of integers, every element appears 
twice except for one. Find that single one.

Note:
	Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

In this solution, I used a XOR operand to solve this problem.

"""
class Solution():

    def singleNumber(self, A) :
        
        result = 0
        for i in range(0, len(A)) :
            result ^= A[i]

        return result


#----------for testing ----------------

array = [1,2,3,4,5,4,3,2,1]

s = Solution()
print s.singleNumber(array)
