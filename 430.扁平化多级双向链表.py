#
# @lc app=leetcode.cn id=430 lang=python3
#
# [430] 扁平化多级双向链表
#

class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

    def append(self, node):
        self.next = node
        node.prev = self

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        self._flatten(head)
        return head
    
    def _flatten(self, head: 'Node') -> 'Node':
        """扁平化链表，传入head，返回tail"""
        node = head
        prev = head
        
        while node:
            # 如果该节点有孩子，就找到子链表的tail
            if node.child:
                child_head = node.child
                child_tail = self._flatten(child_head)
                # 将子链表插入到当前节点与下个节点之间
                old_next = node.next
                node.next = child_head
                child_tail.next = old_next
                child_head.prev = node
                if old_next:
                    old_next.prev = child_tail
                node.child = None
            else:
                prev = node
                node = node.next
        
        return prev

# @lc code=end

# -------
# 测试用例
# -------

def validateDoubleLinkedList(head):
    node = head
    while node and node.next:
        if node.next.prev != node:
            return False
        node = node.next
    return True

def convertLinkedListToArray(head):
    if head is None:
        return []
    arr = []
    node = head
    while node:
        arr.append(node.val)
        node = node.next
    return arr

def convertArrayToDoubleLinkedList(arr):
    head = None
    tail = None
    for num in arr:
        node = Node(num)
        if head is None:
            head = node
        if tail:
            tail.next = node
            node.prev = tail
        tail = node
    return head

def convertArrayToMultiLevelLinkedList(arr):
    compos = []
    for compo in genCompo(arr):
        compos.append(compo)
    
    tempList = None
    for compo in reversed(compos):
        if tempList is None:
            tempList = compo[0]
        else:
            subHead, childPos = compo
            node = subHead
            for i in range(1, childPos):
                node = node.next
            node.child = tempList
            tempList = subHead
    return tempList

def genCompo(arr):
    """将数组分割成子链表，以及 每个子链表中child所在的位置"""
    subarr = []
    nullCount = 0
    for i in range(len(arr)):
        item = arr[i]
        if item and nullCount > 0:
            head = convertArrayToDoubleLinkedList(subarr)
            yield (head, nullCount)
            subarr = []
            nullCount = 0
        if item:
            subarr.append(item)
        else:
            nullCount += 1
    head = convertArrayToDoubleLinkedList(subarr)
    yield (head, nullCount)

def testCase(s, arr):
    head = convertArrayToMultiLevelLinkedList(arr)
    head1 = s.flatten(head)
    assert validateDoubleLinkedList(head1) == True
    return convertLinkedListToArray(head1)
        
if __name__ == "__main__":
    s = Solution()
    arr = [1,2,3,4,5,6,None,None,None,7,8,9,10,None,None,11,12]
    assert testCase(s, arr) == [1,2,3,7,8,11,12,9,10,4,5,6]