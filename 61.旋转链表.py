#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
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
    
    # 问题转化思路：向右移动k个位置，相当于将链表中倒数第k个
    #             节点（如果k小于链表长度）作为新链表的head
    # 1. 如果k值等于或超过链表长度，k取余数
    # 2. 找到链表中倒数第k个节点的方法，用快慢指针，让快指针先走k-1步
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or head is None or head.next is None:
            return head
        
        # 链表长度
        l = 0
        # 快指针先走k-1步
        fast = head
        while fast:
            l += 1
            fast = fast.next
        
        # 如果k值等于或超过链表长度，调整k值
        if k >= l:
            k %= l
        if k == 0:
            return head

        # 让快指针先走k-1步
        fast = head
        for _ in range(k-1):
            fast = fast.next
        
        # 找到倒数第k个节点(slow)
        prev = None
        slow = head
        while fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        # 生成新链表
        if prev:
            prev.next = None
        fast.next = head
        return slow

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

def testCase(s, arr, k):
    head = convertArrayToLinkedList(arr)
    head1 = s.rotateRight(head, k)
    return convertLinkedListToArray(head1)

if __name__ == "__main__":
    s = Solution()
    assert testCase(s, [1,2,3,4,5], 2) == [4,5,1,2,3]
    assert testCase(s, [0,1,2], 4) == [2,0,1]
    assert testCase(s, [1,2], 1) == [2,1]
    assert testCase(s, [1,2], 2) == [1,2]