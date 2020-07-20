import random

length = int(input('How long will the password be?'))

choices = open('Choices.txt', 'r')
f = choices.readlines()

pw = open('password.txt', 'w')

choices_list = [] 
for line in f:
    if line[-1] == '\n':
        choices_list.append(line[:-1])
    else:
        choices_list.append(line)

for i in range(length):
    pw.write(random.choice(choices_list))

choices.close()
pw.close()

final_password = open('password.txt', 'r')
final_password = final_password.read()

print('Your password is', final_password)