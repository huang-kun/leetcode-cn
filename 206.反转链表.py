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


# 官方递归题解
class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last

# 官方迭代题解
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

# 官方换头迭代法：重复将当前节点的next移动到链表的头部。
# https://leetcode-cn.com/explore/learn/card/linked-list/195/classic-problems/749/
class Solution3:
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


