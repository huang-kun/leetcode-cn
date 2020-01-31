#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N叉树的后序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/description/
#
# algorithms
# Easy (70.92%)
# Likes:    47
# Dislikes: 0
# Total Accepted:    14.7K
# Total Submissions: 20.5K
# Testcase Example:  '[1,null,3,2,4,null,5,6]\r'
#
# 给定一个 N 叉树，返回其节点值的后序遍历。
# 
# 例如，给定一个 3叉树 :
# 
# 
# 
# 
# 
# 
# 
# 返回其后序遍历: [5,6,3,2,4,1].
# 
# 
# 
# 说明: 递归法很简单，你可以使用迭代法完成此题吗?
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    # 迭代
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        
        array = []
        stack = [(root, False)]
        
        while len(stack):
            node, visited = stack.pop()
            if visited:
                array.append(node.val)
            else:
                stack.append((node, True))
                if node.children:
                    for child in reversed(node.children):
                        stack.append((child, False))

# @lc code=end

    # 递归
    def postorder1(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        
        array = []
        if root.children:
            for child in root.children:
                array += self.postorder(child)
        
        array.append(root.val)
        return array
        

