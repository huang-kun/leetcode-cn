#
# @lc app=leetcode.cn id=239 lang=python3
#
# [239] 滑动窗口最大值
#

from typing import List

# ------------------------------------------------------------------
# 方法一：向右移动元素数量为k的子数组（暴力法）
class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maximums = []
        for i in range(len(nums)-k+1):
            subnums = nums[i:i+k]
            if len(subnums):
                maximums.append(max(subnums))
        
        return maximums

# ------------------------------------------------------------------
# 方法二：始终维护一个只有k个元素的最大堆/大顶堆
# 因为解题时涉及到需要在堆中进行元素查找，所以效率也不高
def maxHeapAdjust(heap, index):
    # perc up
    i = index
    while i > 0 and (i - 1) // 2 >= 0:
        p = (i - 1) // 2
        if heap[i] > heap[p]:
            heap[i], heap[p] = heap[p], heap[i]
            i = p
        else:
            break
    # perc down
    i = index
    while 2 * i + 1 < len(heap):
        left = 2 * i + 1
        right = 2 * i + 2
        maxChild = left
        if right < len(heap) and heap[right] > heap[left]:
            maxChild = right
        if heap[i] < heap[maxChild]:
            heap[i], heap[maxChild] = heap[maxChild], heap[i]
            i = maxChild
        else:
            break

def maxHeapPush(heap, item):
    heap.append(item)
    maxHeapAdjust(heap, len(heap)-1)

# 由于维护堆的时候，需要删除某个指定数字，所以查找很慢
def maxHeapReplace(heap, old, new):
    for i in range(len(heap)):
        if heap[i] == old:
            heap[i] = new
            maxHeapAdjust(heap, i)
            break

class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        maximums = []
        for i in range(len(nums)):
            if len(heap) < k:
                maxHeapPush(heap, nums[i])
                if len(heap) == k:
                    maximums.append(heap[0])
            else:
                maxHeapReplace(heap, nums[i-k], nums[i])
                maximums.append(heap[0])
        
        return maximums

# ------------------------------------------------------------------
# 方法三：维护一个最多有k个元素的双端队列，并且保持队列中的头部元素始终最大
# 
# 至于为什么要使用“双端队列”而非普通队列？以下摘自leetcode官方解释：
#
# 双端队列和普通队列最大的不同在于，它允许我们在队列的头尾两端都能在 
# O(1)的时间内进行数据的查看、添加和删除。
#
# 与队列相似，我们可以利用一个双链表实现双端队列。双端队列最常用的地方
# 就是实现一个长度动态变化的窗口或者连续区间，而动态窗口这种数据结构在
# 很多题目里都有运用。
#
# 链接：https://leetcode-cn.com/problems/sliding-window-maximum/solution/shi-pin-jie-xi-shuang-duan-dui-lie-hua-dong-chuang/

from collections import deque

class Solution3:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxs = []
        dq = deque()

        for i in range(len(nums)):
            # 依次入队
            dq.append(nums[i])
            # 当队列元素数量大于k
            if len(dq) > k:
                # 保持最多k个元素
                dq.popleft()
                # 由于最大的元素被出队了，所以重新
                # 找出最大元素，并将其放在队列首位
                m = max(dq)
                while dq[0] != m:
                    dq.popleft()
            else:
                # 队列元素没有超过k时，始终保持首位元素最大
                while dq[-1] > dq[0]:
                    dq.popleft()
            
            if i >= k - 1:
                maxs.append(dq[0])
        
        return maxs

# ------------------------------------------------------------------
# 方法四：同理方法三，只是用数组来实现一个普通队列，并且能够快速通过下标访问元素
# 因为方法三中的双端队列，除了使用到下标特性以外，也只作为普通队列来使用，所以完
# 全可以换成一个数组来解题。
class Solution4:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 搜索队列中最大值的index
        def findMax(queue, start):
            max_index = start
            for i in range(start, len(queue)):
                if queue[i] > queue[max_index]:
                    max_index = i
            return max_index

        maxs = []
        # 用数组来实现队列
        queue = []
        # 队列头部指针
        head = -1

        for i in range(len(nums)):
            # 入队
            queue.append(nums[i])
            if head == -1:
                head = 0
            # 如果队列中的元素大于k
            if len(queue) - head > k:
                # 出队一个元素
                head += 1
                # 重新调整队列，让最大值左边的数字全部出队
                head = findMax(queue, head)
            else:
                # 始终维护队列中的头部为最大值：让新入队的元素
                # 跟头部比较，让最大值左边的数字全部出队
                while queue[-1] > queue[head]:
                    head += 1
            # 收集最大值
            if i >= k - 1:
                maxs.append(queue[head])
        
        return maxs
