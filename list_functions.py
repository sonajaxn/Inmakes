fruits=["apple","orange","mango","cherry"]
fruits.append("mulberry")
#print(fruits)


fruits.insert(2,"lemon")
print(fruits)
print(len(fruits))
#print(fruits.index("lemon"))
#print(fruits.index("orange"))

fruits.remove("mango")
#print(fruits)

del  fruits[0]
print(fruits)