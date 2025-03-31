import  random


class node:
    def __init__(self,data,link =None):
        self.data = data
        self.link = link

class list:
    def __init__(self):
        self.head = None

    def append (self,data):
        if self.head == None:
            self.head = node(data)
            return
        corrent = self.head
        while corrent.link:
            current = current.link
        current.link = node(data)



    def __str__(self):
        Node = self.head
        output = ""
        while Node is not None:
            ndata = Node.data
            output += f"{ndata} ->"
            Node = Node.link
        return output

l1 = list()
l1.append(8)
l1.append(9)
l1.append(10)
print(l1)


