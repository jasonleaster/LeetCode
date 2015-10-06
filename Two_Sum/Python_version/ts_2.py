"""
    Code writer : EOF
    Code file   : ts_2.py
    Code date   : 2015.02.15

    Code description :
        This is a solution for Leetcode problem-1 @Two Sum

"""
class Solution() :

    def twoSum(self, num, target):
        if num is None or target is None:
            return

        dic = {}
        for i in range(0, len(num)) :
            dic[num[i]] = i

        for i in range(0, len(num)) :
            if target - num[i] in dic and\
                i is not dic[target- num[i]]:

                return (i + 1, dic[target- num[i]] + 1)

                




#------testing-------

#numbers = [2,7,11,15]
numbers = [3, 2, 4]
#numbers = [-1, -2, -3, -4, -5]
target  = 6
print "Input :"
print "numbers= ", numbers, "target = ", target
s = Solution()
print "Output", s.twoSum(numbers, target)




