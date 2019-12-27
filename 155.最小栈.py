#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    # 单纯从算法的角度考虑的话，可以在每次入栈时比较和保留最小值，
    # 而在出栈后，只有在删除了最小值的情况下，才需要重新计算剩余元素的最小值。
    # 最坏的情况下，每次入栈的数字都是越来越小，那么每次出栈的时间复杂度为O(n)

    def __init__(self):
        self.list = []
        self.min = None

    def push(self, x: int) -> None:
        self.list.append(x)
        self.min = min(self.min, x) if self.min is not None else x

    def pop(self) -> None:
        x = self.list.pop()
        if x == self.min:
            self.min = None
            for n in self.list:
                self.min = min(self.min, n) if self.min is not None else n

    def top(self) -> int:
        return self.list[-1]

    def getMin(self) -> int:
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

