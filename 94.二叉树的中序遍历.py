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
    # 迭代
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        
        # 使用栈来保存节点，以及一个是否访问过该节点的左右子节点的标记
        # 因为只有访问过该节点的左右子节点，才能以正确的顺序将三个节点
        # 依次入栈，否则该节点只作为临时占位，不能收集到最终结果里。
        stack = [(root, False)]
        array = []
        
        while len(stack):
            node, visited = stack.pop()
            if visited:
                # 收集访问过的节点值
                array.append(node.val)
            else:
                # 右节点先入栈
                if node.right:
                    stack.append((node.right, False))
                # 根节点再入栈（并且标记为已访问）
                stack.append((node, True))
                # 左节点最后入栈
                if node.left:
                    stack.append((node.left, False))
        
        return array

# @lc code=end

    # 递归
    def inorderTraversal1(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
        

