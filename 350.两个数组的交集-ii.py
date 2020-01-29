#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#
# https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (45.35%)
# Likes:    225
# Dislikes: 0
# Total Accepted:    62.9K
# Total Submissions: 136.5K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# 给定两个数组，编写一个函数来计算它们的交集。
# 
# 示例 1:
# 
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]
# 
# 
# 示例 2:
# 
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]
# 
# 说明：
# 
# 
# 输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
# 我们可以不考虑输出结果的顺序。
# 
# 
# 进阶:
# 
# 
# 如果给定的数组已经排好序呢？你将如何优化你的算法？
# 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
# 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
# 
# 
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 收集交集数字的集合
        s = set()
        # d1记录nums1中每个数字出现的次数，d2记录nums2中每个数字出现的次数
        d1, d2 = {}, {}
        # l1和l2分别是数组nums1和nums2的长度
        l1, l2 = len(nums1), len(nums2)
        
        # 同时遍历两个数组
        for i in range(max(l1, l2)):
            if i < l1:
                # 从nums1中获取一个数字
                n1 = nums1[i]
                # 如果nums1中的数字出现在d2中，说明是交集元素
                if n1 in d2:
                    s.add(n1)
                # 把该数字保存在d1中，并更新出现次数
                if n1 in d1:
                    d1[n1] += 1
                else:
                    d1[n1] = 1
            if i < l2:
                # 从nums2中获取一个数字
                n2 = nums2[i]
                # 如果nums2中的数字出现在d1中，说明是交集元素
                if n2 in d1:
                    s.add(n2)
                # 把该数字保存在d2中，并更新出现次数
                if n2 in d2:
                    d2[n2] += 1
                else:
                    d2[n2] = 1
        
        arr = []
        for n in s:
            # 题目中表示：每个元素出现的次数，应与元素在两个数组中出现的次数一致。
            # 那就取该元素分别在两个数组中出现次数的最小值。
            t = min(d1[n], d2[n])
            for i in range(t):
                arr.append(n)
        
        return arr
        
# @lc code=end

