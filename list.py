kotta1=[22,44,55,78,"mm","op"]
kotta2=[78,8,"pp",3,"dolupapa",10,2]

# 22  0 k1 even
# 8   1 k2 odd
# 55  2 k1 even
# 3   3 k2 odd
# mm  4 k1 even
# 10  5 k2 odd
#hint : 22 % 2 = 0   , 23 % 2 =1

i=0
while(i<6):
    if(i % 2==0):
        print(kotta1[i])
    else:
        print(kotta2[i])
    i+=1














# i=0
# while(i<2):
#     print(i)
    # print(kotta1[i])
    # print(kotta2[i])
    # i+=1









#print(kotta1[2]+kotta2[3])

#print(str(kotta1[0])+kotta2[2])

#  "i love dolupapa at age 110"
# print("i love " + kotta2[4] +" at age "+ str(kotta1[2]*kotta2[-1]))
