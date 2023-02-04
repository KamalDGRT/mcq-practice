"""
19
What will be the output of the following code snippet?

a) {'first': 'sunday', 'second': 'monday', 1: 3, 2: 4}
b) {'first': 'sunday', 'second': 'monday'}
c) {1: 3, 2: 4}
d) None of the above


"""

dict1 = {'first' : 'sunday', 'second' : 'monday'}
dict2 = {1: 3, 2: 4}
dict3 = {"prime" : [2, 3, 5, 7]}
dict4 = {"names" : {"firstName": "kamal", "lastName": "sharma","friendName": "prathik"}}
dict1.update(dict2)
dict1.update(dict3)
dict1.update(dict4)
print(dict1)
