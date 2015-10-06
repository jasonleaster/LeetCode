class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x = [int(a[i]) for i in xrange(len(a))]
        y = [int(b[i]) for i in xrange(len(b))]
        
        x = x[::-1]
        y = y[::-1]

        if len(x) > len(y):
            while len(x) > len(y):
                y.append(0)
        else:
            while len(x) < len(y):
                x.append(0)

        x.append(0)
        y.append(0)

        for i in xrange(len(x)):
            x[i] += y[i]

        for i in xrange(len(x)):
            if x[i] >= 2:
                tmp = x[i]
                x[i] = tmp % 2
                x[i + 1] += tmp / 2

        string = ""
        find = False
        for i in range(len(x)-1, -1, -1):
            if find == False:
                if x[i] != 0:
                    find = True        
                    string += str(x[i])
            else:
                string += str(x[i])

        if len(string) == 0:
            return "0"
        else:
            return string

 
# ------- test ---------
s = Solution()
print s.addBinary("0", "0")
print s.addBinary("11", "1111")
print s.addBinary("11", "11")
