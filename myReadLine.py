buff= ""
lBuff= ""
nextChar = 0
limit = 0
lLimit = 0
nextLine = 0

def getChar():
    
    global nextChar
    global limit
    global buff
    if(nextChar==limit):
        nextChar = 0
        buffByte = os.read(0,1000)
        print("after read")
        buff=str(buffByte, 'utf-8')
        limit=len(buff)
        if(limit==0):
            return 0
    c=buff[nextChar]
    if(c=="\n"):
        limit=0
        buff=""
        nextChar=0
        return -1
    else:
        nextChar+=1
        return c

def getLine():
    line=""
    c=getChar()
    
    while(c!=0 and c != -1 ):
        line += c
        c=getChar()
    if(len(line)>0):
        return line
    else:
        return "0"

print(readline())
