class Node:
    def __init__(self,data,link=None):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if not self.head: #링크드리스트가 하나도 없는 상태
            self.head = Node(data) #새 노트를 해더에 연결
            return
        current = self.head
        while current.link:
            current = current.next #다음 노드로 이동
        current = Node(data)

ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
