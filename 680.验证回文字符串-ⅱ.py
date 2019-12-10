#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:

    def validPalindrome(self, s: str) -> bool:
        return self._validPalindrome(s, 0, len(s)-1, True)

    def _validPalindrome(self, s, i, j, skip):
        # 双指针
        if i < 0 or j >= len(s):
            return False
        while i < j:
            a, b = s[i], s[j]
            if a != b:
                if skip:
                    skip = False
                    # 双指针技巧下，由于事先并不清楚从哪一端删除一个字母能够成功，
                    # 比如abccbab，所以需要先选一端进行尝试，失败了再选择另一端
                    return self._validPalindrome(s, i+1, j, False) or \
                            self._validPalindrome(s, i, j-1, False)
                return False
            i += 1
            j -= 1
        return True
        
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.validPalindrome("aba") == True
    assert s.validPalindrome("abca") == True
    assert s.validPalindrome("abc") == False
    assert s.validPalindrome("deeee") == True
    assert s.validPalindrome("eeeec") == True
    assert s.validPalindrome("abccbab") == True
