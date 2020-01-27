#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def __init__(self):
        minInt = -2 ** 31
        maxInt = (minInt + 1) * (-1)
        bound = maxInt // 10
        digit = maxInt % 10
        self.minInt = minInt
        self.maxInt = maxInt
        self.maxIntStrLength = len(str(maxInt))
        self.posBound = bound
        self.negBound = bound * (-1)
        self.posDigit = digit
        self.negDigit = (digit + 1) * (-1)
    
    # 在理解了官方题解的基础上，使用字符串来做反转
    def reverse(self, x: int) -> int:
        num = abs(x)
        s = str(num)
        
        # 如果原整数的字符串长度与最大整数字符串长度相同，需要提前避免反转后的结果溢出
        if len(s) == self.maxIntStrLength:
            rev = 0
            for i in range(len(s)-1, -1, -1):
                digit = int(s[i])
                if x < 0:
                    digit *= -1
                    
                # 事先判断rev是否将要溢出
                if rev > self.posBound or (rev == self.posBound and digit > self.posDigit):
                    return 0
                elif rev < self.negBound or (rev == self.negBound and digit < self.negDigit):
                    return 0
                    
                # 安全赋值
                rev = rev * 10 + digit
                
            return rev
        
        # 反转字符串
        # 由于Python的str是不可变对象，允许下标读取（比如s[0]）但是不能给下标赋值（比如s[0] = '1'）
        # 所以不能用双指针(i,j)从头尾开始交换字符的方式了，比如s[i], s[j] = s[j], s[i]
        rs = s[::-1]
        
        if x >= 0:
            return int(rs)
        else:
            return int(rs) * (-1)

# @lc code=end

    # 之前自己刷了3次，结果还是输给了官方题解：
    # 1. 不使用堆栈和数组的前提下，进行数字反转
    # 2. 对于反转后的数字计算过程中，需要时刻防止溢出
    # https://leetcode-cn.com/problems/reverse-integer/solution/zheng-shu-fan-zhuan-by-leetcode/
    def reverse1(self, x: int) -> int:
        # python在取余数和整除运算中，会因为向下取整的规则
        # 导致结果跟预期不一致，因此下面出现的所有取余数和
        # 整除的运算，都按正整数来计算
        
        # 反转后整数的安全范围[-2147483648, 2147483647]
        INT_MIN = -2 ** 31
        INT_MAX = -1 * (INT_MIN + 1)
        
        UPPER_THRESHOLD = INT_MAX // 10
        LOWER_THRESHOLD = UPPER_THRESHOLD * (-1)
        
        num = abs(x)
        rev = 0

        while num > 0:
            pop = num % 10
            num //= 10

            if x < 0:
                pop *= -1

            # 事先判断整数rev是否将要溢出
            if rev > UPPER_THRESHOLD:
                return 0
            elif rev == UPPER_THRESHOLD and pop > 7:
                return 0
            elif rev < LOWER_THRESHOLD:
                return 0
            elif rev == LOWER_THRESHOLD and pop < -8:
                return 0
            # 安全赋值
            rev = rev * 10 + pop
        
        return rev
    

if __name__ == "__main__":
    s = Solution()
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(120) == 21
    assert s.reverse(1534236469) == 0
    assert s.reverse(1563847412) == 0
    assert s.reverse(-1563847412) == 0
