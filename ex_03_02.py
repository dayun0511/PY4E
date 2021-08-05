hour = input("Enter Hours: ")
rate = input("Enter Rate: ")
# 정상 여부 검사를 할 수 있는 예외처리 코드 작성하기
try:
    fh = float(hour)
    fr = float(rate)
except:
    print('Error, please enter numeric input')
    # 에러가 발생했을 경우 더 이상 코드를 실행하지 않고 끝내기
    quit()

if fh > 40 :
    regular = fh * fr
    overtime = (fh - 40) * (fr * 0.5)
    pay = regular + overtime
else:
    pay = fh * fr
print("Pay:",pay)
