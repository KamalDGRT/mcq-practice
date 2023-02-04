"""
13. What is the output of the following addition (+) operator

a)
[10, 20, 30, 40]
[10, 20, 30, 40]

b)
[10, 20]
[10, 20, 30, 40]

c)
[10, 20, 10, 20]
[10, 20, 30, 40]

d)
[10, 20]
[30, 40]

"""

a = [10, 20]
b = a
b += [30, 40]
print(a)
print(b)
