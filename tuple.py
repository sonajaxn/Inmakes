x=(115,28,"helo","tuple")
print(type(x))
#unchangable , no editing
#duplicatable

print(x[0])
#tuple to list inorder to edit(add , remove etc)
y=list(x)
print(y)
y.insert(2,"its ok")
print(y)
#reconversion from list to tuple
x=tuple(y)
print(x)

c=tuple(("hh","ll","oo"))  #tuple creation
print(c)
for i in c:
    print(i)

print(x+c)
print(x*2)#repeat
