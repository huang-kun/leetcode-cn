#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
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
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        node = head
        prev = None
        while node:
            if node.val == val:
                if prev:
                    # 如果val相等，就删除当前node
                    prev.next = node.next
                    node.next = None
                    node = prev.next
                else:
                    # 如果删除的是head，就更新head
                    head = head.next
                    node = head
            else:
                prev = node
                node = node.next
                
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

def testCase(s, arr, val):
    head = convertArrayToLinkedList(arr)
    head1 = s.removeElements(head, val)
    return convertLinkedListToArray(head1)

if __name__ == "__main__":
    s = Solution()
    assert testCase(s, [1,2,6,3,4,5,6], 6) == [1,2,3,4,5]
    assert testCase(s, [1], 1) == []