__author__ = 'jasonleaster'

class Solution:
    def merge(self, header_1, header_2):
        dumb = ListNode(0)

    def sortList(self, head):
        fast = head
        slow = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        middle = slow
