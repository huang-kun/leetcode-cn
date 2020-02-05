#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start
class Solution:
    # 粗暴合并（先忽略题目中的时间复杂度）：合并两个数组，再计算中位数。
    #
    # 最开始想到的是把两个有序数组想像成两个栈，每次比较两个栈顶数字，让最大的出栈，加入到新数组里。
    # 虽然也能通过测试，但是后来发现，用两个指针移动操作的效率更高一些，于是就改成下面的版本。
    # 这两个指针移动也可以理解成：有两个队列，比较两个开头的数字，让最小的出队，加入到新数组。
    #
    # 时间复杂度O(m+n)，空间复杂度O(m+n)，其中m,n分别表示两个数组的长度。
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        i, j = 0, 0
        l1, l2 = len(nums1), len(nums2)
        while i < l1 or j < l2:
            n1 = nums1[i] if i < l1 else None
            n2 = nums2[j] if j < l2 else None
            # 比较两个数字，收集最小的
            if n1 is not None and n2 is not None:
                if n1 < n2:
                    nums.append(n1)
                    i += 1
                elif n1 > n2:
                    nums.append(n2)
                    j += 1
                else:
                    nums.append(n1)
                    nums.append(n2)
                    i += 1
                    j += 1
            elif n1 is not None:
                nums.append(n1)
                i += 1
            elif n2 is not None:
                nums.append(n2)
                j += 1
            else:
                break
        
        # 计算中位数
        if len(nums) == 0:
            return 0
        elif len(nums) % 2 == 0:
            mid = len(nums) // 2
            return (nums[mid] + nums[mid-1]) / 2
        else:
            mid = len(nums) // 2
            return nums[mid]
        
# @lc code=end

