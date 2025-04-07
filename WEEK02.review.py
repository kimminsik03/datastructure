# import array
#
# arr=array.array('i',[1,2,3,4])
#
# for i in range(len(arr)):
#     print(f"{arr[i]},{id(arr[i])}")
#

# def move(list):
#     zero_index = 0
#     for index, n in enumerate(list):
#         if n != 0:
#             list[zero_index] = n
#             if zero_index != index:
#                 list[index] = 0
#             zero_index +=1
#     return (list)
#
# list = [1,0,3,4,0]
# move(list)
# print(list)

# list1 = ["1","2","3"]
# list2 = [1,2,3,3,4,5,6,6,7]
# var = list(zip(list1,list2))
# print(var)
#
# list2_2=set(list2)
# print(list2_2)

# def dupli(arr):
#     result = list()
#     s = set()
#
#     for solo in arr:
#         s1 = len(s)
#         s.add(solo)
#         s2 = len(s)
#         if s1 == s2:
#             result.append(solo)
#     return result
#
# list1 = [1,2,5,123,4,6,12,4,5,1,22,6,8,2]
#
# print(list1)
# print((dupli(list1)))


# def inter(list1, list2):
#     list3 = []
#     for i in list1:
#         if i in list2:
#             list3.append(i)
#     return list3
#
# list1 = [1,2,3,4,5]
# list2 = [3,4,5,6,7]
# print(inter(list1,list2))


# def inter(li1, li2):
#     s1=set(li1)
#     s2=set(li2)
#     return (s1 & s2)
#
# list1 = [1,2,3,4,5]
# list2 = [3,4,5,6,7]
#
# print(inter(list1,list2))