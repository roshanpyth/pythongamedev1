sentance=input("Please enter a sentance")
alphabet=set()
for i in sentance:
    if i.isalpha():
        alphabet.add(i)
#isalpha is used as a scanner (used to see if given character is in alpahbet( thats why we used )

if len(alphabet)==26:
    print("This is a panogram")
else:
    print("This is not a panogram")