''' 윈도우에서 웹페이지를 저장하는 방법 ctrl + s
open은 파일을 여는 코드는 아니다
그러나 파일을 살펴볼 수 있도록 일종의 문을 만들어준다 '''

fh = open('mbox-short.txt')
# 파일을 읽기 위해서 for 루프를 사용한다.
for lx in fh :
    # 파일에 저장되어 있는 개행문자를 제거하는 코드
    ly = lx.rstrip()
    # 파일을 모두 대문자로 변경하여 출력한다.
    print(ly.upper())
