#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:

    # 根据官方题解，可以将问题转换成斐波那契数列，f(n) = f(n-1) + f(n-2)
    # 这里需要字典来保存每次f(n)的结果，减少时间复杂度。
    def __init__(self):
        self.memo = {}
    
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        if n in self.memo:
            return self.memo[n]
        
        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]
        
# @lc code=end

