# my_file= open("a.txt",'r')
# # y_file.write("Hi hello")
# print(my_file.readlines())
# my_file.close()

# with open('f1.txt','w') as f:
#     f.write("Hi file created")


# with open("f1.txt",'r') as fr:
#     print(fr.read())

# with open("f1.txt",'a') as fa:
#     fa.write("\nAppend the next line")

with open("f1.txt",'r+') as fr:
    fr.write("\nnext line")
    print(fr.read())
