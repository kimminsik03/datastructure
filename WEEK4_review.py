import random

from multiprocessing.spawn import prepare


class node:
    def __init__(self,data):
        self.data = data
        self.link = None


class linklist:
    def __init__ (self):
        self.head =None   #시작 노드가 있는지 검사하기 위한 변수를 만듬

    def appeand (self,data):
        if not self.head:
            self.head = node(data)
            return
        current = self.head
        while current.link: #none이 나오기 전까지 계속 반복
            current = current.link
        current.link = node(data)

    def __str__(self):
        Node = self.head
        output =""
        while Node is not None:
           ndata = Node.data
           output += f"{ndata} ->"
           Node = Node.link
        return output

    def remove (self,target): # 노드 값을 삭제
        if self.head.data == target: #만약에 삭제할 노드가 처음에 있는 노드라면
            self.head= self.head.link #현재노드에 있는 링크(다음 노드)를 헤드에 넣어라
            return

        current = self.head #현재 노드를 저장할 변수
        previous = None# 이전의 노드를 저장할 변수

        while current: #한 번에 반복문에는 현재노드만 검사 그리고 한 번 이 while 블록을 검사하고 if에 false가 나오면 그 다음 코드로 이동
            if current.data == target: # 현재 노드에 있는 값이 targer이랑 같으면
                previous.link = current.link #그 말은 현재 노드가 없어질 노드라는 소리임으로 현재 노드가 가리키는 다음 노드의 주소를 이전 노드의 링크로 이전하라
            previous = current #다음 반복문에서 현재노드를 이전 노드로 저장
            current = current.link # 현재 노드에 있는 링크(다음노드의 주소)를 현재 노드로 저장

    def search (self,target):
        result =""
        current = self.head
        while current:
            if current.data == target:
                return f"찾는 값인{target}이 있습니다"

            else :
                current = current.link


        return "원하는 값이 없습니다"

l1 = linklist()
l1.appeand(8)
l1.appeand(9)
l1.appeand(10)
print(l1)

for i in range(10):
    l1.appeand(random.randint(1,30))

print(l1)

print(l1.search(10))