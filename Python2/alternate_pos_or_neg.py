#!/usr/bin/env python3
import sys

number = int(sys.argv[1])

if number > 0:
  print('Postive')
  if number < 50:
    print('Smaller than 50')
    if number%2==0:
      print('It is an even number that is smaller than 50')
elif number == 0:
  print('Equal to zero')
else:
  print('Negative')
