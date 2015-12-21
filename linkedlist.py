class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def add(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
            self.next = None
        else:
            node.next = self.head
            self.head = node
        self.count += 1

    def pop(self):
        if not self.head:
            raise Exception("Unable to pop because linked list head is None")
        popped_value = self.head.data
        self.head = self.head.next
        self.count -= 1
        return popped_value

    def peek(self):
        return self.head.data

    def size(self):
        return self.count

    def has_cycle(self):
        head = self.head
        count = self.count
        while count:
            head = head.next
            count -= 1
        return head is not None

    def circular(self):
        fast = self.head
        slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

    def remove(self, node):
        if node == self.head:
            self.pop()
            return

        new = self.head
        while new:
            if node != new:
                old = new
                new = new.next
            else:
                new = new.next
                old.next = new
                self.count -= 1
                break

ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
ll.add(6)
ll.add(7)
# ll.add(8)
# ll.size()
# ll.peek()
# ll.head.next.next.next.next.next = ll.head.next
# ll.head.next.next.next.next.next.next.next.next = ll.head.next.next
# ll.pop()
# ll.is_valid()
