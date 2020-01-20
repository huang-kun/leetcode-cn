#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

from typing import List

# @lc code=start
class Solution:

    # 第二次刷题，思路依旧是整数与数组转换
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        if l == 0:
            return []
        # 如果个位数小于9，加一后可以快速返回
        last_digit = digits[-1]
        if last_digit < 9:
            last_digit += 1
            digits[-1] = last_digit
            return digits
        # 将数组转换成整数
        num = 0
        allNines = True
        for i in range(l):
            digit = digits[i]
            num += digit * (10 ** (l - i - 1))
            if digit != 9:
                allNines = False
        # 整数加一
        num += 1
        # 如果每个数位都是9，就增加数位长度
        if allNines:
            l += 1
        # 再将整数转换为数组
        digitsPlus = []
        for i in range(l):
            digit = num // (10 ** (l - i - 1))
            digitsPlus.append(digit)
            num %= (10 ** (l - i - 1))
        
        return digitsPlus

    
# @lc code=end

    def plusOne1(self, digits: List[int]) -> List[int]:
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