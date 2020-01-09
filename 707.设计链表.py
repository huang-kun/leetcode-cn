#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
class MyNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        if self.next is None:
            return str(self.val)
        else:
            return str(self.val) + "->" + str(self.next)

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.count = 0

    def find(self, index: int) -> MyNode:
        if index < 0 or index >= self.count:
            return None
        elif index == 0:
            return self.head
        elif index == self.count - 1:
            return self.tail

        node = self.head
        for i in range(1, index+1):
            node = node.next
            if node is None:
                break
        return node


    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        node = self.find(index)
        return node.val if node is not None else -1
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if self.count == 0:
            self.head = MyNode(val)
            self.tail = self.head
        else:
            node = MyNode(val)
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.count += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.count == 0:
            self.tail = MyNode(val)
            self.head = self.tail
        else:
            node = MyNode(val)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.count += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index > self.count:
            return None
        elif index <= 0:
            self.addAtHead(val)
        elif index == self.count:
            self.addAtTail(val)
        else:
            new = MyNode(val)
            old = self.find(index)
            new.next = old
            new.prev = old.prev
            old.prev.next = new
            old.prev = new
            self.count += 1


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.count:
            return None
        
        old = self.find(index)

        if self.count == 1:
            self.head = None
            self.tail = None
        elif old == self.head:
            self.head = old.next
            self.head.prev = None
        elif old == self.tail:
            self.tail = old.prev
            self.tail.next = None
        else:
            old.prev.next = old.next
            old.next.prev = old.prev
        old.prev = None
        old.next = None
        self.count -= 1


    def __str__(self):
        return str(self.head) if self.head is not None else ""

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

def testCase1():
    obj = MyLinkedList()
    obj.addAtHead(1) 
    assert str(obj) == "1"
    obj.addAtTail(3)
    assert str(obj) == "1->3"
    obj.addAtIndex(1,2)  
    assert str(obj) == "1->2->3"
    assert obj.get(1) == 2
    obj.deleteAtIndex(1)
    assert str(obj) == "1->3"
    assert obj.get(1) == 3

def testCase2():
    obj = MyLinkedList()
    obj.addAtHead(1) 
    assert str(obj) == "1"
    obj.addAtTail(3)
    assert str(obj) == "1->3"
    obj.addAtIndex(1,2)  
    assert str(obj) == "1->2->3"
    assert obj.get(1) == 2
    obj.deleteAtIndex(0)
    assert str(obj) == "2->3"
    assert obj.get(0) == 2

def testCase3():
    obj = MyLinkedList()
    obj.addAtHead(1)
    assert str(obj) == "1"
    obj.deleteAtIndex(0)
    assert str(obj) == ""

def testCase4():
    obj = MyLinkedList()
    obj.addAtHead(24)
    assert str(obj) == "24"
    assert obj.get(1) == -1
    obj.addAtTail(18)
    assert str(obj) == "24->18"
    obj.deleteAtIndex(1)
    assert obj.get(1) == -1
    assert str(obj) == "24"

if __name__ == "__main__":
    testCase1()
    testCase2()
    testCase3()
    testCase4()