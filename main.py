# Створити змінні таких типів: string, integer, float, bool, list, dict, tuple, None

variable_string = "Michael"
variable_integer = 91
variable_float = 33.0
variable_bool = True
variable_list = [1, 2, 3, 4, 5, 6, 7]
variable_dict = {'name': 'Michael', 'age': 33, 'weight': 85, 'high': 185}
variable_tuple = (1, 2, 3, 4, 5, 6, 7)
variable_None = None

print(type(variable_string))
print(type(variable_integer))
print(type(variable_float))
print(type(variable_bool))
print(type(variable_list))
print(type(variable_dict))
print(type(variable_tuple))
print(type(variable_None))

# Використати вивчені оператори та порівняти між собою 
# числа, рядки, булеві значення, списки, словники і кортежі

num_1 = 3
num_2 = 7
num_3 = 14
string_1 = 'Michael'

print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_3)
print(num_1 / num_2)

print(num_1 > num_2)
print(num_1 < 10)
print(num_1 == num_3)
print(num_1 != string_1)

print(num_1 != num_2 and num_3 > num_1)
print(num_1 != num_2 or num_3 != num_1)
print('i' not in string_1)
print('M' in string_1)

# Використати вивчені функції Python:

# Робота з рядками:

# 1. Cтворити змінну num_str = 125, перевести її в тип string за допогою функції str()
num_str = 125
print(type(num_str))
num_str_1 = str(num_str)
print(type(num_str_1))

# 2. Cтворити зміну message = 'Hi, my name is Python!' 
# За допомогою функції replace() замінити усі букви 'y' на '0' та 'i' на '1'.
message = 'Hi, my name is Python!'
message = message.replace('y', '0')
message = message.replace('i', '1')
print(message)

# 3. Cтворити зміну split_test = 'This is a split test' 
# і розділити її по пробілах за допомогою функції split(), 
# а потім знову обʼєднати у строку за допомогою функції join() у змінну string_join
split_test = 'This is a split test'
result = split_test.split()
print(result)
string_join = " ".join(result)
print(string_join)

# 4. Визначити довжину рядку string_join за допомогою функції len()
string_join_length = len(string_join)
print(string_join_length)

# Робота зі списками:

#  1. Cтворити змінну list_append = [1, 2, 3] 
# і за допомогою функції append() додати туди спочатку 4, а потім 5
list_append = [1, 2, 3]
print(list_append)
list_append.append(4)
print(list_append)
list_append.append(5)
print(list_append)

# 2. Cтворити змінну list_extend = [4, 5, 6] 
# і розширити цей список іншим списком [7, 8, 9] за допомогою функції extend()
list_extend = [4, 5, 6]
list_extend.extend([7, 8, 9])
print(list_extend)

# 3. Визначити індекс елемента 6 у списку list_extend за допомогою функції index()
print(list_extend.index(6))

# 4. Визначити довжину списку list_append за допомогою функції len()
print(list_append)
print(len(list_append))

# Робота зі словниками:

# 1. Cтворити змінну dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'} 
# та вивести на екран дані, які знаходяться в ключах car та where
dict_test = {'car': 'Toyota', 'price': 4900, 'where': 'EU'}
print(dict_test.get('car'), dict_test.get('where'))

# 2. За допомогою функцій keys() і values() вивести на екран ключі та їх значення
print(dict_test.keys())
print(dict_test.values())

# 3. За допомогою функції items() вивести на екран пари ключ - значення
print(dict_test.items())