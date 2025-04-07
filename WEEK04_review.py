import random

class Node:
    def __init__(self,data,link=None):
        self.data = data
        self.link = link

class Llist :
    def __init__(self):
        self.head = None

    def append(self,data):
        if self.head == None:
           self.head = Node(data)
           return

        current = self.head

        while current.link:
            current = current.link
        current.link = Node(data)

    def __str__(self):
        current  = self.head
        result =""
        while current:
            result += f"{current.data} ->"
            current = current.link
        return result + "end"

    def search(self,target):

        current = self.head

        while  current:
            if current.data ==target:
                return f"찾으시는 숫자{target}를 찾았습니다"

            current = current.link
        return f"찾으시는 숫자{target}를 찾지 못했습니다"

    def remove(self,target):
        current = self.head
        pre = None


        while current:
            if self.head.data == target:  # 첫번째 노드를 지울 때
                self.head = self.head.link
                return

            while current:
                if current.data == target:
                    pre.link = current.link
                pre=current
                current = current.link

#=========================================================================

    def reverse(self):
      current = self.head
      pre =None

      while current:
          next = current.link # 다음으로 이동할 노드의 주소를 어디가에 보관
          current.link =pre #현재 노드의 링크를 이전 노드로 설정
          pre=current #다음 반복문에 쓸 이전노드를 현재노드로 저장
          current=next
      self.head = pre


    def detect_cycle(self):
        slow =self.head
        fast =self.head

        while True:
            try:
                slow =slow.link
                fast = fast.link.link
                if fast == slow:
                    return True
            except:
                return False










list1 = Llist()

list1.append(1)
list1.append(2)
list1.append(3)
print(list1)

# for i in range(1,10):
#     list1.append(random.randint(1,30))
# print(list1)
#
# print(list1.search(20))

list1.remove(1)
list1.remove(2)

print(list1)
list1.reverse()
print(list1)
print(list1.detect_cycle())
