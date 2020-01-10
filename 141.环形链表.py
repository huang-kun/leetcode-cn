#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 使用快慢双指针判断链表中是否存在环
    # https://leetcode-cn.com/explore/learn/card/linked-list/194/two-pointer-technique/743/
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
                
        return False

# @lc code=end

