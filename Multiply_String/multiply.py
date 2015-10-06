class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        product = [0 for i in xrange(len(num1) + len(num2) + 1)]

        num1 = num1[::-1]
        num2 = num2[::-1]

        for i in xrange(len(num1)):
            for j in xrange(len(num2)):
                ans = int(num1[i]) * int(num2[j]) + product[i + j]
                product[i + j] = ans % 10
                product[i + j + 1] += ans /10
        
        string = ""
        find = False
        for i in range(len(product)-1, -1, -1):
            if find == False:
                if product[i] != 0:
                    find = True
                    string += str(product[i])
            else:
                string += str(product[i])
        
        if len(string) == 0:
            return "0"
        else:
            return string

#--------------test ----------------
s = Solution()
print s.multiply("100","450")
print s.multiply("0","0")
print s.multiply("1","1")
print s.multiply("123","456")
