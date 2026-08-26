class Node:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):
        self.right = Node(0)
        self.left = Node(0)
        self.right.prev = self.left
        self.left.next = self.right

    def get(self, index: int) -> int:
        curr = self.left.next

        while curr and index > 0:
            curr = curr.next
            index -= 1
            
        if curr and curr!= self.right and index == 0:
            return curr.val
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        node, next, prev = Node(val), self.left.next, self.left

        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next


    def addAtTail(self, val: int) -> None:
        node, next , prev = Node(val), self.right, self.right.prev

        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.left.next

        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and index ==0:
            node, next, prev = Node(val), curr , curr.prev 

            prev.next = node
            next.prev = node
            node.prev = prev
            node.next = next

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next

        while curr and index > 0:
            curr = curr.next
            index -= 1

        if curr and curr != self.right and index ==0:
            next, prev = curr.next, curr.prev

            prev.next = next
            next.prev = prev

            curr.next, curr.prev, curr.val = None,None,None



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)