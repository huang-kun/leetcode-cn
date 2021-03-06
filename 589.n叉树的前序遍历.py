#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N叉树的前序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/description/
#
# algorithms
# Easy (70.80%)
# Likes:    62
# Dislikes: 0
# Total Accepted:    16.9K
# Total Submissions: 23.5K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# 给定一个 N 叉树，返回其节点值的前序遍历。
# 
# 例如，给定一个 3叉树 :
# 
# 
# 
# 
# 
# 
# 
# 返回其前序遍历: [1,3,5,6,2,4]。
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
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []
        
        array = []
        stack = [root]
        
        while len(stack):
            node = stack.pop()
            array.append(node.val)

            if node.children:
                for child in reversed(node.children):
                    stack.append(child)
        
        return array

# @lc code=end

    # 递归
    def preorder1(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        array = [root.val]
        if root.children:
            for child in root.children:
                array += self.preorder(child)
        
        return array
        

