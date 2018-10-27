#!usr/bin/env python3
import sys

value = int(sys.argv[1])

if value > 0:		
	message = 'Positive'
	print(value,message)
	if value < 50:
		message = 'Less than 50'
		print(message)
		if (value%2)==0:
			message = 'Less than 50 and even'
			print(message)
	elif value > 50:
		message = 'Greater than 50'
