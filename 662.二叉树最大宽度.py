#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
#
# https://leetcode-cn.com/problems/maximum-width-of-binary-tree/description/
#
# algorithms
# Medium (34.38%)
# Likes:    65
# Dislikes: 0
# Total Accepted:    4.2K
# Total Submissions: 12.1K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# 给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary
# tree）结构相同，但一些节点为空。
# 
# 每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。
# 
# 示例 1:
# 
# 
# 输入: 
# 
# ⁠          1
# ⁠        /   \
# ⁠       3     2
# ⁠      / \     \  
# ⁠     5   3     9 
# 
# 输出: 4
# 解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
# 
# 
# 示例 2:
# 
# 
# 输入: 
# 
# ⁠         1
# ⁠        /  
# ⁠       3    
# ⁠      / \       
# ⁠     5   3     
# 
# 输出: 2
# 解释: 最大值出现在树的第 3 层，宽度为 2 (5,3)。
# 
# 
# 示例 3:
# 
# 
# 输入: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2 
# ⁠      /        
# ⁠     5      
# 
# 输出: 2
# 解释: 最大值出现在树的第 2 层，宽度为 2 (3,2)。
# 
# 
# 示例 4:
# 
# 
# 输入: 
# 
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      /     \  
# ⁠     5       9 
# ⁠    /         \
# ⁠   6           7
# 输出: 8
# 解释: 最大值出现在树的第 4 层，宽度为 8 (6,null,null,null,null,null,null,7)。
# 
# 
# 注意: 答案在32位有符号整数的表示范围内。
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
    # 官方题解方法1：宽度优先搜索
    # https://leetcode-cn.com/problems/maximum-width-of-binary-tree/solution/er-cha-shu-zui-da-kuan-du-by-leetcode/
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        # 模拟队列，记录节点（包括null），当前层级，节点位置
        queue = [(root, 1, 1)]
        width = 1
        curr_level = 1
        # 当前level里，左边第一个非空节点的节点位置
        left = 1

        for node, level, pos in queue:
            if node is None:
                continue
            
            # 只有在非空节点下，更新宽度（才有意义）
            if curr_level < level:
                curr_level = level
                left = pos
            width = max(width, pos - left + 1)
            
            # 继续层级遍历
            queue.append((node.left, level+1, 2*pos))
            queue.append((node.right, level+1, 2*pos+1))
            
        return width
        
# @lc code=end

