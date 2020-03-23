#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# 题解参考极客时间算法课
# 分治递归：每次对半分解任务，时间复杂度O(logN)
# 如果n是偶数，pow(x, n) = pow(x, n/2) * pow(x, n/2)
# 如果n是奇数，pow(x, n) = pow(x, n//2) * pow(x, n//2) * x

# @lc code=start
class Solution:

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n == 1:
            return x
        elif n == -1:
            return 1/x

        result = self.myPow(x, n//2)
        result *= result
        if n % 2 != 0:
            result *= x

        return result
# @lc code=end

# 摘录自极客时间算法课，分治迭代
class Solution2:

    def myPow(self, x: float, n: int) -> float:
        if n < 1:
            x = 1/x
            n = -n
        
        res = 1
        while n:
            if n & 1:       # n % 2 != 0
                res *= x
            x *= x
            n >>= 1         # n //= 2
        
        return res


if __name__ == "__main__":
    s = Solution2()
    assert s.myPow(2, 10) == 1024