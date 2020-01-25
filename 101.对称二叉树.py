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

    # 广度优先遍历：
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        f1, f2 = 0, 0
        queue1, queue2 = [root], [root]
        
        while f1 < len(queue1) and f2 < len(queue2) and len(queue1) == len(queue2):
            # 出队
            node1 = queue1[f1]
            f1 += 1
            node2 = queue2[f2]
            f2 += 1
            
            # 比较
            if node1 is None and node2 is None:
                continue
            elif node1 is None or node2 is None:
                return False
            elif node1.val != node2.val:
                return False
            
            # 入队（一个队列从左向右收集，另一个队列从右向左收集）
            queue1.append(node1.left)
            queue1.append(node1.right)
            queue2.append(node2.right)
            queue2.append(node2.left)
        
        return True

# @lc code=end

    # 根据官方题解，学到了用递归实现的思路。可以参照官方题解关于递归的图片和解释：
    # https://leetcode-cn.com/problems/symmetric-tree/solution/dui-cheng-er-cha-shu-by-leetcode/
    # 如果同时满足下面的条件，两个树互为镜像：
    # 1. 它们的两个根结点具有相同的值。
    # 2. 每个树的右子树都与另一个树的左子树镜像对称。
    def isSymmetric2(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)
    
    def isMirror(self, t1: TreeNode, t2: TreeNode):
        if t1 is None and t2 is None:
            return True
        elif t1 is None or t2 is None:
            return False
        
        return t1.val == t2.val and \
               self.isMirror(t1.left, t2.right) and \
               self.isMirror(t1.right, t2.left)


    # 深度优先遍历法，如果是对称的，说明从左边遍历的结果和从右边遍历的结果是相同的。
    def isSymmetric1(self, root: TreeNode) -> bool:
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

