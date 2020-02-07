#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or p is None or q is None:
            return None
        
        # 遍历树，找到p和q的位置
        stack = [(root, 1)]
        cache = {}
        pos_p = 0
        pos_q = 0

        while len(stack):
            node, pos = stack.pop()
            cache[pos] = node
            
            if node.val == p.val:
                pos_p = pos
            elif node.val == q.val:
                pos_q = pos
            
            if pos_p and pos_q:
                break

            if node.left:
                stack.append((node.left, 2*pos))
            if node.right:
                stack.append((node.right, 2*pos+1))

        # 寻找p和q的公共祖先
        s = set([pos_p, pos_q])
        while pos_p or pos_q:
            pos_p //= 2
            pos_q //= 2

            if pos_p in s:
                return cache[pos_p]
            elif pos_p:
                s.add(pos_p)
            
            if pos_q in s:
                return cache[pos_q]
            elif pos_q:
                s.add(pos_q)

        # 如果没有找到公共祖先，返回根节点作为公共祖先
        return root
        
# @lc code=end

