#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x
        while low <= high:
            mid = low + (high - low) / 2
            # 如果出现小数位，并且low和high的整数位都相同，说明可以返回了
            if mid // 1 != mid and low // 1 == high // 1:
                return int(mid)
            sq = mid * mid
            if sq > x:
                high = mid
            elif sq < x:
                low = mid
            else:
                return int(mid)

# @lc code=end

