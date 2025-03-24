import random
rand = random.randint(1,100) #랜덤한 수를 뽑아서 rand값에 넣음

count =0
left = 0
right = 100
while True:
    income = int(input("1~100까의 숫자를 입력하시오:"))
    count += 1

    if income > rand:
        right = income
        print("이것보다는 값이 작습니다")


    elif income < rand:
        left = income
        print("이것보다는 값이 큽니다")

    else:
        print("축하드려요!")
        print( "시도횟수 :",str(count) + "번")
        print("정답 :",rand)
        break

