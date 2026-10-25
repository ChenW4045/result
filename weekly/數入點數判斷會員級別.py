points = int(input('請輸入你的會員點數：'))

if points >= 100:
    print('你的階級是：金牌會員')
elif points >= 50:
    print('你的階級是：銀牌會員')
else:
    print('你的階級是：一般會員')  #僅一次


while True:
    text = input('請輸入你的會員點數,或輸入quit以結束：')
    if text == 'quit':
        break
    try:
        points = int(text)
    except ValueError:
        print('請輸入正整數')
    else:
        if points < 0:
            print('點數不能小於 0')
        elif points >= 100:
            print('你的級別是：金牌會員')
        elif points >= 50:
            print('你的級別是：銀牌會員')
        else:
            print('你的級別是：一般會員')  #無數次
