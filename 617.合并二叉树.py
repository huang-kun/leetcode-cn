#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 一开始思维陷入了如何用迭代法解决问题，发现并不容易，后来突然想到递归就容易了。
    # 只管合并当前的节点就行，至于它的左右子节点的合并问题，就留给它们自己去处理吧。
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        elif t1:
            return t1
        elif t2:
            return t2
        else:
            return None
        
# @lc code=end

