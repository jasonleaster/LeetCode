__author__ = 'jasonleaster'

class Stack() :
      S = []
      def __init__(self, arg = []):
          self.S = [len(arg)] + arg

      def stack_empty(self) :
          if self.S[0] == 0 :
             return True
          else :
             return False

      def push(self,x) :

          self.S[0] += 1

          if len(self.S) > self.S[0] :
             self.S[self.S[0]] = x
          else :
                self.S = self.S + [x]

          return self.S

      def pop(self) :
          if self.stack_empty() == True :
             print "underflow"
          else :
                temp = self.S[0]
                self.S[0] -= 1
                return self.S[temp]

      def show_stack(self) :
          print "stack status:",self.S[1 : self.S[0] + 1]



class Solution:
    Parenthese = {"(":")", "[":"]", "{":"}"}
    def isValid(self, s):
        stack = Stack()
        for i in range(0, len(s)):
            if stack.stack_empty() is True:
                stack.push(s[i])
            else:
                val = stack.pop()
                if val in self.Parenthese:
                    if self.Parenthese[val] != s[i]:
                        stack.push(val)
                        stack.push(s[i])

        if stack.stack_empty() is True:
            return True
        else:
            return False


# ----------- test -------------

s = Solution()
print s.isValid("(([]))")
print s.isValid("([)]")