#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (49.15%)
# Likes:    579
# Dislikes: 0
# Total Accepted:    86K
# Total Submissions: 173.6K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给定一个二叉树，检查它是否是镜像对称的。
# 
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠/ \ / \
# 3  4 4  3
# 
# 
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   2
# ⁠  \   \
# ⁠  3    3
# 
# 
# 说明:
# 
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
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
    # 深度优先遍历法，如果是对称的，说明从左边遍历的结果和从右边遍历的结果是相同的。
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        stack1 = [root]
        stack2 = [root]
        
        while len(stack1) == len(stack2) and len(stack1) > 0:
            node1 = stack1.pop()
            node2 = stack2.pop()
            
            if node1 is None and node2 is None:
                continue
            elif node1 is None or node2 is None:
                return False
            
            if node1.val != node2.val:
                return False
            
            # stack1先收集左边的子节点，再收集右边的子节点，必须也包括空节点
            stack1.append(node1.left)
            stack1.append(node1.right)
            # stack2先收集右边的子节点，再收集左边的子节点，必须也包括空节点
            stack2.append(node2.right)
            stack2.append(node2.left)
            
        return len(stack1) == len(stack2) and len(stack1) == 0
        
# @lc code=end

