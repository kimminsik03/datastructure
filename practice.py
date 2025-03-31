# def inter(list1,list2):
#     list3 = []#이게 중복 값을 저장할 리스트
#     for value in list1:
#         if value in list2:
#             list3.append(value)
#     return list3
#
# list1 = [45, 5, 22, 31, 7, 19]
# list2 = [2, 1, 5, 22, 7, 38, 27, 19, 13, 41]
#
# list3 = list()
# list3= inter(list1,list2)
# print(set(list3))

# def inter(list1, list2):
#     setList1=set(list1)
#     setList2=set(list2)
#     return setList1.intersection(setList2)
#
# list1 = [45, 5, 22, 31, 7, 19]
# list2 = [2, 1, 5, 22, 7, 38, 27, 19, 13, 41]
# print(inter(list1,list2))

# def sample(list1):
#     s1 = set()
#     list3 = []
#
#     for value in list1:
#         l1 = len(s1)
#         s1.add(value)
#         l2 = len(s1)
#         if(l1 == l2):
#             list3.append(value)
#     return list3
#
# list1 = [45, 5, 22, 31, 7, 19,7,19,3]
# print(sample(list1))

def sample(list):
    zeroindex =0
    for index, value in enumerate(list):
        if value !=0:
            list[zeroindex] = value
            if index != zeroindex:
                list[index] =0
            zeroindex+=1
    return list



l = [11, 0, 9, 0, -77]
print(sample(l))

