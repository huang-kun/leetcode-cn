#
# @lc app=leetcode.cn id=138 lang=python3
#
# [138] 复制带随机指针的链表
#
# https://leetcode-cn.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (40.45%)
# Likes:    174
# Dislikes: 0
# Total Accepted:    17.3K
# Total Submissions: 41K
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]\r'
#
# 给定一个链表，每个节点包含一个额外增加的随机指针，该指针可以指向链表中的任何节点或空节点。
# 
# 要求返回这个链表的 深拷贝。 
# 
# 我们用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：
# 
# 
# val：一个表示 Node.val 的整数。
# random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 
# 输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
# 
# 
# 示例 2：
# 
# 
# 
# 输入：head = [[1,1],[2,1]]
# 输出：[[1,1],[2,1]]
# 
# 
# 示例 3：
# 
# 
# 
# 输入：head = [[3,null],[3,0],[3,null]]
# 输出：[[3,null],[3,0],[3,null]]
# 
# 
# 示例 4：
# 
# 输入：head = []
# 输出：[]
# 解释：给定的链表为空（空指针），因此返回 null。
# 
# 
# 
# 
# 提示：
# 
# 
# -10000 <= Node.val <= 10000
# Node.random 为空（null）或指向链表中的节点。
# 节点数目不超过 1000 。
# 
# 
#

class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:

    def __init__(self):
        # key是原来的链表节点
        # value是拷贝原节点后的链表节点
        self.cache = {}

    # 参照官方题解的方法一：回溯
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        if head in self.cache:
            return self.cache[head]
        
        node = Node(head.val, None, None)
        self.cache[head] = node

        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node

# @lc code=end

# -------
# 测试用例
# -------

def convertArray(array):
    nodes = []
    for subarr in array:
        val = subarr[0]
        node = Node(val, None, None)
        if len(nodes) > 0:
            last = nodes[-1]
            last.next = node
        nodes.append(node)
    
    l = len(nodes)
    if l == 0:
        return None
    
    head = nodes[0]
    for i in range(l):
        subarr = array[i]
        index = subarr[1]
        node = nodes[i]
        node.random = findNode(head, index)

    return head

def convertList(head):
    array = []
    node = head
    while node:
        index = findIndex(head, node.random)
        subarr = [node.val, index]
        array.append(subarr)
        node = node.next
    return array

def findNode(head, index):
    if index is None:
        return None
    
    i = 0
    node = head
    while node:
        if i == index:
            return node
        node = node.next
        i += 1

    return node

def findIndex(head, node):
    if head is None or node is None:
        return None

    i = 0
    curr = head
    while curr:
        if curr == node:
            return i
        curr = curr.next
        i += 1

    return None

def testCase(s, array):
    head = convertArray(array)
    head1 = s.copyRandomList(head)
    array1 = convertList(head1)
    assert array == array1

if __name__ == '__main__':
    s = Solution()
    testCase(s, [[7,None],[13,0],[11,4],[10,2],[1,0]])
    testCase(s, [[3,None],[3,0],[3,None]])
    testCase(s, [[1,1],[2,1]])
    testCase(s, [])