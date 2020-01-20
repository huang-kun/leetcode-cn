#
# @lc app=leetcode.cn id=387 lang=python3
#
# [387] 字符串中的第一个唯一字符
#

# @lc code=start
class Solution:
    # 用字典保存每个字母的出现次数
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, c in enumerate(s):
            n = 0
            if c in d:
                i, n = d[c]
            n += 1
            d[c] = (i, n)
        
        minIdx = len(s)
        for k in d:
            i, n = d[k]
            if n == 1 and i < minIdx:
                minIdx = i
        
        return minIdx if minIdx < len(s) else -1
        
# @lc code=end

