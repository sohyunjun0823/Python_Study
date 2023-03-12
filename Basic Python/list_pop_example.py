my_list = [1, 2, 3, 4, 5]


#temp = my_list.pop(3)

#print(temp)



n = int(input("찾고싶은 숫자를 입력하세요. : "))


result = 0 # 내가 찾고싶어 하는 숫자(결과)
index = -1 # 내가 찾고싶어 하는 숫자가 어디에 있는지? 방의 위치
for i in range(len(my_list)):
    if my_list[i] == n:
        index = i
        break

if index == -1:
    print("Error")
else:
    result = my_list.pop(index)
    print(result, "이(가) 존재합니다.")
