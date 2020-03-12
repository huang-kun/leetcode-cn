#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#

# 解题思路可以参考[15]三数之和，下面的链接是三数之和的精选题解：
# https://leetcode-cn.com/problems/3sum/solution/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
#
# 按照上述题解的基本思路不变，需要对优化部分做些改动：
# 比如对排序后的数组，在每一轮外层遍历开始时，先计算出最小和与最大和
# 如果最小和都大于target，说明之后的遍历中，无论任意组合都不可能等于target，直接可以结束遍历
# 如果最大和都小于target，说明当次的外层遍历中，无论任意组合都不可能等于target，但是下一轮外层遍历依然有机会

from typing import List

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        if n < 4:
            return res
        
        # 排序
        nums.sort()

        if target > 0 and nums[0] > target:
            return res
        
        # 外层循环
        for i in range(n-3):
            # 跳过重复数字
            if i != 0 and nums[i] == nums[i-1]:
                continue
            # 最小和
            min1 = nums[i] + nums[i+1] + nums[i+2] + nums[i+3]
            if min1 > target:
                break
            # 最大和
            max1 = nums[i] + nums[n-3] + nums[n-2] + nums[n-1]
            if max1 < target:
                continue
            
            # 内层循环
            for j in range(i+1,n-2):
                # 跳过重复数字
                if j-1 != i and nums[j] == nums[j-1]:
                    continue
                # 最小和
                min2 = nums[i] + nums[j] + nums[j+1] + nums[i+2]
                if min2 > target:
                    break
                # 最大和
                max2 = nums[i] + nums[j] + nums[n-2] + nums[n-1]
                if max2 < target:
                    continue
                
                # 双指针
                L = j + 1
                R = n - 1
                while L < R:
                    # 缩小最大范围
                    if nums[i] + nums[j] + nums[L] + nums[R] > target:
                        R -= 1
                    # 增加最小范围
                    elif nums[i] + nums[j] + nums[L] + nums[R] < target:
                        L += 1
                    else:
                        # 收集结果
                        res.append([nums[i], nums[j], nums[L], nums[R]])
                        # 缩小范围，并且跳过重复数字
                        while L < R and nums[L] == nums[L+1]:
                            L += 1
                        while R < L and nums[R] == nums[R-1]:
                            R -= 1
                        L += 1
                        R -= 1
            
        return res
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.fourSum([1,0,-1,0,-2,2], 0) == [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    assert s.fourSum([0,0,0,0], 0) == [[0,0,0,0]]
    assert s.fourSum([-1,0,1,2,-1,-4], -1) == [[-4,0,1,2],[-1,-1,0,1]]
    assert s.fourSum([1,-2,-5,-4,-3,3,3,5], -11) == [[-5,-4,-3,1]]