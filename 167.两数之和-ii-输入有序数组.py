#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:

    # 参考的双指针技巧
    def twoSum(self, numbers, target):
        i = 0
        j = len(numbers) - 1

        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i+1, j+1]

        return []

# @lc code=end

if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert s.twoSum([1,2,3,4,5,6,7,8,9], 15) == [6,9]