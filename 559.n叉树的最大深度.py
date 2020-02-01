#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/description/
#
# algorithms
# Easy (67.37%)
# Likes:    68
# Dislikes: 0
# Total Accepted:    15.5K
# Total Submissions: 22.8K
# Testcase Example:  '[1,null,3,2,4,null,5,6]\r'
#
# 给定一个 N 叉树，找到其最大深度。
# 
# 最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。
# 
# 例如，给定一个 3叉树 :
# 
# 
# 
# 
# 
# 
# 
# 我们应返回其最大深度，3。
# 
# 说明:
# 
# 
# 树的深度不会超过 1000。
# 树的节点总不会超过 5000。
# 
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
    
    #  深度优先遍历：
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0

        # 使用栈来追踪节点，以及该节点所在的层级
        depth = 1
        stack = [(root, depth)]
        
        while len(stack):
            node, level = stack.pop()
            depth = max(depth, level)

            if node.children:
                for child in reversed(node.children):
                    stack.append((child, level+1))
        
        return depth

# @lc code=end

    # 广度优先遍历：
    def maxDepth1(self, root: 'Node') -> int:
        if root is None:
            return 0

        # 使用队列来追踪节点，以及该节点所在的层级
        pos, depth = 0, 1
        queue = [(root, depth)]
        
        while pos < len(queue):
            # 模拟出队操作
            node, level = queue[pos]
            pos += 1
            # 根据当前节点的层级，得出深度
            depth = max(depth, level)
            # 将孩子节点依次进行入队操作
            if node.children:
                for child in node.children:
                    queue.append((child, level+1))
        
        return depth
        

