#Dictionary Data Type:
#Is a collection of many values which uses many different data types,
# not just integers. 
#Indexes for dictionaries are called keys,
#and a key with its associated value is called a key-value pair.

birthdays = {'Alice': 'Apr. 1', 'Bob': 'Dec 12', 'Carol': 'Mar. 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
   else:
        print('I do not have birthday information for ' + name)
       print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')

