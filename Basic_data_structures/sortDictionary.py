import collections
dict1={100:20,89:10,90:10}
print(dict1.items())
result=sorted(dict1.items())
result=collections.OrderedDict(result)
print(result)