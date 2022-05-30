# set

my_set: set[str] = {'apple', 'aws', 'gcp', 'apple'}
my_set.add('micro')
print(my_set)
'''
my_set.discard('aws')
second_set: set[str] = {'iphone', 'gcp', 'aws'}
difference: set[str] = my_set.difference(second_set)
print(my_set.intersection(second_set))
print(my_set.union(second_set))
el = my_set.pop('aws') # remove the element going to return it
print(f'{my_set} ,,,,, pop = > {my_set}')
my_set.remove('gcp') # remove the element not going to return it
my_set.issuperset # does contain set
my_set.issubset # does contained in another set
'''
my_set.update({'test', 'aws'}) # combine sets
print(my_set)
''' 
# my map 
maps: dict[str: str] = {}

print(maps)

'''
