#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    # 根据官方题解，一遍哈希表：
    def twoSum(self, nums, target):
        # 每次使用字典保存访问过的数字和下标，以空间换时间
        d = {}
        for i, n in enumerate(nums):
            complement = target - n
            if complement in d:
                return [d[complement], i]
            else:
                d[n] = i
        
        return []


# @lc code=end

    def twoSum1(self, nums, target):
        stack = nums
        while len(stack) > 1:
            last_num = stack.pop()
            for (i, n) in enumerate(stack):
                if n == target - last_num:
                    return [i, len(stack)]
        return []


