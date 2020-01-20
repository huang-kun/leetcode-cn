#
# @lc app=leetcode.cn id=278 lang=python3
#
# [278] 第一个错误的版本
#

# @lc code=start
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    # 变相的二分查找
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n
        mid = -1
        fbv = n
        
        while start <= end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                fbv = min(fbv, mid)
                end = mid - 1
            else:
                start = mid + 1
        
        return fbv
        
# @lc code=end

