"""
    Code writer : EOF
    Code file   : ts.py
    Code date   : 2015.02.15

    Code description :
        This is a solution for Leetcode problem-1 @Two Sum

"""
class Solution() :

    def twoSum(self, num, target):
        if num is None or target is None:
            return

        for i in range(0, len(num)) :
            for j in range(i + 1, len(num)) :
                if num[i] + num[j] == target :
                    return (i+1, j+1)

#------testing-------

#numbers = [2,7,11,15]
numbers = [-1, -2, -3, -4, -5]
target  = -8
print "Input :"
print "numbers= ", numbers, "target = ", target
s = Solution()
print "Output", s.twoSum(numbers, target)




