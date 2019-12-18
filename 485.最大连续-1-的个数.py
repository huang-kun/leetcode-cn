#
# @lc app=leetcode.cn id=485 lang=python3
#
# [485] 最大连续1的个数
#

# 双指针技巧二：快指针+慢指针
# https://leetcode-cn.com/explore/learn/card/array-and-string/201/two-pointer-technique/786/    

from typing import List

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        counter = 0
        for n in nums:
            if n == 0:
                result = max(result, counter)
                counter = 0
            else:
                counter += 1
        
        result = max(result, counter)
        return result

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.findMaxConsecutiveOnes([1,1,0,1,1,1]) == 3
