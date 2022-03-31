string1 = 'spam/ '
string2 = 'eggs'
concat_string = string1 + string2
print(len(concat_string))

print(concat_string[::-1])

print(concat_string.find('ddam'))
print(concat_string.find('ddam'))
print("test branch")


print(concat_string.split('/'))

array_string = concat_string.split('/')
print("+".join(array_string))


first_name = 'Victor'
last_name = 'Petrov'
new_string = f'Hello, {first_name} {last_name}'
print(new_string)