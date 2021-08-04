# 시급계산 함수를 정의
def computepay(hours, rate) :
    # 함수 안의 매개변수 명을 유의할 것
    # print("In Computepay", hours, rate)
    if hours > 40 :
        regular = hours * rate
        overtime = (hours - 40) * (rate * 0.5)
        pay = regular + overtime
    else:
        pay = hours * rate
    # print("Returning", pay)
    # 여전히 함수 안에 있을 때 이 함수의 반환값을 의미한다.
    return pay

# 1) 먼저 입력값을 받아 string 타입을 float 타입으로 변환한다.
hour = input("Enter Hours: ")
rate = input("Enter Rate: ")
fh = float(hour)
fr = float(rate)

''' 2) computepay 함수를 호출하여 fh의 값을 hours로 전달, fr의 값을 rate로 전달한다.
pay 변수가 어떤 값이든 관계없이 xp에 할당된다'''

xp = computepay(fh, fr)

print("Pay:",xp)
