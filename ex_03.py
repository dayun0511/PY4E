hour = input("Enter Hours: ")
rate = input("Enter Rate: ")
// input 함수는 문자열 타입을 반환하는 함수이므로 float로 변환해주어야 한다.
pay = float(hour) * float(rate)
print("Pay:",pay)
