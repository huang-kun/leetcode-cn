#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#

# 题解参考自极客时间
class Solution5:
    # 递归思路，时间复杂度O(N)
    # 如果root是p或q其中之一的话，说明另一个p或q就在子树里，所以当前作为root的p或q就是LCA
    # 如果root不是p或q的话，就去子树里找，如果p或q分别在左右子树中找到的话，那么root就是LCA
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is None:
            return None
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果左子树里找不到，就去右子树里找LCA
        if left is None:
            return right
        # 如果右子树里找不到，就去左子树里找LCA
        elif right is None:
            return left
        # 如果在左右子树中分别找到p和q，说明root是LCA
        else:
            return root

class Solution4:

    # 官方题解思路：无父指针的迭代，使用栈（80 ~ 152ms）
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 记录节点和状态：0未遍历子节点，1已遍历左节点，2已遍历左右子节点
        stack = [[root, 0]]
        find_set = set()
        lca = root

        while len(stack):
            subarr = stack[-1]
            node = subarr[0]
            state = subarr[1]

            if node.val == p.val or node.val == q.val:
                if node.val not in find_set:
                    find_set.add(node.val)
                    if len(find_set) == 2:
                        return lca
                    else:
                        lca = node

            if state == 2:
                stack.pop()
                if lca.val == node.val:
                    lca = stack[-1][0] if len(stack) else None
            elif state == 1:
                if node.right:
                    stack.append([node.right, 0])
            elif state == 0:
                if node.left:
                    stack.append([node.left, 0])
            subarr[1] += 1
                    
        return None

class Solution3:
    # 官方题解思路：递归
    # https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/er-cha-shu-de-zui-jin-gong-gong-zu-xian-by-leetcod/
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = root

        def findLCA(node):
            if node is None:
                return False

            mid = node.val == p.val or node.val == q.val
            left = findLCA(node.left)
            right = findLCA(node.right)
            
            if mid + left + right >= 2:
                nonlocal lca
                lca = node
            
            return mid or left or right
        
        findLCA(root)
        return lca


class Solution2:
    def __init__(self):
        self.cache = {}
        self.pos_p = 0
        self.pos_q = 0

    # 递归撒网找pq（148ms）
    # 找到p和q所在的位置，然后倒推计算出最近的公共祖先的位置
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
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


class Solution1:
    # 遍历撒网找pq（128ms）
    # 找到p和q所在的位置，然后倒推计算出最近的公共祖先的位置
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


from lctest import *
def testCase(treestr, nodestr1, nodestr2):
    root = stringToTreeNode(treestr)
    ans = Solution().lowestCommonAncestor(root, TreeNode(int(nodestr1)), TreeNode(int(nodestr2)))
    return str(ans.val)

if __name__ == "__main__":
    assert testCase("[3,5,1,6,2,0,8,null,null,7,4]", "5", "1") == "3"
    assert testCase("[3,5,1,6,2,0,8,null,null,7,4]", "5", "4") == "5"
