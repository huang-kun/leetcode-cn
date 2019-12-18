#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# 双指针技巧二：快指针+慢指针
# https://leetcode-cn.com/explore/learn/card/array-and-string/201/two-pointer-technique/786/    

from typing import List

# @lc code=start
class Solution:

    # 双指针技巧：快指针+慢指针
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i = 0 # 快指针
        k = 0 # 慢指针
        length = len(nums) # 最小的子列表长度
        summary = nums[0] if length > 0 else 0 # 求和
        last_index = length - 1
        temp = None

        while i < last_index:
            # 如果指针重合且求和的值符合条件，结束（特例）
            if i == k and summary >= s:
                return 1
            # 移动快指针
            while summary < s and i < last_index:
                i += 1
                summary += nums[i]
            # 移动慢指针
            while summary >= s and k < i:
                temp = summary
                summary -= nums[k]
                k += 1
            # 计算最小长度
            le = i-k+1 if temp is None else i-k+2
            length = min(length, le)
        
        summary = summary if temp is None else temp
        return length if summary >= s else 0

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.minSubArrayLen(7, [2,3,1,2,4,3]) == 2
    assert s.minSubArrayLen(15, [1,2,3,4,5]) == 5
    assert s.minSubArrayLen(11, [1,2,3,4,5]) == 3
    assert s.minSubArrayLen(1, []) == 0
    assert s.minSubArrayLen(4, [1,4,4]) == 1
    assert s.minSubArrayLen(3, [3]) == 1
    assert s.minSubArrayLen(5, [1,2]) == 0
    assert s.minSubArrayLen(6, [10,2,3]) == 1
