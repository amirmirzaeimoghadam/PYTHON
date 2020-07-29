list_party=[]
for i in range(3):
       list_party.append(input('enter the names of three people you want to invite to the party='))
invite_more=input('Do you want to invite more?')
while (invite_more =='yes'):
    list_party.append(input('enter the names of  more people you want to invite to the party='))
    invite_more=input('Do you want to invite more?')
    
else:
    print(list_party)


name_in_list = input('plz type in one of the names on the list')
list_party.index(name_in_list)
question=input('Do you still want this person to come to the party?')
if (question == 'no'):
    list_party.remove(name_in_list)
print(list_party)    
                
