#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

from typing import List

# @lc code=start
class Solution:
    
    def plusOne(self, digits: List[int]) -> List[int]:
        """该题目可以通过将整数到位数的分解与合成，来实现整数与列表之间的转换"""

        # 首先快速返回一批可以直接在个位数加一的列表
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        
        # 正常情况下，需要将列表还原成为整数本身
        number = 0
        length = len(digits)
        for (index, digit) in enumerate(digits):
            number += 10 ** (length - index - 1) * digit

        # 然后给还原后的整数加一
        number += 1
        
        # 最后将整数转换成列表，返回结果
        digits1 = []
        while number > 0:
            digit = number % 10
            digits1.insert(0, digit)
            number //= 10

        return digits1

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.plusOne([1,2,3]) == [1,2,4]
    assert s.plusOne([4,3,2,1]) == [4,3,2,2]
    assert s.plusOne([9]) == [1,0]