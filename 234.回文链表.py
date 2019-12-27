#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
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
    assert s.isPalindrome(convert("1->2->2->1")) == True