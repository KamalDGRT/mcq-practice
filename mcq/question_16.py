"""
16
What will be the output of the following code snippet?


a) 0 1 2  ... 15
b) infinite loop
c) 0 3 6 9 12 15
d) 0 3 6 9 12

"""


count = 0
while (True):
   if count % 3 == 0:
       print(count, end=" ")
   if (count > 15):
       break
   count += 1 # count = count + 1
