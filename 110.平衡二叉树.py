#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
# https://leetcode-cn.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (49.17%)
# Likes:    209
# Dislikes: 0
# Total Accepted:    45.2K
# Total Submissions: 91.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，判断它是否是高度平衡的二叉树。
# 
# 本题中，一棵高度平衡二叉树定义为：
# 
# 
# 一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。
# 
# 
# 示例 1:
# 
# 给定二叉树 [3,9,20,null,null,15,7]
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回 true 。
# 
# 示例 2:
# 
# 给定二叉树 [1,2,2,3,3,null,null,4,4]
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# 返回 false 。
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

    def __init__(self):
        self.cache = {}

    # 从根节点开始，计算出左右子树的高度差，如果满足条件，就继续检验左右子树，
    # 如果出现不满足条件的子树，说明这棵树不是平衡二叉树
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True

        lh = self.getHeight(root.left)
        rh = self.getHeight(root.right)
        
        if abs(lh - rh) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
    
    # 为了提速，使用了cache字典来缓存每个子树的高度，避免多次递归计算
    def getHeight(self, root: TreeNode) -> int:
        if root is None:
            return 0

        if root in self.cache:
            return self.cache[root]

        lh = self.getHeight(root.left)
        rh = self.getHeight(root.right)
        height = max(lh, rh) + 1

        self.cache[root] = height
        return height
        
# @lc code=end

