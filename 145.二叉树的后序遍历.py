#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
#
# https://leetcode-cn.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (68.96%)
# Likes:    215
# Dislikes: 0
# Total Accepted:    47K
# Total Submissions: 67.3K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 后序 遍历。
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
# 输出: [3,2,1]
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#

# 后序遍历（百度百科）：
# 首先遍历左子树，然后遍历右子树，最后访问根结点。
# 在遍历左、右子树时，仍然先遍历左子树，然后遍历右子树，最后遍历根结点。
# 若二叉树为空则结束返回，否则：
# （1）后序遍历左子树
# （2）后序遍历右子树
# （3）访问根结点
#  比如二叉树：
#       A
#      / \
#     /   \
#    /     \
#   B       C
#  / \     /
# D   E   F
#
# 后序遍历结果为：DEBFCA

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 递归
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
        
# @lc code=end

