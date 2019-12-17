#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# 实现之前参考了stackoverflow
# https://stackoverflow.com/questions/21420447/need-help-in-adding-binary-numbers-in-python

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 把长度不足的字符串用0从左边填满
        max_len = max(len(a), len(b))
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        s = ""
        t = 0 # 进位

        for i in reversed(range(max_len)):
            # 数字相加，包括加上进位值
            d = int(a[i]) + int(b[i]) + t
            # 修改进位
            t = 1 if d >= 2 else 0
            # 累计结果
            s = str(d % 2) + s

        # 如果还有进位，给结果再加上进位
        if t == 1:
            s = "1" + s
        
        return s
        
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.addBinary("11", "1") == "100"
    assert s.addBinary("1010", "1011") == "10101"
    assert s.addBinary("1111", "1111") == "11110"