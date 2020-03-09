#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next:
            return str(self.val) + "->" + str(self.next)
        else:
            return str(self.val)

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 修改链表：时间复杂度O(N)，空间复杂度O(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        # 用快慢指针来找链表中间节点。当快指针到达（或超出）链表尾部时，
        # 慢指针正好走到中间节点（对于偶数节点当链表就是中间位置的下一个）
        # 意思是对于节点个数为N的链表，中间节点就是第 N // 2 + 1 个节点
        fast = head
        slow = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # 以中间节点为界限，拆分成前后两个链表
        if prev:
            prev.next = None
        # 反转后半部分的链表
        rev_head = self.reverse(slow)
        # 把前后两个链表从头到尾进行回文比较
        n1 = head
        n2 = rev_head
        while n1 and n2:
            if n1.val != n2.val:
                return False
            n1 = n1.next
            n2 = n2.next
        
        return True

    # 用3个指针来反转链表
    def reverse(self, head):
        if head is None or head.next is None:
            return head
        
        prev = None
        curr = head
        next = curr.next
        
        while next:
            curr.next = prev
            prev = curr
            curr = next
            next = next.next
        
        curr.next = prev
        return curr

# @lc code=end

# 链表转数组：时间复杂度O(N)，空间复杂度O(N)
class Solution1:
    def isPalindrome(self, head: ListNode) -> bool:
        arr = []
        n = head
        while n is not None:
            arr.append(n.val)
            n = n.next
        
        i = 0
        j = len(arr) - 1
        while i < j:
            if arr[i] != arr[j]:
                return False
            i += 1
            j -= 1
        
        return True


# -------
# 测试用例
# -------

def convert(s: str) -> ListNode:
    nodes = list(map(lambda x: ListNode(x), s.split("->")))
    temp = None
    for node in nodes:
        if temp is not None:
            temp.next = node
        temp = node
    return nodes[0]

if __name__ == "__main__":
    s = Solution()
    assert s.isPalindrome(convert("1")) == True
    assert s.isPalindrome(convert("1->2")) == False
    assert s.isPalindrome(convert("1->2->1")) == True    
    assert s.isPalindrome(convert("1->2->3->4->5")) == False
    assert s.isPalindrome(convert("1->2->2->1")) == True
    assert s.isPalindrome(convert("1->1->2->1")) == False
