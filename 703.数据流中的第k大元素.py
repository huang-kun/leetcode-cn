#
# @lc app=leetcode.cn id=703 lang=python3
#
# [703] 数据流中的第K大元素
#


# 解题思路：（学习自极客时间算法课）
# 1. 选择一种数据结构作为容器用来保存前k大的数，并且容器最多保存k个数字
# 2. 每次向容器添加新数字时，始终保持容器中第一个元素为最小值
# 3. 如果容器已满，再添加新数字时，就跟第一个元素比较，大于第一个元素就替换，
#    并且重新排序，始终保持容器中第一个元素为最小值
# 4. 最后，容器中的第一个元素即为第k大的数


# 方法一：用数组保存前k大的数
# 
# 时间复杂度: 
# N为nums的元素个数，包括后续添加val个数，所以遍历和添加需要O(N)
# 给数组arr排序（按照快速排序）需要k * log(k)
# 因此结果为O(N * k * log(k))

class KthLargest1:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = [] # 保存前k大的数
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.arr) < self.k:
            self.arr.append(val)
            if len(self.arr) == self.k:
                self.arr.sort()
        elif val > self.arr[0]:
            self.arr[0] = val
            self.arr.sort()

        return self.arr[0]

# ----------------------------------------------------

# 方法二：用最小堆（小顶堆）保存前k大的数，因为堆顶元素始终最小。
# 根据解题思路，也只允许这个最小堆保存k个元素。
# 最小堆的调整时间最差需要log2(k)，所以总时间复杂度为O(N * log2(k)) 

class MinHeap:

    def __init__(self, limit):
        self.arr = [0]
        self.size = 0
        self.limit = limit
    
    def top(self):
        return self.arr[1] if self.size > 0 else None
    
    def insert(self, num):
        if self.size < self.limit:
            self.size += 1
            self.arr.append(num)
            self.percUp(self.size)
        elif num > self.arr[1]:
            self.arr[1] = num
            self.percDown(1)

    def percUp(self, i):
        while i // 2 > 0:
            p = i // 2
            if self.arr[p] > self.arr[i]:
                self.arr[p], self.arr[i] = self.arr[i], self.arr[p]
            i = p

    def percDown(self, i):
        while i * 2 <= self.size:
            mc = self.minChild(i)
            if self.arr[i] > self.arr[mc]:
                self.arr[i], self.arr[mc] = self.arr[mc], self.arr[i]
            i = mc
    
    def minChild(self, i):
        left = i * 2
        right = i * 2 + 1
        if right > self.size:
            return left
        return left if self.arr[left] < self.arr[right] else right


class KthLargest2:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = MinHeap(k) # 保存前k大的数
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        self.heap.insert(val)
        return self.heap.top()

# ----------------------------------------------------

# 方法三：用优先队列保存前k大的数
# 
# 优先队列的实现机制：
# 1. Heap (Binary, Binomial, Fibonacci)
# 2. Binary Search Tree
#
# PriorityQueue是Python3中内置的优先队列，每次都会把最小的元素优先出队。
# 有个问题是，这个优先队列没有peek()方法，默认无法看到队列中即将出队的元素，
# 所以干脆先出队，再用属性保存出队的结果，拿去做比较。
# https://docs.python.org/3.6/library/queue.html#queue.PriorityQueue

from queue import PriorityQueue

class KthLargest3:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.queue = PriorityQueue() # 保存前k大的数
        self.size = 0 # 队列中的元素个数
        self.first = None # 队列中的即将出队的元素，也可以理解为队列的首位元素（最小的排首位）
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if self.size < self.k:
            self.queue.put(val)
            self.size += 1
            if self.size == self.k:
                self.first = self.queue.get() # 这里本应该是peek()
        elif val > self.first:
            self.queue.put(val)
            self.first = self.queue.get()
        
        return self.first

# ----------------------------------------------------

# 方法四：用Python内置的heapq，其实就是用数组来保存前k大的数，只
# 是用了二叉树/堆算法来调整数组元素位置，把一个普通的数组变成一个
# 最小堆来使用，无需使用额外的数据结构。
# https://docs.python.org/3.6/library/heapq.html#module-heapq

from heapq import *

class KthLargest4:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = [] # 保存前k大的数
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val) # 添加元素，调整位置
        elif val > self.heap[0]:
            heapreplace(self.heap, val) # 弹出并返回最小元素，然后添加新元素，size不变
        
        return self.heap[0]

