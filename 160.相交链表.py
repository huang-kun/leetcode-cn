#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
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

    # 这里是我给出的题解，遍历次数比官方的最优题解多了diff次（两个链表长度差值），
    # 时间复杂度为O(m+n)，其中m,n分别为两个链表的长度

    # 思路：如果是长度相同的两个链表，那么只要同时遍历它们，然后依次比较两个
    # 链表中的每个节点是否为同一个节点，就可以找到相交节点。但是实际问题中会
    # 出现长度不相同的链表，所以只要能确定哪个是长链表，哪个是短链表，以及它
    # 们相差的节点个数，就容易了。
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 找到长度较长的链表，和长度较短的链表，以及它们相差的个数
        remain, longer, shorter = None, None, None
        
        a, b = headA, headB
        while a and b:
            a = a.next
            b = b.next
        
        if a is None:
            remain = b
            longer = headB
            shorter = headA
        else:
            remain = a
            longer = headA
            shorter = headB

        diff = 0
        while remain:
            remain = remain.next
            diff += 1
        
        # 在知道了谁是长链表，谁是短链表和它们相差的个数后，开始第二次遍历。
        # 首先让长链表先走完diff次，之后短链表开始加入进来，于是两个链表正
        # 好位于同一个起跑线上，之后一起遍历剩余节点的过程，就相当于遍历两个
        # 长度相同的链表一样，遇到同一个的节点即为它们的相交节点。
        pos1 = longer
        for i in range(diff):
            pos1 = pos1.next

        pos2 = shorter
        while pos1 and pos2:
            if pos1 == pos2:
                return pos1
            pos1 = pos1.next
            pos2 = pos2.next

        return None

# @lc code=end

    # 根据官方题解，依然是使用双指针为两个链表同时进行遍历，短链表首先
    # 遍历结束时，再将指针重新设置到长链表的头部继续遍历；长链表遍历结
    # 束时，再将指针重新设置到短链表的头部，此时已经从短链表交换到长链
    # 表的指针，正好走完了长链表比短链表的长度多出来的部分，于是两个指
    # 针剩余未遍历的链表长度相同，继续遍历过程中只要遇到相同的节点就是
    # 相交节点。如果两个指针交换后没有遇到相交节点，那么它们会同时走到
    # 链表结尾（指向null），所以下面的代码参考了其他用户根据官方题解
    # 的最简洁实现。
    def getIntersectionNode1(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a

# ---------------
# 以下代码为测试用例
# ---------------

def prepareLinkedList(array, endIndex=-1):
    nodes = []
    for (i, num) in enumerate(array):
        if i == endIndex:
            break
        node = ListNode(num)
        if len(nodes) > 0:
            nodes[-1].next = node
        nodes.append(node)
    
    if len(nodes) == 0:
        return None, None
        
    return nodes[0], nodes[-1]

def prepareTestCase(intersectVal, listA, listB, skipA, skipB):
    if intersectVal == 0:
        headA, _ = prepareLinkedList(listA)
        headB, _ = prepareLinkedList(listB)
        return headA, headB, None

    headA, tailA = prepareLinkedList(listA, skipA)
    headB, tailB = prepareLinkedList(listB, skipB)
    
    intersectNode, _ = prepareLinkedList(listA[skipA:])
    assert intersectNode.val == intersectVal

    tailA.next = intersectNode
    tailB.next = intersectNode
    
    return headA, headB, intersectNode

if __name__ == "__main__":
    s = Solution()
    headA, headB, intersectNode = prepareTestCase(8, [4,1,8,4,5], [5,0,1,8,4,5], 2, 3)
    assert s.getIntersectionNode(headA, headB) == intersectNode

    headA, headB, intersectNode = prepareTestCase(2, [0,9,1,2,4], [3,2,4], 3, 1)
    assert s.getIntersectionNode(headA, headB) == intersectNode

    headA, headB, intersectNode = prepareTestCase(0, [2,6,4], [1,5], 3, 2)
    assert s.getIntersectionNode(headA, headB) == intersectNode