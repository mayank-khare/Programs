## Pangram

alphabets = 'abcdefghijklmnopqrstuvwxyz'
n=input()
li=[]
count=0
for val in n:
    if(val in alphabets and val not in li):
        count += 1
        #li.append(val)
if(count==26):
    print ("This is a Pangram")
else:
    print ("This is not a Pangram")