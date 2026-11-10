data = {'red':'紅','green':'綠','blue':'藍'}
while True:
    word = input('text:')
    if word in data:
        print(data[word])
    else:
        print('Not found')
    break  #僅一次


data = {'red':'紅','green':'綠','blue':'藍'}
while True:
    word = input('text:')
    if word == 'exit':
        break
    if word in data:
        print(data[word])
    else:
        print('Not found')  #無數次


prices = {'apple': 20, 'banana': 15, 'orange': 25}
while True:
    w = input('which item:')
    if w == 'alr':
        break
    if w in prices:
        print(prices[w])
    else:
        print('No this one')
