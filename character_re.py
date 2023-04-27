import re
pattern="[a-z][0-9][A-Z]"
if re.search(pattern,"j7A"):
    print("matches")
else:
    print("not match")
