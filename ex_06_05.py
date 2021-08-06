str = 'X-DSPAM-Confidence: 0.8475'

#콜론의 위치를 묻는 코드
ipos = str.find(':')
print(ipos)

piece = str[ipos+1:]
print(piece)

value = float(piece)
print(value)
