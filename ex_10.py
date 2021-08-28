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

# di.items = 키(Key)와 값(Value)의 쌍을 (키,값)처럼 튜플 형태로 변환
# sorted 함수를 사용해 튜플의 순서에 따라 정렬(기본 오름차순)
# x = sorted(di.items())

# 튜플을 이용해 단어의 빈도 수를 알아보기
# 1. 리스트 생성
tmp = list()
for k,v in di.items():
    # 2. (값,키)의 순서를 가진 튜플 생성
    newtuple = (v,k)
    tmp.append(newtuple)

# 오름차순(값이 작은 순서대로)정렬되기 때문에 매개변수에 reverse를 넣어 내림차순으로 정렬
tmp = sorted(tmp, reverse = True)
# 상위 5개만 출력
# print('Sorted', tmp[:5])
# 출력문이 보기 좋도록 다시 (키,값)의 순서로 바꿔준다.
for v,k in tmp[:5]:
    print(k,v)
