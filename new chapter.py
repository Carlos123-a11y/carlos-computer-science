counts={}#create a dictionary
counts2 = dict({})#creat a dictionary
counts3 = dict()
print(counts)
print(counts2)
#to add a key value pair
counts['games'] = 24
print(counts)
counts['players'] = 200
print(counts)
#tp check if the number of items in a dictionary
print(len(counts))
#to check if a key is in a dictioanary
if 'players' in counts:#boolean check
    print('players not found')
if 'managers' not in counts :#returns true or false
    print('managers not found')
#to print a  value
print(counts['games'])#returns games value-error
print(counts)
print(counts.get('games'))#returns game value
print(counts)
print(counts.pop('games'))
print(counts)

for key in counts.keys():
    print(key)
for key in counts:#will print keyts in the dictionary
    print(key)
for values in counts:#will prin the values
    print(values)
for key,value in counts.values():#will print the values
    print(f'{key}--{value}')
