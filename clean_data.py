qa=[]
with open('qa.txt', 'r') as f:
    myNames = [line.strip() for line in f]

setlist = set(myNames)
newlist = list(setlist)
print(newlist)

with open('qa_limpo.txt', 'a+') as f:
    for name in newlist:
        f.write("{}\n".format(name))
