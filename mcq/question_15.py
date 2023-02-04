"""
15. What is the output of the following nested loop


a)
10 Chair
10 Table
20 Chair
20 Table

b)
10 Chair
10 Table

"""

numbers = [10, 20]
items = ["Chair", "Table"]

for number in numbers:
  for item in items:
    print(number, item)


"""
*
* *
* * *
* * * *
* * * * *
"""

"""
Iteration 1:
number = 10

item = Chair

10 Chair
10 Table
20 Chair
20 Table
"""