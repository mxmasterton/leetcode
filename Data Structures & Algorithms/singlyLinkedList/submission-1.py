class LinkedNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = LinkedNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next_node
        i = 0

        while curr:
            if i == index:
                return curr.value
            i += 1
            curr = curr.next_node
        return -1
        

    def insertHead(self, value: int) -> None:
        new_node = LinkedNode(value)
        new_node.next_node = self.head.next_node
        self.head.next_node = new_node

        if not new_node.next_node:
            self.tail = new_node

    def insertTail(self, value: int) -> None:
        self.tail.next_node = LinkedNode(value)
        self.tail = self.tail.next_node

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while i < index and curr:
            i += 1
            curr = curr.next_node

        if curr and curr.next_node:
            if curr.next_node == self.tail:
                self.tail = curr
            curr.next_node = curr.next_node.next_node
            return True

        return False

    def getValues(self) -> List[int]:
        curr = self.head.next_node
        out = []

        while curr:
            out.append(curr.value)
            curr = curr.next_node

        return out        
