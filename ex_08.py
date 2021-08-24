# 파일을 여는 코드
han = open('mbox-shots.txt')

# 루프를 실행
for line in han:
    # 공백을 지우는 코드
    line = line.rstrip()
    # 단어 단위로 분할하는 코드
    wds = line.split()
    # 리스트에서 0번째 위치의 단어가 From인지 확인하고
    # From이 아니면 진행, 맞으면 2번째 위치의 단어를 출력
    # 코드가 오류없이 작동하도록 하기 위해서 해당 줄의 단어가 3개 이하라면 진행하는 코드 추가
    if len(wds) < 3 or wds[0] != 'From':
        continue
    print(wds[2])
