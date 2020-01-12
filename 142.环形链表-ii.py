#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#
# https://leetcode-cn.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (46.35%)
# Likes:    321
# Dislikes: 0
# Total Accepted:    44.5K
# Total Submissions: 94.4K
# Testcase Example:  '[3,2,0,-4]\n1'
#
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# 
# 说明：不允许修改给定的链表。
# 
# 
# 
# 示例 1：
# 
# 输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 
# 
# 
# 
# 示例 2：
# 
# 输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
# 
# 
# 
# 
# 示例 3：
# 
# 输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。
# 
# 
# 
# 
# 
# 
# 进阶：
# 你是否可以不用额外空间解决此题？
# 
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # 参考官方最优解
    # https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode/
    
    def getIntersect(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return fast
        
        return None
    
    
    def detectCycle(self, head: ListNode) -> ListNode:
        node = self.getIntersect(head)
        if node is None:
            return None
        
        ptr1 = head
        ptr2 = node
        
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        return ptr1

# @lc code=end

def cycleList(head, pos):
    nodes = []
    for i in head:
        node = ListNode(i)
        if len(nodes) > 0:
            nodes[-1].next = node
        nodes.append(node)

    if len(nodes) == 0 or pos >= len(nodes):
        return (None, None)

    if pos == -1:
        return (nodes[0], None)
    
    nodes[-1].next = nodes[pos]
    return (nodes[0], nodes[pos])


if __name__ == '__main__':
    s = Solution()
    head, result = cycleList([3,2,0,-4], 1)
    assert s.detectCycle(head) == result

    head, result = cycleList([1,2], 0)
    assert s.detectCycle(head) == result

    head, result = cycleList([], -1)
    assert s.detectCycle(head) == result

    head, result = cycleList([-1,-7,7,-4,19,6,-9,-5,-2,-5], 6)
    assert s.detectCycle(head) == result

