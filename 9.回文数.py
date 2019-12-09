#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:

    def isPalindrome(self, x):
        """该题目要求：不能将整数转换为字符串来解决问题"""
        
        if x < 0:
            return False
        if x < 10:
            return True

        # 将整数分解成由数字组成的倒叙列表
        n = x
        numbers = []
        while n >= 10:
            m = n % 10
            numbers.append(m)
            n //= 10
        numbers.append(n)

        # 使用双指针技巧
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] != numbers[j]:
                return False
            i += 1
            j -= 1

        return True
        
        
# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome(121) == True
    assert s.isPalindrome(-121) == False
    assert s.isPalindrome(10) == False
