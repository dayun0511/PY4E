fname = input('Enter File: ')
# 그냥 enter만 눌렀을 때 기본적으로 clown.txt 파일을 실행하도록 함
if len(fname) < 1 : fname = 'clown.txt'
# 파일을 연다
hand = open(fname)

di = dict()

# 파일을 읽음
for lin in hand:
    # 파일의 각 줄의 오른쪽 끝에 있는 개행문자를 삭제
    lin = lin.rstrip()
    # 이전에 작성한 코드를 확인하는 print(lin)을 추가하는 것도 좋은 방법이다
    # 파일의 각 줄을 단어로 분리하는 코드
    wds = lin.split()
    # print(wds)
    for w in wds:
        # 단어가 이미 dictionary에 있는 경우 1을 더한다.
        if w in di:
            di[w] = di[w] + 1
            print('**Existing**')
        # 단어가 dictionary에 존재하지 않는 경우 단어를 저장하고 1을 부여한다.
        else:
            di[w] = 1
            print('**New**')
        print(di[w])

print(di)
