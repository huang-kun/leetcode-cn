#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        if head.next is None:
            return head
        
        # 分别定义奇数链表和偶数链表
        odd, even = None, None
        
        i = 1
        node = head
        ehead = head.next
        
        while node:
            # 对原链表的节点进行分类
            if i % 2 == 0:
                if even:
                    even.next = node
                even = node
            else:
                if odd:
                    odd.next = node
                odd = node
            # 迭代下一个节点
            node = node.next
            i += 1
        
        # 连接奇数链表和偶数链表
        if odd:
            odd.next = ehead
        if even:
            even.next = None
        
        return head

# @lc code=end

