#!/usr/bin/python3

import base64


if __name__ == '__main__':
  str = "this is string example....wow!!!"
  str = base64.b64encode(str.encode('utf-8', errors = 'strictttttt'))
  
  print(str)
