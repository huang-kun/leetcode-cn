#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 用3指针，交换curr和next的位置
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        
        new_head = head.next
        
        prev = None
        curr = head
        next = head.next
        
        while next:
            curr.next = next.next
            next.next = curr
            if prev:
                prev.next = next
            
            prev = curr
            curr = curr.next
            next = curr.next if curr else None

        return new_head

# @lc code=end

