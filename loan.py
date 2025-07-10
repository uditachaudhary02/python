owed=float(input('how much do you owe?\n'))
apr=float(input('what is apr?\n'))
payment=float(input('pay for a month?\n'))
months=int(input('how many months\n'))

month_rate=apr/100/12
for i in range(months):
    interest=month_rate*owed
    owed=owed+interest
    if(owed-payment<0):
        print('last payment',owed)
        print('paid off loan',i+1,'months')
        break
  owed=owed-payment

    print('paid',payment,'of which',interest,'was interset', end=' ')
    print('i owe',owed)