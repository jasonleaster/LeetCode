class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        dic = {}

        while True:
            number = []
            while n != 0:
                number.append(n % 10)
                if number[-1] in dic:
                    return False
                else:
                    dic[number[-1]] = number[-1]
                n /= 10
                
            sumer = 0
            for i in number:
                sumer += i*i
                
            if sumer == 1:
                return True
            else:
                n = sumer

#-----------------------------------

s = Solution()
print s.isHappy(2)
print s.isHappy(7)
