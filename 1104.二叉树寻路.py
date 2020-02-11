#
# @lc app=leetcode.cn id=1104 lang=python3
#
# [1104] 二叉树寻路
#

from typing import List
import math

# @lc code=start
class Solution:
    # 算法思路：想象在正常完全二叉树的情况下，如何从节点label开始寻找
    # 所有的父节点？该题目就是将偶数level的节点全部倒叙排列了而已。
    #
    # 最开始我尝试用数组来建立一个从根节点开始到label的二叉树，因为
    # label=691938的测试用例导致结果超时，所以我才打算从直接从label
    # 开始收集父节点，遇到偶数level的话，就保持在正常二叉树的节点位置
    # 不变，而去收集一个计算倒叙位置上的节点值就行。
    def pathInZigZagTree(self, label: int) -> List[int]:
        # 计算出label所在的二叉树层级level
        level = math.log(label, 2) + 1
        level = math.floor(level)

        arr = []
        # 正常二叉树的节点值
        i = label
        # 需要被收集的节点值（包括偶数level下反转后的节点值）
        j = label

        while i > 0:
            j = i
            if level % 2 == 0:
                # 当前level中的节点个数
                count = 2 ** (level - 1)
                # 正常情况下，当前level中的第一个节点的值
                start = 2 ** (level - 1)
                # 正常情况下，当前level中的最后一个节点的值
                end = start + count - 1
                # 调整i为正常值
                if i == label:
                    i = end - label + start
                # 计算当前节点在当前level中的起始偏移量
                offset = i - start
                # 在偶数level中的当前节点值就等于正常二叉树
                # 在这层level下的节点(end - offset)的值
                j = end - offset
            # 收集节点
            arr.append(j)
            # 寻找父节点
            i //= 2
            level -= 1

        arr.reverse()
        return arr
        
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.pathInZigZagTree(14) == [1,3,4,14]
    assert s.pathInZigZagTree(16) == [1,3,4,15,16]
    assert s.pathInZigZagTree(26) == [1,2,6,10,26]
    assert s.pathInZigZagTree(691938) == [1, 2, 6, 10, 26, 42, 107, 168, 430, 675, 1720, 2702, 6882, 10811, 27528, 43246, 110115, 172984, 440462, 691938]