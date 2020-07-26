n = int(input("jan jomle az fibo mikhay:"))
l1 =[]    
for i in range(0,n+1):
    

    def fibo(i):
         if (i==0):
            return 0
         elif (i== 1):
            return 1
         else:
             return fibo(i-1)+ fibo(i-2)


    l1.append(fibo(i))
print("jomalat fibo",l1)
    
