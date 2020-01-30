#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#
# https://leetcode-cn.com/problems/string-to-integer-atoi/description/
#
# algorithms
# Medium (18.62%)
# Likes:    530
# Dislikes: 0
# Total Accepted:    102.7K
# Total Submissions: 543K
# Testcase Example:  '"42"'
#
# 请你来实现一个 atoi 函数，使其能将字符串转换成整数。
# 
# 首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。
# 
# 
# 当我们寻找到的第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字组合起来，作为该整数的正负号；假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。
# 
# 该字符串除了有效的整数部分之后也可能会存在多余的字符，这些字符可以被忽略，它们对于函数不应该造成影响。
# 
# 注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。
# 
# 在任何情况下，若函数不能进行有效的转换时，请返回 0。
# 
# 说明：
# 
# 假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为 [−2^31,  2^31 − 1]。如果数值超过这个范围，请返回  INT_MAX
# (2^31 − 1) 或 INT_MIN (−2^31) 。
# 
# 示例 1:
# 
# 输入: "42"
# 输出: 42
# 
# 
# 示例 2:
# 
# 输入: "   -42"
# 输出: -42
# 解释: 第一个非空白字符为 '-', 它是一个负号。
# 我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
# 
# 
# 示例 3:
# 
# 输入: "4193 with words"
# 输出: 4193
# 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
# 
# 
# 示例 4:
# 
# 输入: "words and 987"
# 输出: 0
# 解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
# ⁠    因此无法执行有效的转换。
# 
# 示例 5:
# 
# 输入: "-91283472332"
# 输出: -2147483648
# 解释: 数字 "-91283472332" 超过 32 位有符号整数范围。 
# 因此返回 INT_MIN (−2^31) 。
# 
# 
#

# @lc code=start
class Solution:
    
    def __init__(self):
        # 设置整数的最大和最小值，以及预防溢出的边界。边界的设置可以参考 -- 7.整数反转 -- 的官方题解：
        # https://leetcode-cn.com/problems/reverse-integer/solution/zheng-shu-fan-zhuan-by-leetcode/
        minInt = -2 ** 31
        maxInt = (minInt + 1) * (-1)
        bound = maxInt // 10
        digit = maxInt % 10
        self.minInt = minInt
        self.maxInt = maxInt
        self.posBound = bound
        self.negBound = bound * (-1)
        self.posDigit = digit
        self.negDigit = (digit + 1) * (-1)
        
        # 获取0～9的数字字符，方便字符的快速匹配
        self.digits = {}
        for i in range(10):
            self.digits[str(i)] = i
        
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        number = 0
        is_neg = False
        space_head = False
        index_after_space = 0

        for index in range(0, len(s)):
            char = s[index]

            # 跳过字符串左侧的空白
            if index == 0 and char.isspace():
                space_head = True
            if char.isspace() and space_head:
                index_after_space += 1
                continue
            else:
                space_head = False

            # 判断正负号
            if char == '+' and index == index_after_space:
                continue
            if char == '-' and index == index_after_space:
                is_neg = True
                continue
            
            # 如果出现非数字字符，结束
            if char not in self.digits:
                break
                
            # 将字符转换为整数数字（开头是0也没有关系）
            digit = self.digits[char]
            if is_neg:
                digit *= -1
            
            # 事先判断number是否将要溢出
            if number > self.posBound or (number == self.posBound and digit > self.posDigit):
                return self.maxInt
            elif number < self.negBound or (number == self.negBound and digit < self.negDigit):
                return self.minInt
            
            # 安全赋值
            number = number * 10 + digit
        
        return number
        
# @lc code=end

if __name__ == '__main__':
    s = Solution()
    assert s.myAtoi('42') == 42
    assert s.myAtoi('4193 with words') == 4193
    assert s.myAtoi('words and 987') == 0
    assert s.myAtoi('-91283472332') == -2147483648
    assert s.myAtoi('-2147483649') == -2147483648
    assert s.myAtoi('-2147483648') == -2147483648
    assert s.myAtoi('-2147483647') == -2147483647
    assert s.myAtoi('91283472332') == 2147483647
    assert s.myAtoi('2147483646') == 2147483646
    assert s.myAtoi('2147483647') == 2147483647
    assert s.myAtoi('2147483648') == 2147483647
    assert s.myAtoi('0123') == 123
    assert s.myAtoi('00001023') == 1023
    assert s.myAtoi('   -42') == -42
    assert s.myAtoi('   --42') == 0
    assert s.myAtoi('   - 42') == 0
    assert s.myAtoi('   -4-2') == -4
    assert s.myAtoi('-4-2') == -4
    assert s.myAtoi('-04-2') == -4
    assert s.myAtoi('+42') == 42
    assert s.myAtoi(' +42') == 42
    assert s.myAtoi(' + 42') == 0
    assert s.myAtoi(' +4 2 ') == 4
    assert s.myAtoi('+-42') == 0
    assert s.myAtoi('++42') == 0
    assert s.myAtoi('-+42') == 0
    assert s.myAtoi(' 4 2 ') == 4
    assert s.myAtoi('  42  ') == 42
    assert s.myAtoi('  042  ') == 42
    assert s.myAtoi('  004020  ') == 4020
    assert s.myAtoi(' 0 42 0  ') == 0
    assert s.myAtoi('    ') == 0
    assert s.myAtoi('') == 0

