#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next is None:
            return str(self.val) + "->NULL"
        else:
            return str(self.val) + "->" + str(self.next)

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # 递归法：从链表tail开始向前回溯反转
    def reverseList(self, head: ListNode) -> ListNode:
        oldTail = head
        
        def reverse(curr):
            # 如果没有next，即找到tail，返回自己
            if not curr or not curr.next:
                nonlocal oldTail
                oldTail = curr
                return curr
            # 如果有next，递归next，再将返回的next反转指向自己
            next = reverse(curr.next)
            next.next = curr
            curr.next = None
            return curr

        reverse(head)
        return oldTail

# @lc code=end

class Solution2:
    # 迭代法：（官方思路）重复将当前节点的next移动到链表的头部。
    # https://leetcode-cn.com/explore/learn/card/linked-list/195/classic-problems/749/
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        curr = head
        while curr.next:
            next = curr.next
            curr.next = next.next
            next.next = head
            head = next

        return head

    # 递归实现：重复将当前节点的next移动到链表的头部。
    def reverseList2(self, head: ListNode) -> ListNode:
        h = head
        
        def reverse(curr):
            if not curr or not curr.next:
                return

            next = curr.next
            curr.next = next.next
            nonlocal h
            next.next = h
            h = next
            
            reverse(curr)
        
        reverse(head)
        return h

# 指针移动迭代法：
class Solution1:
    # 3个指针一边遍历一边反转，空间复杂度O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        # 定义3个指针
        prev = None
        curr = head
        next = head.next
        while next:
            # 反转当前节点的指向
            curr.next = prev
            # 3个指针依次向前移动
            prev = curr
            curr = next
            next = next.next
        # 反转最后一个节点的指向
        curr.next = prev
        # 最后一个节点成为新的head
        return curr

    # 后来发现用两个指针就够了（参考极客时间算法课）
    def reverseList2(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        return prev

if __name__ == "__main__":
    s = Solution()
    assert s.reverseList(None) == None

    head = None
    temp = None
    for i in range(1, 6):
        node = ListNode(i)
        if head is None:
            head = node
        if temp is not None:
            temp.next = node
        temp = node
    assert str(head) == "1->2->3->4->5->NULL"

    new_head = s.reverseList(head)
    assert str(new_head) == "5->4->3->2->1->NULL"


