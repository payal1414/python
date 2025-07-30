my_list = ['payal', 'yadav', 'section']
old_value = 'yadav'
new_value = 'kumari'

if old_value in my_list:
    index = my_list.index(old_value)
    my_list[index] = new_value
else:
    print(f"{old_value} not found in the list")

print(my_list)
