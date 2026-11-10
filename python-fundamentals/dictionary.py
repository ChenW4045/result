data = {'a':1,'b':2,'c':3}
def w(e,f):
  try:
    return e[f]
  except KeyError:
    return 'Not found'
print(w(data,'a'))
print(w(data,'h'))


user_info = {'name':'alice','role':'admin'}
def w(e,f):
 try:
   return e[f]
 except KeyError:
  return 'No this one'
print(w(user_info,'name'))
print(w(user_info,'age'))


app_config = {'host':'localhost','port':8000}
def w(e,f):
    try:
        return e[f]
    except KeyError:
        return 'Default config'
print(w(app_config,'time'))
print(w(app_config,'port'))
