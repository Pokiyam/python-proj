# 10 + 20 + 30 + 40 - 50 계산과정
# ['10', '+', '20', '+', '30', '+', '40', '-', '50']
# ['30', '+', '30', '+', '40', '-', '50']
# ['60', '+', '40', '-', '50']
# ['100', '-', '50']
# ['50']

import os

os.system("cls")
op = ["+", "-", "*" , "/", "="]

# 계산기 함수
def str_calculator(user_input, show_history):
    str_list = []
    lop = 0 # last operation position
    for i, s in enumerate(user_input):
        if s in op:
            if user_input[lop:i].strip() != "":
                str_list.append(user_input[lop:i].strip())
                str_list.append(s)
                lop = i + 1
    str_list.append(user_input[lop:].strip())

    pos = 0
    while True:
        if pos + 1 > len(str_list):
            break
        if str_list[pos] in op:
            temp = str_list[pos-1] + str_list[pos] + str_list[pos+1]
            del str_list[0:3]
            str_list.insert(0, str(eval(temp))) #insert 해야 list의 앞으로 삽입
            pos = 0
        pos += 1
        if(show_history == True):
            print(str_list)
    if len(str_list) > 0:
        result = float(str_list[0])
    return round(result, 4)

# main
while True:
    user_input = input("계산식을 입력하세요> ")
    if user_input == "/exit": #계산 종료 기능
        break
    elif user_input == "/clear": #화면 지우는 기능
        os.system("cls")
        continue
    result = str_calculator(user_input, show_history=True)
    print("결과 : {}".format(result))   
