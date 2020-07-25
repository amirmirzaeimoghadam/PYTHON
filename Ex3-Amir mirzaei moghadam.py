year = int (input ("plz entsr your year="))
month = int (input ("plz entsr your month="))
day = int (input ("plz entsr your day="))
kabiise = 0

if  year % 4 != 0 :
    print("your year is not kabisse")
    

else :
     if year % 400  == 0 :
        print("your year is kabisse")
        kabiise = 1
    
     elif year % 100 == 0 :
        print("your year is not kabisse")


     else  :
          print("your year is kabisse")
          kabiise = 1
         

      
   
list_month = [31 , 28 ,31 , 30 , 31 ,30 , 31, 31 ,30 , 31, 30 , 31]

if kabiise == 1:
    list_month[1] =  29

    
ruz = sum(list_month[:month -1]) + day
print (ruz , 'omin ruze sal')
