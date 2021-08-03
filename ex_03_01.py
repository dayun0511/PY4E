hour = input("Enter Hours: ")
rate = input("Enter Rate: ")
#string 타입으로 입력받은 숫자를 float 타입으로 변환
fh = float(hour)
fr = float(rate)
if fh > 40 :
    regular = fh * fr
    overtime = (fh - 40) * (fr * 0.5)
    pay = regular + overtime
else:
    pay = fh * fr
print("Pay:",pay)
