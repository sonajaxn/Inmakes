import re
pattern="hey"
if re.match(pattern,"hey it was nice to meet you"):
    print("matches")
else:
    print("not match")