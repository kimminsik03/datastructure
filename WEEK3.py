import array
arr =array.array('f',[11, 9 ,-77, 8])

for i in range(len(arr)):
    print (arr[i],id(arr[i]))
#배열 처럼 보이는 리스트