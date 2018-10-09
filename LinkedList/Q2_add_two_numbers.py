# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None or l2 == None:
            l = ListNode(0)
            return l
        params = 0
        l = None
        while l1 != None and l2 != None:
            num = l1.val + l2.val + params
            if num > 9:
                num = num - 10
                params = 1
            else:
                params = 0
            if l == None:
                l = ListNode(num)
                t = l
            else:
                p = ListNode(num)
                t.next = p
                p = p.next
                t = t.next
            l1 = l1.next
            l2 = l2.next
        while l1 == None and l2 != None:
            num = l2.val + params
            if num > 9:
                num = num - 10
                params = 1
            else:
                params = 0
            if l == None:
                l = ListNode(num)
                t = l
            else:
                p = ListNode(num)
                t.next = p
                p = p.next
                t = t.next
            l2 = l2.next
        while l1 != None and l2 == None:
            num = l1.val + params
            if num > 9:
                num = num - 10
                params = 1
            else:
                params = 0
            if l == None:
                l = ListNode(num)
                t = l
            else:
                p = ListNode(num)
                t.next = p
                p = p.next
                t = t.next
            l1 = l1.next
        while l1 == None and l2 == None:
            if params > 0:
                num = params
                if l == None:
                    l = ListNode(num)
                    t = l
                else:
                    p = ListNode(num)
                    t.next = p
                    p = p.next
                    t = t.next
                return l
            else:
                return l
