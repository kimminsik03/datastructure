#선형 시간 O(n)
n = int(input("10단위 수 입력:"))
result =0

for i in range(1 , n+1):
    print(result)


#상수시간 O(1)
result =n * (n+1)/2

print(result)