fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()

for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # get 메소드를 활용해 if/else 구문을 간결하게 표현하기
        # ex_09_02의 4줄(검색,생성,업데이트)를 1줄로 요약함
        di[w] = di.get(w,0) + 1

# 파일에서 가장 많이 등장하는 단어를 찾음 (최댓값을 찾는 반복문)
# 카운터의 모든 값이 양수이므로 초기 값을 음수로 정하는 것이 괜찮은 방법이다.
largest = -1
theword = None
for k,v in di.items():
    # print(k,v)
    if v > largest:
        largest = v
        theword = k
print(theword, largest)
