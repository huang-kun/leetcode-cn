#
# @lc app=leetcode.cn id=102 lang=python3
#
# [102] 二叉树的层次遍历
#
# https://leetcode-cn.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (59.90%)
# Likes:    355
# Dislikes: 0
# Total Accepted:    71.6K
# Total Submissions: 118.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。
# 
# 例如:
# 给定二叉树: [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 返回其层次遍历结果：
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        # 收集结果
        array = []
        # 广度优先遍历：使用队列来记录节点和所在level
        first = 0
        queue = [(root, 0)]
        
        while first < len(queue):
            # 出队
            node, level = queue[first]
            first += 1
            
            # 收集当前level的节点val
            if level < len(array):
                subarr = array[level]
                subarr.append(node.val)
            else:
                subarr = [node.val]
                array.append(subarr)
            
            # 入队
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        
        return array
        
# @lc code=end

