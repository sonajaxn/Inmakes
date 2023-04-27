#dictionary is represented by {} these brackets and contains key and value.
#duplication is not allowed

x={"chair":500,"table":450,42:"rain"}
x["veg"]=120
x.update({"sun":20})
print(x)

print(x["chair"])
#inorder to get the value printed type keyword as above ,x.pop("keyname")=remove
print(len(x))
#to know the length, here 3 values

for i in x:
    print(i)
for i in x.items():
    print(i)