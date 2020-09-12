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

class Solution2(object):
    def firstBadVersion(self, n):
        return self.lookup(1, n)

    def lookup(self, start, end):
        # 二分查找，判断中间值mid是否为badV
        # 如果mid是badV，说明firstBadV在[start, mid]里
        # 如果mid不是badV，说明firstBadV在[mid+1, end]里
        # 当start == end，说明找到firstBadV
        if start == end:
            return start
        
        mid = (start + end) // 2

        if isBadVersion(mid):
            return self.lookup(start, mid)
        else:
            return self.lookup(mid+1, end)


class Solution:
    
    # 根据官方题解的优化版本：
    # https://leetcode-cn.com/problems/first-bad-version/solution/di-yi-ge-cuo-wu-de-ban-ben-by-leetcode/
    
    def firstBadVersion(self, n):
        start, end = 1, n
        while start < end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                # 如果mid是错误版本，那么mid之后的版本不可能是第一个错误版本
                # 所以将end调整到mid位置，这样end有可能成为第一个错误版本
                end = mid
            else:
                # 如果mid是正确版本，那么mid之前的都是正确版本，所以可以将
                # start调整到mid+1，这样start有可能成为第一个错误版本
                start = mid + 1
        # 当start == end时候，即找到第一个错误版本，结束循环
        return start

# @lc code=end

    # 变相的二分查找
    def firstBadVersion1(self, n):
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
        

def isBadVersion(version):
    pass