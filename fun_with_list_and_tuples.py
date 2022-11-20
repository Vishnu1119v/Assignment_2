itm=int(input('enter the number of items'))
lst1=[]
for i in range(itm):
    a,b=map(int,input("Enter a multiple value: ").split(','))
    x=(a,b)
    lst1.append(x)
print('before sorting =',lst1)
for i in range(len(lst1)):
    for j in range(i+1,len(lst1)):
      if lst1[i][-1]>lst1[j][-1]:
        lst1[i],lst1[j]=lst1[j],lst1[i]
print('after sorting=',lst1)
# [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]