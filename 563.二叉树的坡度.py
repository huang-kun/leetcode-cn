#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归法
class Solution:
    def findTilt(self, root: TreeNode) -> int:

        # 递归返回(总坡度, 节点之和)
        def getTiltAndSum(node):
            if node is None:
                return 0, 0
            
            leftTilt, leftSum = getTiltAndSum(node.left)
            rightTilt, rightSum = getTiltAndSum(node.right)
            
            currTilt = abs(leftSum - rightSum)
            totalTilt = currTilt + leftTilt + rightTilt
            totalVal = leftSum + rightSum + node.val
            
            return totalTilt, totalVal

        tilt, _ = getTiltAndSum(root)
        return tilt
        
# @lc code=end

