#중복값을 출력하기

def sameValue (city):
    list = list() #중복값을 출력할 리스트
    s = set()
    for city in city: #시티 배열에서 도시를 하나씩 빼옴
        l1 = len(s)  #길이를 구함
        s.add(city)  #값을 넣어줌
        l2 = len(s)  #길이를 구함 만약 중복 값이 들어오지 않으면 길이는 변하지 않음
        if l1 == l2: #따라서 두 변수의 길이가 같다는 것은 중복값이 들어왔다는 걸 의미
            list.append(city) # 중복값 배열에 넣기


city = ["인천","서울","김포","수원","서울","부산"]
city.append("김포") #set은 add 속성을 통하여 값을 추가할 수 있음 다만 중복 값은 무시됨
city.append("대전")
print(city)




