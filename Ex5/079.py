nums = []

for i in range(3):
    n = int(input('enter the number: '))
    nums.append(n)
ans = input('Do you want to keep the last number you entered? :')
if ans == 'no':
    nums.pop(-1)
print(nums)
