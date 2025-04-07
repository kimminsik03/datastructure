import random

num = random.randint(1,100)
tries = 0

while True:
    inputnum = int(input("1~100 사이의 숫자를 입력하시오:"))

    if(inputnum == num):
        break
    elif(inputnum >num ):
        print("입력하신 수보다 작습니다")

    else:
        print("입력하신 수보다 큽니다")

    tries+=1

print(f"정답입니다 시도횟수{tries}")

