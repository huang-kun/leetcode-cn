#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:

    def reverse(self, x):
        number = abs(x)
        re_num = 0

        # 获取该整数的位数
        place = len(str(number))

        # 在python版本的do while循环中进行以下操作：
        # 1. 从个位数开始获取当前数位上的数字
        # 2. 计算出将其反转到高位后的数字，并加入到结果中
        # 3. 更新剩余数字和数位
        while True:
            digit = number % 10
            re_num += digit * (10 ** (place - 1))
            number //= 10
            place -= 1
            if place == 0:
                break
        
        if x < 0:
            re_num *= -1

        limit = 2 ** 31
        if re_num < -limit or re_num > limit - 1:
            return 0

        return re_num
        
# @lc code=end

    def reverse1(self, x: int) -> int:
        """
        在完成了该方法的实现以后，我想到其实可以去除digits列表的部分，
        直接从整数分解到每个数位上的数字时也许可以直接转换到结果上面，
        省去了列表的遍历。该方法保留了最初实现整数反转的思路。
        """
        
        n = abs(x)

        # 首先将整数分解成由数字组成的倒叙列表
        digits = []
        while n >= 10:
            m = n % 10
            digits.append(m)
            n //= 10
        digits.append(n)
        
        # 再将列表中的数字结合成整数
        r = 0
        count = len(digits)
        for (i, n) in enumerate(digits):
            r += n * pow(10, count-i-1)

        # 题目限制：只接受32位的有符号整数
        if r > pow(2, 31) - 1:
            return 0

        return r if x > 0 else -r

if __name__ == "__main__":
    s = Solution()
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(120) == 21
    assert s.reverse(1534236469) == 0
    assert s.reverse(1563847412) == 0
