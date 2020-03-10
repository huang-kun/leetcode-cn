#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

from typing import List

# @lc code=start

# 参考题解：排序+双指针jk
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        pass
        
# @lc code=end

# ---------------------------------------------------------
# 方法1：三重循环暴力法
class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = len(nums)
        array = []
        for i in range(count-2):
            for j in range(i+1, count-1):
                for k in range(j+1, count):
                    if nums[i] + nums[j] + nums[k] == 0:
                        subarr = [nums[i], nums[j], nums[k]]
                        subarr.sort()
                        array.append(subarr)
        return array

# ---------------------------------------------------------
# 方法2（参考精选题解）：排序 + 双指针，感觉人家把算法优化到极致了～
# https://leetcode-cn.com/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
class Solution2:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        # 数组个数小于3，返回空
        if n < 3:
            return res
        # 数组排序
        nums.sort()
        # 排序后，如果最小值大于0，说明无解
        if nums[0] > 0:
            return res

        for i in range(n):
            # 当遍历到数字大于0，再往后收集就重复了。
            if nums[i] > 0:
                return res
            # 跳过重复值
            if i != 0 and nums[i] == nums[i-1]:
                continue
            # 初始化左右指针
            L = i + 1
            R = n - 1
            while L < R:
                # 如果3数之和大于0，调整R
                if nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
                # 如果3数之和小于0，调整L
                elif nums[i] + nums[L] + nums[R] < 0:
                    L += 1
                # 3数之和等于0，收集结果，同时调整LR（跳过重复值）
                else:
                    res.append([nums[i], nums[L], nums[R]])
                    while L < R and nums[L] == nums[L+1]:
                        L += 1
                    while R > L and nums[R] == nums[R-1]:
                        R -= 1
                    L += 1
                    R -= 1

        return res

# ---------------------------------------------------------
# 测试
if __name__ == "__main__":
    s = Solution()
    assert s.threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
    assert s.threeSum([1,2,-2,-1]) == []

