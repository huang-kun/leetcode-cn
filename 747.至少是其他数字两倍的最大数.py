#
# @lc app=leetcode.cn id=747 lang=python3
#
# [747] 至少是其他数字两倍的最大数
#

from typing import List

# @lc code=start
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        # 获取列表中最大和第二大的数字
        max_num, second_max_num = 0, 0
        index = 0
        for (i, n) in enumerate(nums):
            if max_num < n:
                second_max_num = max_num
                max_num = n
                index = i
            elif second_max_num < n:
                second_max_num = n
        
        if max_num >= second_max_num * 2:
            return index
        else:
            return -1

        
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.dominantIndex([0,0,0,1]) == 3
    assert s.dominantIndex([0,0,3,2]) == -1
    assert s.dominantIndex([3,6,1,0]) == 1
    assert s.dominantIndex([1,2,3,4]) == -1