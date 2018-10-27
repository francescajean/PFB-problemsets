#!/usr/bin/env python3

my_list = ['a','bb','ccc']

list_copy = my_list#makes list_copy and my_list equivalent

print(my_list)#prints the original list

list_copy.append('dddd')#appends the copied list but because they are equivalent, the original is also changed

print(my_list)
