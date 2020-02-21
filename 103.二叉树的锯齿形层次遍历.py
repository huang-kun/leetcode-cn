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

class Solution:

    # 用双栈，从第1层算起：
    # 1. 根据当前层数来选择栈进行弹出遍历，如果当前栈空了，更新层级
    # 2. 用一个栈收集偶数层的节点，因为遍历顺序是反向的，所以要从左往右正向收集
    # 3. 用另一个栈收集奇数层节点，因为遍历顺序是正向的，所以要从右往左倒着收集
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        level = 1
        s1, s2, array = [root], [], []

        while len(s1) or len(s2):
            node = None
            if level % 2 != 0:
                node = s1.pop()

                subarr = []
                if level-1 < len(array):
                    subarr = array[level-1]
                else:
                    array.append(subarr)
                subarr.append(node.val)

                if node.left:
                    s2.append(node.left)
                if node.right:
                    s2.append(node.right)

                if len(s1) == 0:
                    level += 1
            else:
                node = s2.pop()

                subarr = []
                if level-1 < len(array):
                    subarr = array[level-1]
                else:
                    array.append(subarr)
                subarr.append(node.val)

                if node.right:
                    s1.append(node.right)
                if node.left:
                    s1.append(node.left)
                    
                if len(s2) == 0:
                    level += 1
        
        return array

class Solution1:
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

