# class stack:
#     def __init__(self): #배열
#         self.items = []
#
#     def push(self,data):
#         self.items.append(data)
#
#     def pop(self):
#         self.items.pop()
#
#     def size(self):
#         return  len(self.items)
#
#     def is_empty(self): # true or false
#         return (self.items) == 0
#
#     def peek(self):
#         return self.items[-1]
#
#
# st1 = stack()
#
# st1.push(1)
# st1.push(2)
# st1.push(3)
# print(st1.size())
#
# st1.pop()
# print(st1.size())


# class Node:
#     def __init__(self,data,link =None):
#         self.data = data
#         self.link = link
#
# class stack:
#     def __init__(self):
#         self.head = None
#
#     def push(self,data):
#         node = Node(data)
#         if self.head == None:
#             self.head =node
#             return
#         else:
#              node.link= self.head
#              self.head = node
#
#     def pop(self):
#         if self.head == None:
#             return "이 스택은 비어 있습니다"
#
#         last_node = self.head
#         self.head = self.head.link
#         return last_node.data
#
#
# s1 = stack()
#
# s1.push(1)
# s1.push(2)
# print(s1.pop())
# print(s1.pop())

# stack = []
# print(stack)
# stack.append(1)
# print(stack)
# stack.append(2)
# print(stack)
# stack.append(3)
# print(stack)
# stack.pop()
# print(stack)


def cheak (string):
    stack =[]
    for c in string:
        if c == "(":
            stack.append(c)
        if c == ")":
           if len(stack)==0:
               return False
           else:
               stack.pop()
    return len(stack) ==0 # 이걸 통해 스택이 0이면 정상적으로 괄호가 들어 갔다는 거임

print(cheak("안녕하세요 (자료구조)입니다"))








