#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 实现 strStr()
#

# @lc code=start
class Solution:
    # 让needle的第一个字符去匹配haystack中的每个字符，如果找到
    # 匹配，再继续匹配needle后续的字符是否与接下来的字符都相等。
    # PS: 提交测试的跑分为60ms（排名居然快垫底了～）
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        
        haylen = len(haystack)
        neelen = len(needle)
        
        for i in range(haylen):
            # 找到第一个匹配的字符
            if haystack[i] == needle[0]:
                # 继续尝试匹配剩余的needle字符
                match = True
                for j in range(1, neelen):
                    if i+j >= haylen:
                        return -1
                    if haystack[i+j] != needle[j]:
                        match = False
                        break
                if match:
                    return i
        return -1
        
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.strStr("mississippi", "pi") == 9
    assert s.strStr("mississippi", "issip") == 4