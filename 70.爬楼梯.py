#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# 官方题解
# https://leetcode-cn.com/problems/climbing-stairs/solution/pa-lou-ti-by-leetcode/

# @lc code=start
class Solution:

    def climbStairs(self, n: int) -> int:
        return self.flatFib2(n)

    # 根据官方题解，实现空间复杂度为0(1)的斐波那契数列
    def flatFib2(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        first = 1
        second = 2
        
        for i in range(3, n+1):
            third = first + second
            first = second
            second = third
            
        return third

# @lc code=end

    # 根据官方题解，使用动态规划的实现。其实也是用遍历而
    # 非递归的方式实现的“扁平化版本”的斐波那契数列。
    def flatFib(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        arr = [0] * (n + 1)
        arr[1] = 1
        arr[2] = 2
        
        for i in range(3, n+1):
            arr[i] = arr[i-1] + arr[i-2]
            
        return arr[n]


    # 根据官方题解，可以将问题转换成斐波那契数列，f(n) = f(n-1) + f(n-2)
    # 这里需要字典来保存每次f(n)的结果，减少时间复杂度。
    def __init__(self):
        self.memo = {}

    def fibonacci(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        if n in self.memo:
            return self.memo[n]
        
        self.memo[n] = self.fibonacci(n - 1) + self.fibonacci(n - 2)
        return self.memo[n]
        

if __name__ == "__main__":
    pass