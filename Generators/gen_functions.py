# returns generator object which is lazy loading 
# used in processing large data sets because generator object only holds the current state of the object
# 
def gen_obj1(num):
    for i in range(num):
        if i%2==0:
            yield i

print(iter(gen_obj1(20)))

# generator objects 
gen_object=(num**2 for num in range(10))

def fibanacci_gen(num):
    def fibonacci_num(input,dict):
        if input in dict:
            print(dict[input])
            return dict[input]
        if input<=1:
            return 1
        else:
            dict[input]=fibonacci_num(input-1,dict)+fibonacci_num(input-2,dict)
            return dict[input]
    dict1=dict()
    for i in range(num):
        yield fibonacci_num(i,dict1)


print(list(fibanacci_gen(20)))
