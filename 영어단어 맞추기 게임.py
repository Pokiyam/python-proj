# 딕셔너리, 리스트 사용 (O)
# 모든 문제 다 제출하면, 점수 출력하는 기능 (O)
# 대/소문자 입력 가능하게 함 (O) lower() 
# 영어만 입력하게 함 
# 힌트 기능 만들기 
# 띄어쓰기 입력할 수도있으므로 strip() 해주기 (O)

import random
import os

word_dict = {
    "정보" : "information",
    "열정" : "passion",
    "냉장고" : "refrigerator",
    "사자" : "lion",
    "얼음" : "ice"
}

words = []
solved = []

for i in word_dict:
    words.append(i)

random.shuffle(words)

os.system("cls")
chance = 3
score = 0

print("기회는 총 {}번 입니다.".format(chance))
for i in range(len(words)):
    chance = 3
    print("*"*30)
    print("{}번째 문제(20점)".format(i+1))
    print("*"*30)
    for j in range(chance):
        print("기회가 {}번 남았습니다.".format(chance))
        user = str(input("{}을/를 영어로 하면?>".format(words[i])))
        answer = word_dict[words[i]]
        if(user.strip().lower() == answer.lower()):
            if(i == len(words) - 1):
                print("정답!")
            else:
                print("정답! 다음 문제로 넘어갑니다.!")
            solved.append(words[i])
            break
        else:
            print("오답입니다.")
            chance -= 1
        if chance == 0:
            if(i == len(words) - 1):
                print("문제를 맞추지 못하였습니다.")
            else:
                print("문제를 맞추지 못하였습니다. 다음문제로 넘어갑니다.")
                break
        

print("*" * 30)
print("맞춘 문제")
print("*" * 30)
for i in range(len(solved)):
    print(solved[i])
    score += 20

print("총 {}개의 문제를 맞추셨습니다. 점수는 {}점 입니다!".format(len(solved), score))