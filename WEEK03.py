#================================================

#0을 오른쪽으로 옮겨줌
def move_zeros(a_list):
    zero_index =0;
    for index , n in enumerate(a_list):
        if n != 0:
            a_list[zero_index] =n
            if zero_index != index:
                a_list[index] =0
            zero_index +=1
    return(a_list)

a_list = [8,0,3,0,12]
move_zeros(a_list)
print(a_list)

#===============================================

#2개의 리스트를 튜플형태로 묶어서 출력

groups =['HOT','Seventeen','black pink' , 'nkz']
ratings =[1,2,4,3]

group_rating = list(zip(groups ,ratings))
print(group_rating)

#================================================

#중복값을 출력해줌
def duplicate_city(cities):
    result =list()
    s = set()

    for city in cities:
        l1 =len(s)
        s.add(city)
        l2 = len(s)
        if l1 == l2 : #중복값이 들어옴
            result.append(city)
    return result

#city = ['incheon','incheon', 'inhceon', 'gimpo','seoul']
cities = {'incheon','incheon', 'inhceon', 'gimpo','seoul'}
cities = set(cities)
cities.append('anyang')
cities.append('seoul')
print(cities)
print(set(duplicate_city(cities))) #중복 도시 제외

#=========================================================

#2개의 리스트를 돌면서 같은 값을 따로 리스트형태로 출력
def intersection (l1 , l2):
    l3 = list()
    for v in l1 :
        if v in l2:
            l3.append(v)
    return l3

l1 = [45,5,22,31,7,19]
l2 = [2,1,5,22,7,19,38,27,13,8]
print(intersection(l1,l2))











































