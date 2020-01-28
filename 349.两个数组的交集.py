#
# @lc app=leetcode.cn id=349 lang=python3
#
# [349] 两个数组的交集
#
# https://leetcode-cn.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (67.17%)
# Likes:    155
# Dislikes: 0
# Total Accepted:    47.7K
# Total Submissions: 70.5K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# 给定两个数组，编写一个函数来计算它们的交集。
# 
# 示例 1:
# 
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2]
# 
# 
# 示例 2:
# 
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [9,4]
# 
# 说明:
# 
# 
# 输出结果中的每个元素一定是唯一的。
# 我们可以不考虑输出结果的顺序。
# 
# 
#

# @lc code=start
class Solution:

    # 三个集合：一个用来收集答案，其他两个分别保存各自数组的元素。
    # 时间复杂度O(max(m,n))，空间复杂度O(m+n)，用空间换时间。
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set0, set1, set2 = set(), set(), set()
        l1, l2 = len(nums1), len(nums2)
        for i in range(max(l1, l2)):
            if i < l1:
                # 在列表1中取到当前数字
                n1 = nums1[i]
                # 保存在集合1中
                set1.add(n1)
                # 如果该数字出现在集合2中，说明是交集
                if n1 in set2:
                    set0.add(n1)
            if i < l2:
                # 在列表2中取到当前数字
                n2 = nums2[i]
                # 保存在集合2中
                set2.add(n2)
                # 如果该数字出现在集合1中，说明是交集
                if n2 in set1:
                    set0.add(n2)
        return list(set0)
        
# @lc code=end
    
    # 粗暴遍历：时间复杂度是O(m*n)，m和n分别表示两个数组长度。
    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr = []
        for i in nums1:
            if i in nums2:
                if i not in arr:
                    arr.append(i)
        return arr

