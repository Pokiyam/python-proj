import itertools
import zipfile
import os

class Colors:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '033[37m'
    UNDERLINE = '033[4m'
    RESET = '\033[0m'
    BRIGHT_MAGENTA = '\033[95m'

def input_check():
    while True:
        path = str(input("zip파일 경로>")).strip()
        if(path == "C:/zip/solve.zip"):
            ZipPath = zipfile.ZipFile(path)
            return ZipPath
        else:
            print("잘못된 경로입니다.")
            continue

def manual():
    print("                  ● 사용 방법 ●\n")
    print("1. C드라이브에 들어간다.\n")
    print("2. 새 폴더를 만들고 이름을 'zip' 으로 바꿔준다.\n")
    print("3. 암호를 알고싶은 zip파일을 새로만든 'zip' 폴더에 넣어준다.\n")
    print("4. 암호를 알고싶은 zip파일의 이름을 'solve' 로 바꿔준다.\n")
    print("5. 아래 경로를 복사하여 붙여넣기한다.")
    print("")
    print("          C:/zip/solve.zip")
    print("")

def decryption(password_binding, min, max, ZipPath):
    """_summary_

    Parameters
    ----------
    password_binding : string
        숫자,영어(대/소),특수문자 등 조합가능한 모든 문자
    min : int
        password의 최소길이
    max : int
        password의 최대길이
    ZipPath : string
        암호를 찾을 Zip파일의 경로 (예시 : zipfile.ZipFile('C:/user/test.zip'))
    ----------
    """
    flag = False
    for i in range(min, max + 1):
        string = itertools.product(password_binding, repeat = i)
        for j in string:
            password = ''.join(j) # 튜플을 string 으로 바꿈 
            print(password)
            try:
                ZipPath.extractall(path='C:/Zip', pwd=password.encode())
                print("*"*50)
                print("암호 해독 완료")
                print(Colors.YELLOW + '암호는 {} 입니다.'.format(password) + Colors.RESET)
                print("*"*50)
                flag = True
                break
            except:
                pass
        if flag == True: #암호 해독완료 시 break
            break


os.system("cls") 

print("*"*60)
print(Colors.RED + '암호가 길수록 시간이 많이 소요됩니다.' + Colors.RESET)
print("")
manual()
print("*"*60)

password_binding = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+"
ZipPath = input_check()
password_len = int(input("암호의 최대 길이 입력>"))
# ZipPath = zipfile.ZipFile('C:/zip/solve.zip')

decryption(password_binding, 1, password_len, ZipPath)
os.system('pause')

while True:
    user_input = str(input("/exit을 입력하면 프로그램이 종료됩니다>"))
    if(user_input == "/exit"):
        break