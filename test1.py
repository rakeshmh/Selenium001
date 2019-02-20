# def fi(name = 'Test'):
#     print("Hi",name)
#
# fi("rakesh")
# fi()


l=[1,2,3,('a','b','c'),4]

for i in l:
    if type(i) == tuple:
        continue
    else:
        print(i)