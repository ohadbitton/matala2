def revword(word:str):
        word=word[::-1]
        word=word.lower()
        return word


def countword ():
    file = open("text.txt") 
    for line in file:
        line=line.strip("\n")
        leadword=line
        break
        
    counter=1
    for line in file:
        line = line.strip("\n")
        if line==leadword: continue
        words = line.split()
        for j in words:
            revword(j)
            if  revword(j)==leadword :
                counter=counter+1              
    return counter    

