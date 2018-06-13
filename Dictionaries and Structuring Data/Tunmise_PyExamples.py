#automate example 1

#birthdays = {'Alice': 'Apr. 1', 'Bob': 'Dec 12', 'Carol': 'Mar. 4'}

#while True:
#    print('Enter a name: (blank to quit)')
#    name = input()
#    if name == '':
#        break

#    if name in birthdays:
#        print(birthdays[name] + ' is the birthday of ' + name)
#   else:
#        print('I do not have birthday information for ' + name)
#       print('What is their birthday?')
#        bday = input()
#        birthdays[name] = bday
#        print('Birthday database updated.')
######################################################
#automate example 2

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
cout= {}

for character in message:
    cout.setdefault(character, 0)
    cout[character] = cout[character] + 1

print(cout)
    
