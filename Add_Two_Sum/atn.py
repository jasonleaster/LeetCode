"""
Programmer  :   EOF
Date        :   2015.04.14
File        :   atn.py
E-mail      :   jasonleaster@gmail.com

"""
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        
        ret_list  = ListNode(0)
        iter_list = ret_list
        
        remainder = 0
        quotient  = 0
        
        while l1 != None and l2 != None:
            remainder = (l1.val + l2.val + iter_list.val) % 10
            quotient  = (l1.val + l2.val + iter_list.val) / 10
            
            iter_list.val  = remainder
            iter_list.next = ListNode(quotient)
            last_prev = iter_list

            iter_list = iter_list.next
        
            l1 = l1.next
            l2 = l2.next
    
        if l1 != None:
            while l1 is not None:
                
                remainder = (l1.val + iter_list.val) % 10
                quotient  = (l1.val + iter_list.val) / 10

                iter_list.val  = remainder
                iter_list.next = ListNode(quotient)
                last_prev = iter_list

                iter_list = iter_list.next

                l1 = l1.next
            
        if l2 != None:
            while l2 is not None:
                
                remainder = (l2.val + iter_list.val) % 10
                quotient  = (l2.val + iter_list.val) / 10

                iter_list.val  = remainder
                iter_list.next = ListNode(quotient)
                last_prev = iter_list

                iter_list = iter_list.next

                l2 = l2.next

        if iter_list is not None and iter_list.val == 0:
            del last_prev.next
            last_prev.next = None

        return ret_list
    def create_list(self, num):
        iterator = ListNode(num[0])
        ret_val  = iterator
        i = 1
        while i < len(num):
            iterator.next = ListNode(num[i])
            iterator = iterator.next
            i += 1

        return ret_val


#--------- just for testing ------
s = Solution()

print s.addTwoNumbers( s.create_list([0]), s.create_list([0]) )
print s.addTwoNumbers( s.create_list([3,6]), s.create_list([8,5]) )
