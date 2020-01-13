#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # Hint: keep a certain distance between the two pointers.
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head is None or n == 0:
            return head
        
        # 使用快慢双指针，先让快指针提前走完倒数个数n-1次
        fast = head
        for i in range(n-1):
            fast = fast.next
        
        # 快慢指针（通常情况下会保持一定距离）一起走，
        # 当快指针走到尾部，删除的节点就是慢指针的位置
        # prev指针是为了实现删除而记录上一个慢指针的位置
        prev = None
        slow = head
        while fast.next:
            fast = fast.next
            prev = slow
            slow = slow.next
        
        if prev:
            prev.next = slow.next
            slow.next = None
        else:
            # 如果慢指针没有走，说明删除的是head
            head = head.next

        return head

# @lc code=end

# -------
# 测试用例
# -------

def convertArrayToLinkedList(arr):
    if len(arr) == 0:
        return None
    nodes = []
    for i in arr:
        node = ListNode(i)
        if len(nodes) > 0:
            nodes[-1].next = node
        nodes.append(node)
    return nodes[0]

def convertLinkedListToArray(head):
    if head is None:
        return []
    arr = []
    p = head
    while p:
        arr.append(p.val)
        p = p.next
    return arr

def testCase(s, array, n):
    head = convertArrayToLinkedList(array)
    head1 = s.removeNthFromEnd(head, n)
    return convertLinkedListToArray(head1)

if __name__ == "__main__":
    s = Solution()
    assert testCase(s, [1,2,3,4,5], 2) == [1,2,3,5]
    assert testCase(s, [1,2], 2) == [2]
    assert testCase(s, [1], 1) == []