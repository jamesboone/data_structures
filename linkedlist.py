class Node(object):
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def add(self, data):
        node = Node(data, None, None)
        if self.head is None:
            self.head = node
            self.tail = node
            self.next = None
            self.prev = None
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.count += 1

    def pop(self):
        if not self.head:
            return 'pop not valid'
        popped_value = self.head.data
        self.head = self.head.next
        self.count -= 1
        return popped_value

    def pop_dll_head(self):
        if self.head or not self.tail:
            popped_value = self.head.data
            self.head.next.prev = None
            self.head = self.head.next
            self.count -= 1
            return popped_value
        else:
            return 'wrong'

    def pop_dll_tail(self):
        if self.tail or not self.head:
            popped_value = self.tail.data
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.count -= 1
            return popped_value
        else:
            return 'wrong'

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

    def remove_dll(self, node_to_remove):
        if node_to_remove == self.head:
            self.pop_dll_head()
            return
        elif node_to_remove == self.tail:
            self.pop_dll_tail()
            return

        node_to_remove.prev.next = node_to_remove.next
        node_to_remove.next.prev = node_to_remove.prev
        self.count -= 1
        return


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
# ll.harvey()
# ll.is_valid()


# def remove_node(self):
