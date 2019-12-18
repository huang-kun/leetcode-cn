#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

from typing import List

# @lc code=start
class Solution:

    # 双指针技巧二：快指针+慢指针
    # https://leetcode-cn.com/explore/learn/card/array-and-string/201/two-pointer-technique/786/
    
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k



# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.removeElement([3,2,2,3], 3) == 2
    assert s.removeElement([0,1,2,2,3,0,4,2], 2) == 5