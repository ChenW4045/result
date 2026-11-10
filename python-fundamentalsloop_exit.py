scores = {'math':80,'english':90,'python':95}
while True:
  w = input('text:')
  if w == 'quit':
    print('bye')
    break
  if w in scores:
    print(scores[w])
  else:
    print('Subject not found')
