#!/usr/bin/env python3

nums = ['101','2','15','22','95','33','2','27','72','15','52']

#for x in nums: #this is good for the first part of 6
#	print(x)
	

#for x in nums:#this is good for the second part of 6
#	if int(x)%2==0:
#		print(x)

#sorted(nums)#beginning of 7
#sorted_nums = sorted(nums)
#for x in sorted_nums:
#	print(x)

#sorted(nums)
#sorted_nums = sorted(nums)
even = 0
odd = 0
for x in nums:
	if int(x)%2==0:
		even += int(x)
	else: 
		odd += int(x)
print("Sum of even numbers: ",even,'/nSum of odd numbers: ',odd)

		
