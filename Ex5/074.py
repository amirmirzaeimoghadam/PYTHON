list_colour = ['zard','nili','meshki','sefid','narenji','banafsh','keremi','ghermez','sabz','abi']
one_num = int(input("lotfan yek adad bein 0 ta 4 vared kon"))
two_num = int(input("lotfan yekadad bein 5 ta 9 vard konid"))
list_colour2 = []
for i in range(one_num , two_num+1):
    list_colour2.append(list_colour[i])
print (list_colour2)    
