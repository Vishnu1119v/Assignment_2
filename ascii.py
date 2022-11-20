alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
asciidict=dict()
alfapeTeller=range(97,123)
for i in alphabet:
    for j in alfapeTeller:
        asciidict[i]=j
print(asciidict)