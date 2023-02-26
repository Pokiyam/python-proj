import random
import os

numbers = []
number = str(random.randint(0,9))
os.system("cls")

print("*" * 60)
print("숫자 야구게임을 시작합니다!!!")
print("*"*60)

#세 자리 숫자만 입력할 수 있게 하는 함수
def input_check(msg, casting = int):
    while True:
        try:
            num = input(msg)
            num_str = str(num)
            if(casting(num) and len(num) == 3):
                return num_str
        except:
            print("입력 오류")
            continue
        
# 0~9까지 랜덤 숫자 3개 뽑아서 numbers에 저장 
for i in range(3):
    while number in numbers:
        number = str(random.randint(0,9))
    numbers.append(number)

# 사용자가 숫자 3개를 입력해서 각 자리수 비교하기 
strike_cnt = 0
ball_cnt = 0
while strike_cnt<3:
    strike_cnt = 0
    ball_cnt = 0
    num = input_check("숫자 3개를 입력하세요>")
    for i in range(3):
        for j in range(3):
            if(num[i] == numbers[j]):
                if(i == j):
                    strike_cnt += 1
                else:
                    ball_cnt += 1
    if(strike_cnt == 0 and ball_cnt == 0):
        print("3아웃!!!")
    else:
        output = ""
        if(strike_cnt > 0):
            output += "{}스트라이크".format(strike_cnt)
        if(ball_cnt > 0):
            output += "{}볼".format(ball_cnt)
        print(output)

print("성공! 정답은 {} 입니다!".format(num))
        