#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层次遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 用二维数组按正常的层级来收集节点值，最后反转层级中的节点值
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        array = []
        queue = [(root, 0)]
        for node, level_idx in queue:
            subarr = []
            if level_idx < len(array):
                subarr = array[level_idx]
            else:
                array.append(subarr)

            subarr.append(node.val)

            if node.left:
                queue.append((node.left, level_idx+1))
            if node.right:
                queue.append((node.right, level_idx+1))
        
        for i in range(len(array)):
            if i % 2 != 0:
                array[i].reverse()
        
        return array

        
# @lc code=end

