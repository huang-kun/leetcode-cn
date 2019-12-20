#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] 只出现一次的数字
#

from typing import List

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = len(nums)
        for i in range(0, count, 2):
            if i + 1 < count and nums[i] != nums[i + 1]:
                return nums[i]
        
        return nums[count - 1]

    # 这我绝对想不到：位操作，将所有的数进行 XOR 操作，得到那个唯一的数字。时间复杂度O(n)，空间复杂度O(1)
    # https://leetcode-cn.com/problems/single-number/solution/zhi-chu-xian-yi-ci-de-shu-zi-by-leetcode/
    def singleNumber2(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    s.singleNumber([2,2,1]) == 1
    s.singleNumber([4,1,2,1,2]) == 4