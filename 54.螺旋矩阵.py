#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

from typing import List

# @lc code=start
class Solution:

    # 我的题解思路：四指针从各自顶点向内环移动
    # https://leetcode-cn.com/problems/spiral-matrix/solution/54luo-xuan-ju-zhen-si-zhi-zhen-cong-ge-zi-ding-dia/

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 矩阵行数
        row = len(matrix)
        # 矩阵列数
        col = len(matrix[0]) if row > 0 else 0
        if row == 0 or col == 0:
            return []
        
        order = []
        # 已经收集的元素个数
        count = 0
        # 在矩阵中需要收集的全部元素数量
        total = row * col
        # 上边界
        minY = 0
        # 右边界
        maxX = col - 1
        # 下边界
        maxY = row - 1
        # 左边界
        minX = 0
        
        # 首先收集原点
        (x, y) = (0, 0)
        order.append(matrix[y][x])
        count += 1
        
        while True:
            # 向右收集
            while x < maxX:
                x += 1
                order.append(matrix[y][x])
                count += 1
            # 缩小上边界
            minY += 1
            # 避免重复收集元素，及时检查收集数量
            if count == total:
                break

            # 向下收集
            while y < maxY:
                y += 1
                order.append(matrix[y][x])
                count += 1
            # 缩小右边界
            maxX -= 1
            # 检查结果
            if count == total:
                break

            # 向左收集
            while x > minX:
                x -= 1
                order.append(matrix[y][x])
                count += 1
            # 缩小下边界
            maxY -= 1
            # 检查结果
            if count == total:
                break

            # 向上收集
            while y > minY:
                y -= 1
                order.append(matrix[y][x])
                count += 1
            # 缩小左边界
            minX += 1
            # 检查结果
            if count == total:
                break
        
        return order

        
# @lc code=end

if __name__ == "__main__":
    s = Solution()

    m1 = [
        [ 1, 2, 3 ],
        [ 4, 5, 6 ],
        [ 7, 8, 9 ]
    ]
    assert s.spiralOrder(m1) == [1,2,3,6,9,8,7,4,5]

    m2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12]
    ]
    assert s.spiralOrder(m2) == [1,2,3,4,8,12,11,10,9,5,6,7]

    m3 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9,10,11,12],
        [13,14,15,16]
    ]
    assert s.spiralOrder(m3) == [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]