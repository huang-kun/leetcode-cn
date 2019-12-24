#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

from typing import List

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        start = 0
        for (i2, n2) in enumerate(nums2):
            # 插入排序：将新数字插入到有序列表num1的合适位置中
            # 由于num2也是有序列表，就可以从num1上次插入的位置向后查找新位置
            end = m + i2
            inserted = False
            for i in range(start, end):
                if nums1[i] > n2:
                    # 如果找到了合适的位置，就需要将nums1从该
                    # 位置起把元素依次向后移动，以便腾出空位置
                    for j in range(end, i, -1):
                        nums1[j] = nums1[j-1]
                    # 然后在空位置这里插入元素
                    nums1[i] = n2
                    # 更新下次查找的起始位置
                    start = i
                    inserted = True
                    break
            if not inserted:
                nums1[end] = n2
                start = end
        return None

# @lc code=end

    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for (i2, n2) in enumerate(nums2):
            # 把nums2的元素插入到nums1的末尾（第一个空余0的位置）
            i = m + i2
            nums1[i] = n2
            # 冒泡排序nums1
            while i >= 1 and nums1[i] < nums1[i-1]:
                temp = nums1[i-1]
                nums1[i-1] = nums1[i]
                nums1[i] = temp
                i -= 1
        return None

if __name__ == "__main__":
    s = Solution()

    nums1 = [1,2,3,0,0,0]; m = 3
    nums2 = [2,5,6];       n = 3
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1,2,2,3,5,6]

    nums1 = [2,0]; m = 1
    nums2 = [1];   n = 1
    s.merge(nums1, m, nums2, n)
    assert nums1 == [1,2]