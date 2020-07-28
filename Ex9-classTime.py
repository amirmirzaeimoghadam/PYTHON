class Time:
    def __init__(self,hour,minitues,second):
        self.hour = hour
        self.minitues = minitues
        self.second = second
    def show(self):
        return str(self.hour)+":"+str(self.minitues)+":"+str(self.second)
    
    def __str__(self):
         return str(self.hour)+":"+str(self.minitues)+":"+str(self.second)


    def __repr__(self):
        return str(self.hour)+":"+str(self.minitues)+":"+str(self.second)

    def __add__(self,other):

          add_hour = self.hour + other.hour 
          add_minitues = self.minitues + other.minitues
          add_second = self.second + other.second
          if (add_second >= 60):
              add_second-=60
              add_minitues+=1
          if (add_minitues >=60):
              add_minitues-=60
              add_hour+=1

          return (str(add_hour)+":"+str(add_minitues)+":"+str(add_second))
        

    def __sub__(self,other):
          return str(self.hour-other.hour)+":"+str(self.minitues - other.minitues)+":"+str(self.second-other.second)


    
    def __lt__(self,other):
       second_finall_1 = self.second + self.minitues*60 + self.hour *3600
       second_finall_2 = other.second + other.minitues*60 + other.hour *3600
       if (second_finall_1 < second_finall_2):
           return True
       else:
           return False



    def __le__(self,other):
           second_finall_1 = self.second + self.minitues*60 + self.hour *3600
           second_finall_2 = other.second + other.minitues*60 + other.hour *3600
           if (second_finall_1 <= second_finall_2):
               return True
           else:
               return False



    def __gt__(self,other):
           second_finall_1 = self.second + self.minitues*60 + self.hour *3600
           second_finall_2 = other.second + other.minitues*60 + other.hour *3600
           if (second_finall_1 > second_finall_2):
               return True
           else:
               return False



    def __ge__(self,other):
           second_finall_1 = self.second + self.minitues*60 + self.hour *3600
           second_finall_2 = other.second + other.minitues*60 + other.hour *3600
           if (second_finall_1 >= second_finall_2):
               return True
           else:
               return False 
