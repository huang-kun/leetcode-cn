#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0]) if row > 0 else 0
        if row == 0 or col == 0:
            return False

        # 移动搜索原点
        (xo, yo) = (0, 0)
        while xo < col and yo < row:
            # 二分搜索查找行
            (x, y) = (xo, yo)
            minX = xo
            maxX = col - 1
            while minX <= maxX:
                x = (minX + maxX) // 2
                n = matrix[y][x]
                if n > target:
                    maxX = x - 1
                elif n < target:
                    minX = x + 1
                else:
                    return True
            
            # 二分搜索查找列
            (x, y) = (xo, yo)
            minY = yo
            maxY = row - 1
            while minY <= maxY:
                y = (minY + maxY) // 2
                n = matrix[y][x]
                if n > target:
                    maxY = y - 1
                elif n < target:
                    minY = y + 1
                else:
                    return True

            # 更新搜索原点坐标
            xo += 1
            yo += 1

        return False

# @lc code=end

if __name__ == "__main__":
    s = Solution()

    m = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]
    assert s.searchMatrix(m, 5) == True
    assert s.searchMatrix(m, 20) == False