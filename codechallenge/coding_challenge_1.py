#SONA JAISON

movies=["kgf","avatar","murder mystery","half girlfriend","batman","colours","om shanti om","classmates"]
print("list of 8 movies : " + str(movies))

del movies[4]
print("after removing 5th movies : " + str(movies))

movies.insert(4,"LALJOS")
print("inserting director in 4th index position : " + str(movies))

print("printing out the movie elements :")
for i in movies:
    print(i)
print("4th element :" +movies[4])

movies.append("yeh jawani hei deewani")
print("additional movie :"+ str(movies))
