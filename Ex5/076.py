list_party=[]
for i in range(3):
       list_party.append(input('enter the names of three people you want to invite to the party='))
invite_more=input('Do you want to invite more?')
while (invite_more =='yes'):
    list_party.append(input('enter the names of  more people you want to invite to the party='))
    invite_more=input('Do you want to invite more?')
    
else:
    print(len(list_party))
