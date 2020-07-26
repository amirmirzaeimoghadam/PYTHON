
def taghvim(year , month, day):

    list_month = [31 , 28 ,31 , 30 , 31 ,30 , 31, 31 ,30 , 31, 30 , 31]
    
    kabiise = 0

    if  year % 4 != 0  and year % 400  == 0 :
        
           kabiise = 1
           
    elif year % 4 != 0  and year % 100  == 0 :
        
           kabiise = 0       
            
    else:
           kabiise = 1
             



    

    if kabiise == 1:
      list_month[1] =  29


            
    ruz = sum(list_month[:month -1]) + day
    return (ruz ,'omin ruze sal')
