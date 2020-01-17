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

    # 队列思路：
    # 把链表看作成一个队列，向左移动就是一次出队(dequeue)再加上一次入队(inqueue)
    # 的过程，所以可以把向右移动转换成向左移动，通过重复出队和入队实现移动
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or head is None or head.next is None:
            return head

        # 找到tail和链表长度
        l = 1
        tail = head
        while tail.next:
            l += 1
            tail = tail.next
        
        # 如果k值等于或超过链表长度，调整k值
        if k >= l:
            k %= l
        if k == 0:
            return head
        
        # 将向右移动转换成向左移动
        m = l - k
        for _ in range(m):
            # 出队
            node = head
            head = head.next
            node.next = None
            # 入队
            tail.next = node
            tail = tail.next

        return head

# @lc code=end
            
    # 倒数第k个思路：
    # 向右移动k个位置，相当于将链表中倒数第k个节点（如果k小于链表长度）
    # 作为新链表的head
    
    # 算法步骤：
    # 1. 如果k值等于或超过链表长度，k取余数
    # 2. 找到链表中倒数第k个节点的方法，用快慢指针，让快指针先走k-1步
    def rotateRight1(self, head: ListNode, k: int) -> ListNode:
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