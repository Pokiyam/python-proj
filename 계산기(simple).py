import os

while True:
    os.system("cls")
    s = input("계산식 입력> ")
    #eval() : string을 계산가능한 식으로 바꿔주는 함수
    print("결과 : {}".format(eval(s)))
    os.system("pause")