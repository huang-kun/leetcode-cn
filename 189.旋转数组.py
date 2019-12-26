#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

from typing import List

# 为了减少时间复杂度，所以尽可能较少次数地遍历列表。
# 如果只遍历一次的话，就需要将每个元素直接旋转到最终位置，
# 下面为此给出了两个方法：抢位和让位。

# @lc code=start
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # 抢位算法：首先移动第一个元素到指定位置，将该位置的元素踢出去（抢了他的位置）
        #          被踢出的元素于是需要寻找自己的新位置，继续踢出别的元素
        # 空间复杂度O(1)，时间复杂度O(n)

        # 优化移动位置数
        length = len(nums)
        if k >= length:
            k %= length
        if k == 0:
            return None
        # 初始配置
        first_idx = 0
        p_idx = first_idx
        p_num = nums[p_idx]
        times = length
        while times > 1:
            # 找到抢占的目标位置
            i = p_idx
            i += k
            if i >= length:
                i -= length
            # 如果抢到了first_idx，本轮抢位结束，错位后继续
            if i == first_idx:
                nums[i] = p_num
                first_idx += 1
                p_idx = first_idx
                p_num = nums[p_idx]
            # 踢出元素，抢占位置
            else:
                temp = nums[i]
                nums[i] = p_num
                p_num = temp
                p_idx = i
            # 减少剩余次数
            times -= 1
        # 占据最后一个位置
        nums[first_idx] = p_num
        return None

# @lc code=end

    def rotate1(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 让位算法：首先出让一个位置，让其他元素来填补，
        #         填补后由于会空出新的位置，于是就循环填补
        # 空间复杂度O(1)，时间复杂度O(n)
        
        # 如果移动次数大于列表长度，可以简化移动次数
        length = len(nums)
        times = length
        if k >= length:
            k %= length
        if k == 0:
            return None

        # 先腾出列表首位数字作为空位置
        first_idx = 0
        p_idx = first_idx
        p_num = nums[p_idx]
        while times > 1:
            # 计算出旋转k次后应该放置在此空位置的数字的index
            i = p_idx
            i -= k
            if i < 0:
                i += length
            # 如果计算出的新位置正好等于最开始让出的位置
            # 本轮让位循环结束，错位后进行新一轮的让位循环
            if i == first_idx:
                nums[p_idx] = p_num
                first_idx += 1
                p_idx = first_idx
                p_num = nums[p_idx]
            # 无需错位情况下，将新数字填补到空位置
            # 填补后腾出该数字的旧位置
            else:
                nums[p_idx] = nums[i]
                p_idx = i
            # 减少移动次数
            times -= 1
        # 填补最后一个的空位置
        nums[p_idx] = p_num
        return None
        

if __name__ == "__main__":
    s = Solution()
    
    nums1 = [1,2,3,4,5,6,7]
    s.rotate(nums1, 3)
    assert nums1 == [5,6,7,1,2,3,4]

    nums2 = [1,2,3,4]
    s.rotate(nums2, 2)
    assert nums2 == [3,4,1,2]

    nums3 = [1,2,3,4,5,6]
    s.rotate(nums3, 3)
    assert nums3 == [4,5,6,1,2,3]
