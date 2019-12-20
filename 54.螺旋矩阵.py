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
        count = 0
        (maxX, maxY) = (col - 1, row - 1)
        # 在矩阵中需要收集的全部元素数量
        total = row * col

        # 位于左上角的指针p1（限制最小y值的上边界）
        (x1, y1) = (0, 0)
        # 位于右上角的指针p2（限制最大x值的右边界）
        (x2, y2) = (maxX, 0)
        # 位于右下角的指针p3（限制最大y值的下边界）
        (x3, y3) = (maxX, maxY)
        # 位于左下角的指针p4（限制最小x值的左边界）
        (x4, y4) = (0, maxY)
        
        # 将坐标的起始位置设置在最外环的p1这里
        (x, y) = (x1, y1)
        # 收集第一个元素
        order.append(matrix[y][x])
        count += 1
        
        while True:
            # 收集p1 -> p2之间的元素
            while x < x2:
                x += 1
                order.append(matrix[y][x])
                count += 1
            # 向内环方向缩小p1的边界
            (x1, y1) = (min(x4, x2), y1 + 1)
            # 避免重复收集元素，及时检查收集数量
            if count == total:
                break

            # 收集p2 -> p3之间的元素
            while y < y3:
                y += 1
                order.append(matrix[y][x])
                count += 1
            # 向内环方向缩小p2的边界
            (x2, y2) = (x2 - 1, min(y1, y3))
            if count == total:
                break

            # 收集p3 -> p4之间的元素
            while x > x4:
                x -= 1
                order.append(matrix[y][x])
                count += 1
            # 向内环方向缩小p3的边界
            (x3, y3) = (max(x2, x4), y3 - 1)
            if count == total:
                break

            #收集p4 -> p1之间的元素
            while y > y1:
                y -= 1
                order.append(matrix[y][x])
                count += 1
            # 向内环方向缩小p4的边界
            (x4, y4) = (x4 + 1, max(y3, y1))
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