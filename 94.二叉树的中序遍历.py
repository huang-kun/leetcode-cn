#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#
# https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (69.13%)
# Likes:    376
# Dislikes: 0
# Total Accepted:    96.2K
# Total Submissions: 137.9K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的中序 遍历。
# 
# 示例:
# 
# 输入: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# 输出: [1,3,2]
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#

# 中序遍历（百度百科）：
# 首先遍历左子树，然后访问根结点，最后遍历右子树。若二叉树为空则结束返回，否则
# （1）中序遍历左子树
# （2）访问根结点
# （3）中序遍历右子树
#
#  比如二叉树：
#       A
#      / \
#     /   \
#    /     \
#   B       C
#  / \     /
# D   E   F
#
# 中序遍历结果为：DBEAFC

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 递归
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        
# @lc code=end

