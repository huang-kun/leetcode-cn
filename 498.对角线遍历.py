#
# @lc app=leetcode.cn id=498 lang=python3
#
# [498] 对角线遍历
#

from typing import List

# @lc code=start
class Solution:

    # 参考用户Ikaruga的思路
    # https://leetcode-cn.com/problems/diagonal-traverse/solution/dui-jiao-xian-bian-li-fen-xi-ti-mu-zhao-zhun-gui-l/

    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        order = []
        # 矩阵行数
        row = len(matrix)
        # 矩阵列数
        col = len(matrix[0]) if row > 0 else 0
        # 矩阵原点（左上角）
        (x, y) = (0, 0)
        # 矩阵距离原点最远的点（右下角）
        (maxX, maxY) = (col - 1, row - 1)
        # 对角线的下标，即坐标轴x,y的和，同一条对角线上的元素坐标中x+y都是相同的
        diagIdx = 0
        # 对角线方向，down表示沿左下方向
        down = False
        # 从矩阵原点到最远点的方向，遍历每条对角线
        while diagIdx <= maxX + maxY:
            # 朝向为左下方的对角线
            if down:
                # 找到这条对角线右上方起始元素的坐标（x最大，y最小）
                (x, y) = (diagIdx, 0)
                if x > maxX:
                    (x, y) = (maxX, diagIdx - maxX)
                # 收集元素并沿着对角线一路向下，寻找下个元素（x递减，y递增）
                while x >= 0 and y <= maxY:
                    elem = matrix[y][x]
                    order.append(elem)
                    x -= 1
                    y += 1

            # 朝向为右上方的对角线
            else:
                # 找到这条对角线左下方起始元素的坐标（x最小，y最大）
                (x, y) = (0, diagIdx)
                if y > maxY:
                    (x, y) = (diagIdx - maxY, maxY)
                # 收集元素并沿着对角线一路向上，寻找下个元素（x递增，y递减）
                while y >= 0 and x <= maxX:
                    elem = matrix[y][x]
                    order.append(elem)
                    x += 1
                    y -= 1
            
            # 更新到下一条对角线
            diagIdx += 1
            down = not down

        return order
        
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,4,7,5,3,6,8,9]
    assert s.findDiagonalOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,5,9,6,3,4,7,10,11,8,12]
    assert s.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9],[10,11,12]]) == [1,2,4,7,5,3,6,8,10,11,9,12]
    assert s.findDiagonalOrder([]) == []
