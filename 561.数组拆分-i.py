#
# @lc app=leetcode.cn id=561 lang=python3
#
# [561] 数组拆分 I
#

from typing import List

# @lc code=start
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        s = 0
        for i in range(0, len(nums), 2):
            s += nums[i]
        return s

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.arrayPairSum([1,4,3,2]) == 4