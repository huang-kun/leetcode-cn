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
    
    def __init__(self):
        self.cache = {}
        self.pos_p = 0
        self.pos_q = 0
        self.ans = None

    # 官方题解：递归（80ms）
    # https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/er-cha-shu-de-zui-jin-gong-gong-zu-xian-by-leetcod/
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def findAncestor(node):
            if node is None:
                return False
            is_node = node.val == p.val or node.val == q.val
            in_left = findAncestor(node.left)
            in_right = False
            if is_node and in_left:
                self.ans = node
            else:
                in_right = findAncestor(node.right)
                if is_node and in_right:
                    self.ans = node
                elif in_left and in_right:
                    self.ans = node
            return is_node or in_left or in_right
        
        findAncestor(root)
        return self.ans

# @lc code=end

    # 递归撒网找pq（148ms）
    # 找到p和q所在的位置，然后倒推计算出最近的公共祖先的位置
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None or p is None or q is None:
            return None

        self.findPQ(root, 1, p.val, q.val)

        pos_p = self.pos_p
        pos_q = self.pos_q
        s = set([pos_p, pos_q])
        while pos_p or pos_q:
            pos_p //= 2
            if pos_p in s:
                return self.cache[pos_p]
            elif pos_p:
                s.add(pos_p)
            
            pos_q //= 2
            if pos_q in s:
                return self.cache[pos_q]
            elif pos_q:
                s.add(pos_q)
        
        return root

    def findPQ(self, root: 'TreeNode', pos: int, val_p: int, val_q: int):
        if root is None:
            return
        
        self.cache[pos] = root
        
        if root.val == val_p:
            self.pos_p = pos
        elif root.val == val_q:
            self.pos_q = pos
        
        if self.pos_p and self.pos_q:
            return
        
        if root.left:
            self.findPQ(root.left, 2*pos, val_p, val_q)
        if root.right:
            self.findPQ(root.right, 2*pos+1, val_p, val_q)

    # 遍历撒网找pq（128ms）
    # 找到p和q所在的位置，然后倒推计算出最近的公共祖先的位置
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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
        

