i=int(input('enter the total number of alphabet'))
asciidict=dict()
alpha=range(97,97+i)
for i in alpha:
        asciidict[chr(i)]=i
print(asciidict)
