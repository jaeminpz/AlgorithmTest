class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def get_kth_node_from_last(self, k):
        # 구현해보세요!
        # 총 길이에서 뒤에 k 값을 빼서 결과값을 구한다.
        length = 1
        cur = self.head

        while cur.next is not None:
            cur = cur.next
            length +=1
        end_length = length - k
        cur = self.head
        for i in range(end_length):
            cur = cur.next

        return cur


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!