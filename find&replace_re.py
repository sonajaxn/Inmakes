import re
str="hello , how are  you , hope u r fine"
pattern="hello"#the word u need to change
new=re.sub(pattern,"hey",str) #re.subformat ,"_" the word u need to replace
print(new)