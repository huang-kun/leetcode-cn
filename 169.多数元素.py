#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

from typing import List

# @lc code=start

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        pass
        
# @lc code=end

# 字典计数法：时间O(N)，空间O(N)
class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        total = len(nums)
        half = total / 2
        d = {}

        for n in nums:
            c = 1
            if n in d:
                c = d[n]
                c += 1
                if c > half:
                    return n
            d[n] = c

        return nums[0] if total > 0 else None

# 排序计数法：时间O(N*logN)，空间O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        total = len(nums)
        for i in range(total):
            if i > 0 and nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1

            if count > total / 2:
                return nums[i]


if __name__ == "__main__":
    s = Solution()
    assert s.majorityElement([1]) == 1
    assert s.majorityElement([3,2,3]) == 3
    assert s.majorityElement([2,2,1,1,1,2,2]) == 2