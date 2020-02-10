#
# @lc app=leetcode.cn id=814 lang=python3
#
# [814] 二叉树剪枝
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 该题不适合使用迭代法，因为迭代一遍到叶子结点进行剪枝后，
    # 还需要从叶子处折返回来进行二次判断，但是递归就可以做到
    # 一边向下递归，一边剪枝。
    def pruneTree(self, root: TreeNode) -> TreeNode:
        # 递归：从值为0的叶子节点开始一点点向上剪枝
        def isZeroTree(node: TreeNode) -> bool:
            if node is None:
                return False
            # 如果左子树满足剪枝条件，剪去
            if isZeroTree(node.left):
                node.left = None
            # 如果右子树满足剪枝条件，剪去
            if isZeroTree(node.right):
                node.right = None
            # 满足剪枝的条件就是：值为0的叶子节点
            return node.val == 0 and node.left is None and node.right is None
            
        isZeroTree(root)
        return root
        
# @lc code=end

