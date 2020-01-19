#
# @lc app=leetcode.cn id=237 lang=python3
#
# [237] 删除链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    # 我一开始认为这道题目是个bug，出题者少给了参数，没有提供链表head，我怎么删除node？
    # 在想不通的情况下去看了几条评论，发现讨论的人都在说题目本身没有问题，我这才恍然大悟，
    # 原来这道题就是考察如何在不提供head（链表信息不全）的情况下删除node
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 从node开始遍历链表，将node.next的val值赋给当前的node.val，最后删除尾节点
        prev = None
        curr = node
        while curr.next:
            curr.val = curr.next.val
            prev = curr
            curr = curr.next
        prev.next = None
        
# @lc code=end

