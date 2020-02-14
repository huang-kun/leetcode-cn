#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    
    # 二分查找
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        
        start = 0
        end = len(nums) - 1

        if target > nums[end]:
            return len(nums)

        while start < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid
            else:
                return mid

        return start

# @lc code=end

class Solution1:
    # 迭代法
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if target <= n:
                return i
                
        return len(nums)
