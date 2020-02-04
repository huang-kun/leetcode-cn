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
    # 迭代的方法参考了官方题解中的方法二
    # https://leetcode-cn.com/problems/merge-two-binary-trees/solution/he-bing-er-cha-shu-by-leetcode/
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        # 让两棵树的节点同时入栈，等待出栈后进行合并操作
        stack = [(t1, t2)]
        while len(stack):
            n1, n2 = stack.pop()
            if n1 is None and n2 is None:
                continue

            if n1 and n2:
                # 将两棵树的当前节点值合并到n1
                n1.val = n1.val + n2.val
                # 如果n1没有左子树，就把n2的左子树嫁接过去
                if n1.left is None:
                    n1.left = n2.left
                    n2.left = None
                # 如果n1没有右子树，就把n2的右子树嫁接过去
                if n1.right is None:
                    n1.right = n2.right
                    n2.right = None

            l1 = n1.left if n1 else None
            l2 = n2.left if n2 else None

            r1 = n1.right if n1 else None
            r2 = n2.right if n2 else None

            if l1 or l2:
                # 继续将两颗树当前节点的左子节点一起入栈
                stack.append((l1, l2))
            if r1 or r2:
                # 继续将两颗树当前节点的右子节点一起入栈
                stack.append((r1, r2))

        return t1

# @lc code=end

    # 一开始思维陷入了如何用迭代法解决问题，发现并不容易，后来突然想到递归就容易了。
    # 只管合并当前的节点就行，至于它的左右子节点的合并问题，就留给它们自己去处理吧。
    def mergeTrees1(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
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
        

