# This is an app for creating and working with a dictionary.

my_dict = {
    'tuple': (56, 'something', None, 3.14, False, 0),
    'list': ['abc', 0, True, 57.2, 'def', 12],
    'dict': {'one': 'value', 'two': 'value2', 'three': 'value3', 'four': 'value4', 'five': 'value5', 'six': 'value6'},
    'set': {44, None, 6, 7.12, 'text', False}
}

last_element_tuple = my_dict['tuple'][-1]

last_element_tuple = str(last_element_tuple)

print('Last element tuple = ' + last_element_tuple)

print('=' * 125)

my_dict['list'].append(False)

my_dict['list'].pop(2)

my_dict['dict'][('i am a tuple',)] = 'valuetuple'

my_dict['dict'].pop('six')

my_dict['set'].add('moretext')

my_dict['set'].pop()

print('Entire dictionary:')

print("Tuple: " + str(my_dict['tuple']))

print("List: " + str(my_dict['list']))

print("Dict: " + str(my_dict['dict']))

print("Set: " + str(my_dict['set']))

print('=' * 125)
