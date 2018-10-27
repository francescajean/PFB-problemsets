#!/usr/bin/env python3

my_list2 = ['a','bb','ccc']

list_copy2 = my_list2.copy()#makes an actual copy of the first list

print(my_list2)#prints the original list

list_copy2.append('dddd')#changes only the copy of the list, not the original list

print(my_list2)#prints the original, unchanged list
