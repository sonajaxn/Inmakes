#used to convert complex codes to simple one.,uses square bracket

set=[i for i in "inmakes"]
print(set)

box=[i for i in "variables"]
print(box)
# to show words with same initial letters
y=["hi","helo","ok","done","deal"]
new=[]
for i in y:
    if 'h' in i:
        new.append(i)
       #simple way-
print(new)
new1=[i.upper() for i in y if 'd'in i]  #.upper= capital
print(new1)
