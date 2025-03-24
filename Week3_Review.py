#방법 1 리스트 축약으로 교집합을 확인
# def same(list1,list2):
#     list3 = [v for v in list1 if v in list2 ]
#     # 리스트 축약
#     #풀어보면  list1을 돌면서 안에 있는 값이 v를 꺼내서 list2에 있는 v값이 같으면 list3에 v(맨 앞에)를 추가(append)
#     return(list3)


#방법 2 set함수 안에는 intersection() 즉 교집합을 구하는 함수가 있으므로 이를 활용함
def same(list1,list2):
   set1 = set(list1)
   set2 = set(list2)
   return list(set1.intersection(set2)) # set1 & set2


list1  = [1,5,6,11,25,13]
list2  = [2,5,7,12,11,25]
list3 = same(list1,list2)
print(list3)



