#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#
# https://leetcode-cn.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (62.73%)
# Likes:    196
# Dislikes: 0
# Total Accepted:    62.9K
# Total Submissions: 98.8K
# Testcase Example:  '[1,null,2,3]'
#
# 给定一个二叉树，返回它的 前序 遍历。
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
# 输出: [1,2,3]
# 
# 
# 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
# 
#

# 前序遍历特点（摘自百度百科）：
# 前序遍历首先访问根结点然后遍历左子树，最后遍历右子树。
# 在遍历左、右子树时，仍然先访问根结点，然后遍历左子树，最后遍历右子树。
#
# 若二叉树为空则结束返回，否则：
# （1）访问根结点。
# （2）前序遍历左子树。
# （3）前序遍历右子树。
#  需要注意的是：遍历左右子树时仍然采用前序遍历方法。
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
# 前序遍历结果为：ABDECF

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 递归
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

# @lc code=end

    # 非递归
    def preorderTraversal1(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        # 使用栈（后进先出），先进右，再进左
        stack = [root]
        array = []
        while len(stack):
            node = stack.pop()
            array.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return array
        

