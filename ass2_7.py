my_list = ['payal', 'kumari', 'section']
new_item = 'yadav'
after_item = 'kumari'
if after_item in my_list:
    index = my_list.index(after_item)
    my_list.insert(index + 1, new_item)
else:
    print(f"{after_item} not found in the list")

print(my_list)
