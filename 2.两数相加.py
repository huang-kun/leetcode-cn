#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head, tail = None, None
        n1, n2 = l1, l2
        # 是否进位
        carry = False
        
        while n1 or n2:
            s = 0
            if n1:
                s += n1.val
            if n2:
                s += n2.val
            
            if carry:
                s += 1
                carry = False
            if s >= 10:
                s -= 10
                carry = True
            else:
                carry = False
                
            node = ListNode(s)
            if head is None:
                head = node
            if tail:
                tail.next = node
            tail = node
            
            if n1:
                n1 = n1.next
            if n2:
                n2 = n2.next
        
        if carry:
            node = ListNode(1)
            tail.next = node
            tail = node
            carry = False
        
        return head
        
# @lc code=end

