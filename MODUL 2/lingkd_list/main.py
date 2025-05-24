class Node:
    def _init_(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def _init_(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def delete_first(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_last(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.prev.next = None

    def delete_by_value(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                return
            curr = curr.next

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=' <-> ')
            curr = curr.next
        print("None")

# Contoh penggunaan
dll = DoubleLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

print("Sebelum penghapusan:")
dll.display()

dll.delete_first()
print("Setelah hapus node pertama:")
dll.display()

dll.delete_last()
print("Setelah hapus node terakhir:")
dll.display()

dll.delete_by_value(30)
print("Setelah hapus node dengan nilai 30:")
dll.display()
