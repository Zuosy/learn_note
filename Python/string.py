#!/usr/bin/python3

if __name__ == '__main__' :
  str1 = "'This is a string'"
  _fen_ge_xian = "\n--------hualide fengexian ---------\n"
  print("str1 = " + str1)
  print("str1.title() = " + str1.title())
  print("str1.upper() = " + str1.upper())
  print("str1.lower() = " + str1.lower())
  print(_fen_ge_xian)
  print(" - - string Pin Jie - - ")
  first_name = 'tom'
  last_name = 'cat'
  print("first_name = ", first_name, '', sep='\'')
  print("last_name = ", last_name, '', sep='\'')
  full_name = first_name + ' ' + last_name
  print("full_name = first_name + ' ' + last_name")
  print("full_name = ", full_name, '', sep='\'')

  print(_fen_ge_xian)

  print(str("string method").center(40, '-'))
  print("str.capitalize()")
  print(
"""@doc:
    str.capitalize() equal with follow operate:
    seq = 'to b or not 2b this is a question'
    result = seq[0].upper() + seq[1:].lower()
@return:
    str:'To b or not 2b this is a question'
""")

  print("\n")
  print("str.center(width[, fillchar]")
  print(
"""@doc:
    [fillchar] is only one char!
    str = "tom cat"
    result = str.center(30, '*')
    len(result) == 30
    result is '***********tom cat************'
@return:
    str:'***********tom cat************'
@???:
def center(_str, width, char):
  assert len(char) == 1 and type(char) == type('')
  if width <= len(_str):
    return _str
  lnum = (width - len(_str)) // 2
  rnum = width - len(_str) - lnum
  return lnum * char + _str + rnum * char
""")


  print("\n")
  print("str.count(sub, start = 0, end = len(string))")
  print(
"""@doc:
    return the number of substring in the range[start, end].
    hello = 'hello world'
    hello.count('l')
@return:
    int:3
@???:
def count(_str, sub, start = 0, end = -1):
  if end == -1:
    end = len(_str)
  counter = 0
  assert len(_str[start:end]) >= len(sub)
  for i in range(start, end):
    if _str[i:i+len(sub)] == sub:
      counter = counter + 1
  return counter
""")