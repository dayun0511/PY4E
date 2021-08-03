hour = input("Enter Hours: ")
rate = input("Enter Rate: ")
#string 타입으로 입력받은 숫자를 float 타입으로 변환
fh = float(hour)
fr = float(rate)
#40시간을 초과할 경우 초과분에 대해 1.5배의 수당을 지급하는 경우를 조건문으로 작성
if fh > 40 :
    regular = fh * fr
    overtime = (fh - 40) * (fr * 0.5)
    pay = regular + overtime
else:
    pay = fh * fr
print("Pay:",pay)
