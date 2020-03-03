#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:

        def isLeftHalf(a):
            return a == '(' or a == '{' or a == '['
        
        def isRightHalf(b):
            return b == ')' or b == '}' or b == ']'

        def isPair(a,b):
            return (a == '(' and b == ')') or \
                    (a == '{' and b == '}') or \
                    (a == '[' and b == ']')

        if len(s) == 0:
            return True
        if isRightHalf(s[0]):
            return False

        stack = []
        for c in s:
            if isLeftHalf(c):
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif isPair(stack[-1], c):
                stack.pop()
            else:
                return False
        
        return len(stack) == 0

# @lc code=end    

# 来自极客时间算法课
class Solution0:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', '}':'{', ']':'['}
        for c in s:
            if c not in pairs:
                stack.append(c)
            elif not stack and stack.pop() != pairs[c]:
                return False
        return not stack