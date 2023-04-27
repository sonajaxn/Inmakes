file=open("fileprogram.txt",'r')
content=file.read()
print(content)
file.close()

file=open("fileprogram.txt",'w')
file.write(" this is it")
file.close()


file=open("fileprogram.txt",'a')
file.write("I am fine .")
file.close()