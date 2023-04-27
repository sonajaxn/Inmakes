#if there are errors we give-
try:
    a=5
    b=0
    print(a/b)
except:
    print("there is an error")
finally:
    print("done")
#finally is used nomatter whether there is error or not , it will get printed
