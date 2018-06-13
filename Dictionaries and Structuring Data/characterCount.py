#Counts the number of occurrences of each letter in a string.

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
cout= {}

for character in message:
    cout.setdefault(character, 0)
    cout[character] = cout[character] + 1

print(cout)
