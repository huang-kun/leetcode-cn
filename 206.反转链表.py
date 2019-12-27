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

    # 递归法
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        new_tail, new_head = self._reverseList(head)
        new_tail.next = None
        return new_head

    # 递归获取原先的next节点，然后反转指向，同时也要将新链表的头节点一起返回
    def _reverseList(self, head: ListNode) -> (ListNode, ListNode):
        if head is None:
            return None, None
        
        old_next, old_tail = self._reverseList(head.next)
        if old_next is not None:
            old_next.next = head
        if old_tail is None:
            old_tail = head
        return head, old_tail

# @lc code=end

    # 迭代法：用栈的特性（后进先出）重新构建出的链表即为反转链表
    def reverseList1(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        stack = []
        n = head
        while n is not None:
            stack.append(n)
            n = n.next
        
        node = stack.pop()
        first = node
        while len(stack) > 0:
            node.next = stack.pop()
            node = node.next
        
        node.next = None
        return first


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


