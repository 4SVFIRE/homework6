my_dict = {'name' : 'Artem', 'year_of_birth' : 2003, 'number' : 84531237604}
print(my_dict)
print(my_dict.get('name'))
print(my_dict.get('surname'))
my_dict.update({'surname ' : 'Sapozhnikov',
                'year' : 2024})
my_dict.pop('number')
print(my_dict)

my_set = {1, 2, 3, 4, 5, 1, 2, 4, 5, 6, 'voice', 'voice', 'hello', False, False}
print(my_set)
my_set.add(7)
my_set.discard('voice')
print(my_set)
