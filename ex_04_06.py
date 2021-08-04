def computepay(hours, rate) :
    # print("In Computepay", hours, rate)
    if hours > 40 :
        regular = hours * rate
        overtime = (hours - 40) * (rate * 0.5)
        pay = regular + overtime
    else:
        pay = hours * rate
    # print("Returning", pay)
    return pay

hour = input("Enter Hours: ")
rate = input("Enter Rate: ")
fh = float(hour)
fr = float(rate)

xp = computepay(fh, fr)

print("Pay:",xp)
