program_tv = ['khandevane','dorehami','navad','football_120']
for i in program_tv:
    print(i)
name_add_program = input('plz enter your favorite tv program: ')
position_add_program=int(input('plz enter position your favorite tv program in list:  '))
program_tv.insert(position_add_program,name_add_program)
for i in program_tv:
    print(i)
                         
