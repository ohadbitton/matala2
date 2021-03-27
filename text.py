file = open("C:/Users/tuvs2/Desktop/pythonprograms/matala2/text.txt") 
def revword(word:str):
        newword=word[::-1]
        newword=newword.lower()
        return newword


def countword (file):
    for line in file:
        line=line.strip("\n")
        leadword=line
        break
        
    counter=1
    for line in file:
        line = line.strip("\n")
        if line==leadword:
	continue
        words = line.split()
        for j in words:
            revword(j)
            if  revword(j)==leadword :
                counter=counter+1              
    return counter    

