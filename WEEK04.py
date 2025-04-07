import random

class node:
    def __init__(self,data,link=None):
        self.data = data
        self.link = link

class list:
    def __init__(self):
        self.head = None

    def append(self,data):
        current = self.head
        if not current:
            self.head = node(data)
            return

        while current.link:
            current=current.link
        current.link = node(data)

    def __str__(self):
        current = self.head
        result =""
        while current:
            result = result + f"{current.data}->"
            current = current.link
        return result + "tail"

    def search(self,target):
        current = self.head
        while current:
            if current.data == target:
                return f"찾는 값{target}이 있습니다"
            current = current.link
        return f"찾는 값{target}이 없습니다"

    def remove(self,target):

        if self.head.data == target:
            self.head = self.head.link
            return

        pre = None
        current =self.head
        while current:
            if current.data == target:
                pre.link=current.link
                return
            pre=current
            current = current.link


a = list()
a.append(1)
a.append(2)
a.append(3)
print(a)

# for i in range(1,10):
#     a.append(random.randint(1,30))
# print(a)
# print(a.search(10))
a.remove(2)
a.remove(1)
print(a)