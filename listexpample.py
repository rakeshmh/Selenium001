
#Creatineg the list
l= ['q','w','r','t']
l1= [1,2,3,4]
#Print the list elements
print(l)

#print lenght of the list
print(len(l))

#Adding element to string
l.append("y")
print(l)
l.insert(2,'e')
print(l)
l.extend(l1)
print(l)

#Deleting the elemets from list

l.remove("y")
print(l)

l.pop()
print(l)

l.pop(1)
print(l)

del l[1]
print(l)

l.clear()
print(l)