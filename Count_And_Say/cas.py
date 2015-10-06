class Solution:

    def next_sequence(self, n):
        string = "1"
        while n != 0:
            string = string[::-1]
            integer = int(string)
            string = ""
            while integer != 0:
                counter = 0
                while (integer % 10) == ((integer / 10) % 10):
                    counter += 1
                    integer /= 10
                counter += 1
                string += str(counter) + str(integer % 10)
                integer /= 10
            n -= 1
        return string

    def countAndSay(self, n):
        return self.next_sequence(n-1)

# ------------------------------ Code for test -------------------------------
s = Solution()
print s.countAndSay(4)
