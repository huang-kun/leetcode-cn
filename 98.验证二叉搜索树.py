#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
# https://leetcode-cn.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (27.97%)
# Likes:    379
# Dislikes: 0
# Total Accepted:    61.5K
# Total Submissions: 216.3K
# Testcase Example:  '[2,1,3]'
#
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 
# 假设一个二叉搜索树具有如下特征：
# 
# 
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
# 
# 
# 示例 1:
# 
# 输入:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 输出: true
# 
# 
# 示例 2:
# 
# 输入:
#    5
#   / \
#  1   4
#     / \
#    3   6
# 输出: false
# 解释: 输入为: [5,1,4,null,null,3,6]。
# 根节点的值为 5 ，但是其右子节点值为 4 。
# 
# 
#

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# ----------------------------------------------------
# 方法1：范围限制（递归）
#
# 比如二叉搜索树：
#  10
#  / \
# 5  15
#    / \
#   12 20
#
# 二叉搜索树的每个节点的值都是限制在一个(min, max)区间内的，
# 而min和max的值都是继承自父节点的，所以验证二叉搜索树的方法
# 就是：
# 1. 判断当前节点是否满足min < root.val < max
# 2. 如果当前节点满足条件，再去递归判断左右子节点
#    是否都满足条件，并且更新min和max
#
#         -inf<[10]<+inf
#             /    \
#           /        \
#         /            \
#  -inf<[5]<10      10<[15]<+inf
#                      /   \
#                    /       \
#                  /           \
#             10<[12]<15   15<[20]<+inf
#
class Solution1:
    def isValidBST(self, root: TreeNode) -> bool:
        # 满足二叉搜索树的条件：min < root.val < max
        def isBST(root, min, max):
            if root is None:
                return True
            
            val = root.val
            if val <= min or val >= max:
                return False
            
            return isBST(root.left, min, val) and \
                    isBST(root.right, val, max)
        
        return isBST(root, float('-inf'), float('inf'))

# ----------------------------------------------------
# 方法2：范围限制（迭代），原理同上
#
class Solution2:
    # 广度优先遍历法：
    def isValidBST(self, root: TreeNode) -> bool:
        """满足二叉搜索树的条件：minVal < node.val < maxVal"""
        if root is None:
            return True
        
        # 用（伪）队列来记录每个节点以及节点值的有效范围
        first = 0
        queue = [(root, None, None)]
        while first < len(queue):
            # 出队
            node, minVal, maxVal = queue[first]
            first += 1
            
            if node is None:
                continue
            if minVal is not None and node.val <= minVal:
                return False
            if maxVal is not None and node.val >= maxVal:
                return False
            
            # 入队
            queue.append((node.left, minVal, node.val))
            queue.append((node.right, node.val, maxVal))
        
        return True

    # 深度优先遍历法：
    def isValidBST2(self, root: TreeNode) -> bool:
        """满足二叉搜索树的条件：minVal < node.val < maxVal"""
        if root is None:
            return True
        
        # 用栈来记录每个节点以及节点值的有效范围
        stack = [(root, None, None)]
        while len(stack):
            # 出栈
            node, minVal, maxVal = stack.pop()
            
            if node is None:
                continue
            if minVal is not None and node.val <= minVal:
                return False
            if maxVal is not None and node.val >= maxVal:
                return False
            
            # 入栈
            stack.append((node.left, minVal, node.val))                
            stack.append((node.right, node.val, maxVal))
        
        return True

# ----------------------------------------------------
# 方法3：中序遍历（左->根->右），题解来源于极客时间
# 如果是标准二叉搜索树的话，使用中序遍历把树转换成数组，那么一定
# 会得到一个升序排列的数组。实现这个算法的时候，也可以进一步优化，
# 比如在中序遍历过程中，每次记录上一个节点prev，确保prev的值总是
# 小于当前节点值。
#
class Solution3:
    def __init__(self):
        self.prev = None

    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left):
            return False
        if self.prev and self.prev.val >= root.val:
            return False
        
        self.prev = root
        return self.isValidBST(root.right)

# -------
# 测试用例
# -------

def indexOfLastNode(nodeList):
    """返回最后一个不是None的节点的index"""
    if nodeList == []:
        return -1
    for i in range(len(nodeList)-1, -1, -1):
        if nodeList[i] is not None:
            return i
    return -1

def makeNode(val):
    """生成树节点"""
    if val is None:
        return None
    return TreeNode(val)

def convertTree(tree):
    """树 -> 数组"""
    if tree is None:
        return []
    
    first = 0
    queue = [tree]
    while first < len(queue):
        # dequeue
        node = queue[first]
        first += 1

        if node is None:
            continue

        # inqueue
        queue.append(node.left)
        queue.append(node.right)
    
    # 除去尾部多余的null
    last = indexOfLastNode(queue)
    queue = queue[:last+1]
    # 取出val
    return list(map(lambda x: x if x is None else x.val, queue))

def convertArray(array):
    """数组 -> 树"""
    if array is None or array == []:
        return None

    count = len(array)
    nodes = list(map(lambda x: makeNode(x), array))
    for parentIdx, parent in enumerate(nodes):
        leftChildIdx = parentIdx * 2 + 1
        if leftChildIdx < count:
            leftChild = nodes[leftChildIdx]
            parent.left = leftChild
        rightChildIdx = parentIdx * 2 + 2
        if rightChildIdx < count:
            rightChild = nodes[rightChildIdx]
            parent.right = rightChild

    return nodes[0]

def testCase(s, array):
    tree = convertArray(array)
    return s.isValidBST(tree)

if __name__ == '__main__':
    s = Solution1()
    assert testCase(s, [2,1,3]) == True
    assert testCase(s, [5,1,4,None,None,3,6]) == False
    assert testCase(s, [1,1]) == False
