#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # 候选法：
    # 时间复杂度O(m+n)，其中m,n分别为两个链表各自长度；空间复杂度O(1)
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        
        # 定义当前节点current与候选节点candidate
        (curr, cand) = (l1, l2) if l1.val <= l2.val else (l2, l1)
        head = curr
        
        while curr.next:
            # 让当前节点的下个节点与候选节点进行比较
            # 让结果小的作为当前节点的下个节点，结果大的作为候选节点
            if cand.val < curr.next.val:
                temp = curr.next
                curr.next = cand
                cand = temp
            curr = curr.next
        
        # 连接剩下的候选节点
        curr.next = cand
        
        return head

# @lc code=end

