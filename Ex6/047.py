number_1=int(input('plz enter first number:  '))
number_2=int(input('plz enter second number:  '))
result=number_1+number_2
question = input('type "y" if you want to add another number: ')
while question == 'y':
    number_other = int(input('plz enter other number: '))
    result+=number_other
    question = input('type "y" if you want to add another number: ')

print(result)
