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

    # 参考用户@王尼玛的图解
    # https://leetcode-cn.com/problems/palindrome-linked-list/solution/dong-hua-yan-shi-234-hui-wen-lian-biao-by-user7439/
    def isPalindrome(self, head: ListNode) -> bool:
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
        
# @lc code=end

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
    assert s.isPalindrome(convert("1->2")) == False
    assert s.isPalindrome(convert("1->2->1")) == True    
    assert s.isPalindrome(convert("1->2->3->4->5")) == False
    assert s.isPalindrome(convert("1->2->2->1")) == True
