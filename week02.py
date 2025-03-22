n = int(input("10단위 수 입력:"))
result =0

#선형 시간 O(n)
for i in range (1, n+1):
    result += i

print(result)