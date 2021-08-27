fname = input('Enter File: ')
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)

di = dict()


for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # get 메소드를 활용해 if/else 구문을 간결하게 표현하기
        oldcount = di.get(w,0)
        print(w,'old',oldcount)
        newcount = oldcount + 1
        di[w] = newcount
        print(w,'new',newcount)
