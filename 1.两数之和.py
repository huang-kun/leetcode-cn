#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        stack = nums
        while len(stack) > 1:
            last_num = stack.pop()
            for (i, n) in enumerate(stack):
                if n == target - last_num:
                    return [i, len(stack)]
        return []

# @lc code=end
