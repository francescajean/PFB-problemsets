#!/usr/bin/env python3

variable = "sapiens,erecertus,neanderthalensis"

print(variable)#print the string

variable.split(',')#split the string

print(variable.split(','))#print the split string

new_variable = variable.split(',')#renaming the split string as a new variable

print(new_variable)#printing the new variable

sorted(new_variable)#sorting the new variable in alphabetical order

print(sorted(new_variable))#printed in alphabetical order

non_num = sorted(new_variable)#made the alphabetical order a new variable

lengths = []#made a for loop to make a list of the number of length for each of the values in the original variable
for x in non_num:#for every item in the list
	lengths.append(len(x))#add the length of each item to the lengths list
sorted(lengths)#sort the lengths list so it is in numeric order
print(sorted(lengths))#print the sorted lengths list

sorted(new_variable,key=len)#sort the alphabetical list by the shortest word
print(sorted(new_variable,key=len))#print the list by shortest word






