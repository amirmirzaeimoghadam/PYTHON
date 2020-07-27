dict_food={}
for i in range(0,4):
    dict_food[i] = input("plz enter your favorite foods:")
print (dict_food)
food_del = input('Which one do you want to get rid of? ')
for i in range(0,4):
        if dict_food[i]== food_del :
           dict_food.pop(i)
print(dict_food)
