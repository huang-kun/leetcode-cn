#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:

    def isPalindrome(self, s: str) -> bool:
        # 双指针技巧
        i, j = 0, len(s) - 1
        while i < j:
            a, b = s[i], s[j]
            if not a.isalnum():
                i += 1
                continue
            elif not b.isalnum():
                j -= 1
                continue
            elif a.lower() != b.lower():
                return False
            
            i += 1
            j -= 1
        
        return True

        
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome("A man, a plan, a canal: Panama") == True
    assert s.isPalindrome("race a car") == False
