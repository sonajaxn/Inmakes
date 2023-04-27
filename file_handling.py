file=open("demo.txt",'r')
content=file.read()

print(content)
file.close()
#w=write, r=read,a=append file=variable name , file.readline= read only one line ,file.read(5)=will read only upto 5 bytes

box=open("trial.txt",'w')
box.write("this may work , yahoo")
box.close()
#write to read (what writes here got printed in the newly formed page.

box=open("trial.txt",'a')
box.write("this is addition of the words in same variable.")
box.close()