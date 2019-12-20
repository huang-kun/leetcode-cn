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
        end = row * col

        # 位于左上角的指针p1
        (x1, y1) = (0, 0)
        # 位于右上角的指针p2
        (x2, y2) = (maxX, 0)
        # 位于右下角的指针p3
        (x3, y3) = (maxX, maxY)
        # 位于左下角的指针p4
        (x4, y4) = (0, maxY)
        
        # 移动坐标起始于p1
        (x, y) = (x1, y1)
        # 收集第一个元素
        order.append(matrix[y][x])
        count += 1

        # 如果指针移动超过矩阵边长的一半，结束
        while x2 >= x4 and y1 <= y3:
            # 收集p1 -> p2之间的元素
            while x < x2:
                x += 1
                order.append(matrix[y][x])
                count += 1
            # 完成后，向下移动p1
            y1 += 1
            # 避免后续重复收集，需要及时检查收集数量
            if count == end:
                break

            # 收集p2 -> p3之间的元素
            while y < y3:
                y += 1
                order.append(matrix[y][x])
                count += 1
            # 完成后，向左移动p2
            x2 -= 1
            if count == end:
                break

            # 收集p3 -> p4之间的元素
            while x > x4:
                x -= 1
                order.append(matrix[y][x])
                count += 1
            # 完成后，向上移动p3
            y3 -= 1
            if count == end:
                break

            #收集p4 -> p1之间的元素
            while y > y1:
                y -= 1
                order.append(matrix[y][x])
                count += 1
            # 完成后，向右移动p4
            x4 += 1
            if count == end:
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