#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

from typing import List

# @lc code=start
class Solution:
    # 参考了官方题解后的实现（48ms）
    def moveZeroes(self, nums: List[int]) -> None:
        # 将找到的非0数字需要被安置的下标位置
        k = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                # 交换下标i,k的数字
                nums[i], nums[k] = nums[k], nums[i]
                k += 1
                
# @lc code=end

    # 该实现虽然能够通过测试，但是离最优解仍有差距（404ms）
    def moveZeroes1(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return None

        # head指针用来找0
        head = 0
        # tail指针用来指定放置0的位置
        tail = len(nums) - 1
        
        while head < tail:
            # 如果找到0
            if nums[head] == 0:
                # 就将后面的数字依次向前移动一个位置
                for i in range(head, tail):
                    nums[i] = nums[i + 1]
                # 再将0插入tail的位置
                nums[tail] = 0
                tail -= 1
            else:
                head += 1

if __name__ == "__main__":
    s = Solution()

    nums = [0,1,0,3,12]
    s.moveZeroes(nums)
    assert nums == [1,3,12,0,0]

    nums = [0,0,1]
    s.moveZeroes(nums)
    assert nums == [1,0,0]
