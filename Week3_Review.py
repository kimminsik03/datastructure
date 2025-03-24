def move_zeros(list):
    zero_index =0
    for index , value in enumerate(list):
            if value != 0: #0이 아닌 값을 왼쪽으로 옮기기 위해
                list[zero_index] = value     #0이 아닌 값을 실제로 맨 왼쪽부터 옮김
                if zero_index != index:     #둘이 같지 않다는 것은 위에서 index에 값을 복사했다는 뜻
                    list[index] =0          #위에서 index에 value값을 복사하였으니 원래값(index)은 0으로 바뀜
                zero_index+=1
    return(list)

list =[1,0,7,12,0,4]
move_zeros(list)
print(list)


# list = [1,2,3,4,5]
#
# for i in range (len(list)):
#     print(i,list[i])

#enumerate 함수는 값과 인덱스를 함께 반환
#for i in enumerate(list)
#=> 여기에서 i는 튜플 형태로 받음
#ex) (0,1) (1,10)
#=> 이걸 언팩킹하기 위해서 반복문에 2개의 변수를 사용
