nums=[1,2,3,4]
nums.sort()
product1=nums[-1]*nums[-2]*nums[-3]
product2=nums[0]*nums[1]*nums[-1]
if product1>product2:
  maximum=product1
else:
  maximum=product2
print("Maximum Product:",maximum)
