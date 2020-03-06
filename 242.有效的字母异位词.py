#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        pass
# @lc code=end

# ------------------------------------------------
# 方法1：字典计数
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        def store(d, c):
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        d1, d2 = {}, {}
        for i in range(len(s)):
            store(d1, s[i])
            store(d2, t[i])
        
        return d1 == d2

# ------------------------------------------------
# 方法2：字符串排序
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) == sorted(t)

# ------------------------------------------------
# 方法3：字典计数（极客时间版）
class Solution3:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d1, d2 = {}, {}
        for i in range(len(s)):
            d1[s[i]] = d1.get(s[i], 0) + 1
            d2[t[i]] = d2.get(t[i], 0) + 1
        
        return d1 == d2
    
    def isAnagram2(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # 由于小写字母只有26个，所以可以将a~z映射成数字0~25
        # 类似于字典的Hash实现
        d1, d2 = [0]*26, [0]*26
        for i in range(len(s)):
            n1 = ord(s[i]) - ord('a')
            n2 = ord(t[i]) - ord('a')
            d1[n1] += 1
            d2[n2] += 1
        
        return d1 == d2