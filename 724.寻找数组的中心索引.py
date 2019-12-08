#
# @lc app=leetcode.cn id=724 lang=python3
#
# [724] 寻找数组的中心索引
#
# https://leetcode-cn.com/problems/find-pivot-index/description/
#
# algorithms
# Easy (35.56%)
# Likes:    134
# Dislikes: 0
# Total Accepted:    22.3K
# Total Submissions: 62.7K
# Testcase Example:  '[1,7,3,6,5,6]'
#
# 给定一个整数类型的数组 nums，请编写一个能够返回数组“中心索引”的方法。
# 
# 我们是这样定义数组中心索引的：数组中心索引的左侧所有元素相加的和等于右侧所有元素相加的和。
# 
# 如果数组不存在中心索引，那么我们应该返回 -1。如果数组有多个中心索引，那么我们应该返回最靠近左边的那一个。
# 
# 示例 1:
# 
# 
# 输入: 
# nums = [1, 7, 3, 6, 5, 6]
# 输出: 3
# 解释: 
# 索引3 (nums[3] = 6) 的左侧数之和(1 + 7 + 3 = 11)，与右侧数之和(5 + 6 = 11)相等。
# 同时, 3 也是第一个符合要求的中心索引。
# 
# 
# 示例 2:
# 
# 
# 输入: 
# nums = [1, 2, 3]
# 输出: -1
# 解释: 
# 数组中不存在满足此条件的中心索引。
# 
# 说明:
# 
# 
# nums 的长度范围为 [0, 10000]。
# 任何一个 nums[i] 将会是一个范围在 [-1000, 1000]的整数。
# 
# 
#

from typing import List

# @lc code=start
class Solution:
    
    def pivotIndex(self, nums: List[int]) -> int:
        count = len(nums)
        if count < 3:
            return -1

        # 如果存在下标i的左边元素累加之和 * 2 + 第i和元素 == 数组元素总和
        # 即可满足题目要求（这是我提交通过后才发现别人写的更优算法）
        s = sum(nums)
        left = 0
        for (i, n) in enumerate(nums):
            if left * 2 + nums[i] == s:
                return i
            left += n

        return -1

# @lc code=end

if __name__ == '__main__':
    s = Solution()
    assert s.pivotIndex([1,7,3,6,5,6]) == 3
    # 这条测试用例有误吧
    assert s.pivotIndex([-1,-1,-1,0,1,1]) == 0