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

class Solution:

    # 重新答题（2020年1月15日）
    def isPalindrome(self, head: ListNode) -> bool:
        # 快慢指针找到链表中间位置
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        if slow is None:
            return True
        if slow.next is None:
            return slow.val == head.val
        
        # 反转链表的后半部分
        prev, curr, next = None, slow, slow.next
        while next:
            curr.next = prev
            prev, curr, next = curr, next, next.next
        curr.next = prev
                
        # 回文比较
        p1 = head
        p2 = curr
        while p2:
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        
        return True

    # @lc code=end

    # 初级思路：将该问题转换为，求解一个数组是否为回文数组？
    # 需要O(n)的空间将链表转换为数组
    def isPalindrome2(self, head: ListNode) -> bool:
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        
        i, j = 0, len(arr) - 1
        while i < j:
            if arr[i] != arr[j]:
                return False
            i += 1
            j -= 1
        
        return True

    # 参考用户@王尼玛的图解
    # https://leetcode-cn.com/problems/palindrome-linked-list/solution/dong-hua-yan-shi-234-hui-wen-lian-biao-by-user7439/
    def isPalindrome1(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        
        # 用双指针（一快一慢）来寻找链表中间节点：
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # show此时所在的位置为第(len // 2 + 1)个节点，其中len表示链表节点总数
        fast = slow
        slow = head

        # 反转链表的后半部分（需要3个指针）
        prev, curr, next = None, fast, fast.next
        while next:
            # 反转当前节点的指向
            curr.next = prev
            # 3个指针依次向前移动
            prev, curr, next = curr, next, next.next
        # 反转最后一个节点的指向
        curr.next = prev

        # 回文比较
        while curr:
            if curr.val != slow.val:
                return False
            curr = curr.next
            slow = slow.next
        
        return True
        

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
