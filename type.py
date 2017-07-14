sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']
a = [sI,mI,bI,eI,spI,sS,mS,bS,eS,aL,mL,lL,eL,spL]
for item in a:
    if type(item)==int:
        if item>=100:
            print "That's a big number!"
        else:
            print "That's a small number!"
    if type(item)==str:
        if len(item)>=50:
            print "That's a long string!"
        else:
            print "That's a short string!"
    if type(item)==list:
        if len(item)>=10:
            print "That's a long list!"
        else:
            print "That's a short list!"
