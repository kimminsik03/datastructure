#중복 요소 찾기
city = ["인천","서울","김포","수원","서울","부산"]

city = set(city) #set를 사용하면 중복값은 제외하고 출력이 됨
city.add("김포") #set은 add 속성을 통하여 값을 추가할 수 있음 다만 중복 값은 무시됨
city.add("대전")

print(city)



