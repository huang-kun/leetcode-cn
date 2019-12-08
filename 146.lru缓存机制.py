#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU缓存机制
#
# https://leetcode-cn.com/problems/lru-cache/description/
#
# algorithms
# Medium (44.70%)
# Likes:    316
# Dislikes: 0
# Total Accepted:    25.3K
# Total Submissions: 56.7K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# 运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。
# 
# 获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
# 写入数据 put(key, value) -
# 如果密钥不存在，则写入其数据值。当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间。
# 
# 进阶:
# 
# 你是否可以在 O(1) 时间复杂度内完成这两种操作？
# 
# 示例:
# 
# LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // 返回  1
# cache.put(3, 3);    // 该操作会使得密钥 2 作废
# cache.get(2);       // 返回 -1 (未找到)
# cache.put(4, 4);    // 该操作会使得密钥 1 作废
# cache.get(1);       // 返回 -1 (未找到)
# cache.get(3);       // 返回  3
# cache.get(4);       // 返回  4
# 
# 
#

# @lc code=start
class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        pre = self.prev.key if self.prev is not None else "?"
        nxt = self.next.key if self.next is not None else "?"
        return f"prev[{pre}] -> curr[{self.key}] -> next[{nxt}]"

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head is None and self.tail is None
    
    def append(self, node):
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def popHead(self):
        if self.isEmpty():
            return None
        fst = self.head
        self.remove(fst)
        return fst

    def remove(self, node):
        if node is self.head:
            self.head = node.next
        if node is self.tail:
            self.tail = node.prev
        
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        
        node.prev = None
        node.next = None

    def __str__(self):
        p = self.head
        if p is None:
            return ""

        s = str(p.key)
        while p.next is not None:
            p = p.next
            s += " -> "
            s += str(p.key)
        
        return s

class LRUCache:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.lst = LinkedList()
        self.dic = {}
        self.totalCount = 0
    
    def put(self, key, value):
        node = Node(key, value)
        
        # 如果之前缓存过，更新它在链表中的位置（移到链表尾部）
        if key in self.dic:
            old = self.dic[key]
            self.lst.remove(old)
        else:
            self.totalCount += 1

        self.dic[key] = node
        self.lst.append(node)

        # 如果超过缓存限制，从链表头节点开始清理
        while self.totalCount > self.capacity:
            earliest = self.lst.popHead()
            if earliest is not None:
                del self.dic[earliest.key]
                self.totalCount -= 1

    def get(self, key):
        # 如果之前缓存过，更新它在链表中的位置（移到链表尾部）
        if key in self.dic:
            node = self.dic[key]
            if node is not self.lst.tail:
                self.lst.remove(node)
                self.lst.append(node)
            return node.value
        else:
            return -1

    def __str__(self):
        return str(self.lst)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

def testLRUCache():
    cache = LRUCache(2)

    cache.put(2, 1)
    assert(str(cache) == "2")
    
    cache.put(1, 1)
    assert(str(cache) == "2 -> 1")
    
    cache.put(2, 3)
    assert(str(cache) == "1 -> 2")
    
    cache.put(4, 1)
    assert(str(cache) == "2 -> 4")
    
    r = cache.get(1)
    assert(r == -1)
    assert(str(cache) == "2 -> 4")
    
    r = cache.get(2)
    assert(r == 3)
    assert(str(cache) == "4 -> 2")
    
    cache.put(1, 1)
    assert(str(cache) == "2 -> 1")
    
    cache.put(2, 2)
    assert(str(cache) == "1 -> 2")
    
    r = cache.get(1)
    assert(r == 1)
    assert(str(cache) == "2 -> 1")
    
    cache.put(3, 3)
    assert(str(cache) == "1 -> 3")
    
    r = cache.get(2)
    assert(r == -1)
    assert(str(cache) == "1 -> 3")
    
    cache.put(4, 4)
    assert(str(cache) == "3 -> 4")
    
    r = cache.get(1)
    assert(r == -1)
    assert(str(cache) == "3 -> 4")
    
    r = cache.get(3)
    assert(r == 3)
    assert(str(cache) == "4 -> 3")
    
    r = cache.get(4)
    assert(r == 4)
    assert(str(cache) == "3 -> 4")

def testLRUCache2():
    cache = LRUCache(1)
    cache.put(2,1)
    assert(str(cache) == "2")
    r = cache.get(2)
    assert(r == 1)
    assert(str(cache) == "2")

if __name__ == "__main__":
    testLRUCache()
    testLRUCache2()