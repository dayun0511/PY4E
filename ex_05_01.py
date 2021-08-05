number = 0
total = 0.0
# while 문: 반복 범위 없이 조건에 따라서 반복 수행 여부 결정
while True :
    stringvalue = input('Enter your number: ')
    # 'done'을 입력받을 경우 반복문을 빠져나온다.
    if stringvalue == 'done' :
        break
    # 입력값 예외처리를 통해 유요한 입력값인지 확인한다.      
    try :
        floatvalue = float(stringvalue)
    except :
        print('Invalid input')
        # 잘못된 값이 입력될 경우 코드 최상단으로 가게 만든다.
        continue
    # print(floatvalue)
    number = number + 1
    total = total + floatvalue

# print('ALL DONE')
print(total, number, total / number)
