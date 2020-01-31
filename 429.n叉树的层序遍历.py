#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N叉树的层序遍历
#
# https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Medium (63.54%)
# Likes:    68
# Dislikes: 0
# Total Accepted:    13.5K
# Total Submissions: 21K
# Testcase Example:  '[1,null,3,2,4,null,5,6]\r'
#
# 给定一个 N 叉树，返回其节点值的层序遍历。 (即从左到右，逐层遍历)。
# 
# 例如，给定一个 3叉树 :
# 
# 
# 
# 
# 
# 
# 
# 返回其层序遍历:
# 
# [
# ⁠    [1],
# ⁠    [3,2,4],
# ⁠    [5,6]
# ]
# 
# 
# 
# 
# 说明:
# 
# 
# 树的深度不会超过 1000。
# 树的节点总数不会超过 5000。
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

    # 广度优先遍历：
    # 使用队列在遍历中记录节点，以及当前节点所处层级的index
    # 使用array在遍历中，仅收集child.val就够了，无需收集根节点的val
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []

        pos = 0
        queue = [(root, 0)]
        array = [[root.val]]

        while pos < len(queue):
            node, level = queue[pos]
            pos += 1

            if node.children:
                subarr = []
                nextLevel = level + 1

                if nextLevel < len(array):
                    subarr = array[nextLevel]
                else:
                    array.append(subarr)

                for child in node.children:
                    subarr.append(child.val)
                    queue.append((child, nextLevel))

        return array
        
# @lc code=end

