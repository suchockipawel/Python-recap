
fruit_list: list = ['pulmengroundnuts', "apple", "bananna", "orange"]
name: str = "johndoe"
random_list: list = list(name) # converts anyother container to a list [string, tuple, dictionary]

# linear? yes
# mutable or immutable ? mutable

# concatenation
# print(random_list)
all_items: list = fruit_list + random_list

# repition
# print(fruit_list * 4)

# indexing
#print(fruit_list[-4])
# slicing
# print(fruit_list[-2:-1]) # -2(bananna),
# print(fruit_list[2:4]) # 2(bananna), 3(orange),
# print(fruit_list[2:]) # 2(bananna), 3(orange),
# size of list
#print(len(fruit_list))
#3 
# 4
#looping
# for x in fruit_list:
#     print(x)
# list_size = len(fruit_list)
# for x in range(list_size):
#     print(x)

# 'append', 'count', 'extend','insert', 
# 'pop', 'remove', 'reverse', 'sort'

# append add an item to a list
#print(fruit_list)
# "grapes*2" == "grapesgrapes"
# fruit_list.append("grapes"*2)
# fruit_list.append("grapes")
# fruit_list.append(600)
# fruit_list.append([2,70,100])
# print(fruit_list)

# list is mutable

# count, no of a specific item in a list
#print(fruit_list.count("grapes"))

#extend picks up a list of items and pours it into another list

# print(fruit_list)
# color_list: list = ["red", "green"]
# fruit_list.extend(color_list)
# print(fruit_list)

# insert is similar to append ,adds an item to a particular position
# print(fruit_list)
# fruit_list.insert(1, "random text")
# print(fruit_list)

# pop allows us to remove something from a list based on position
# print(fruit_list)
# fruit_list.pop()
# print(fruit_list)

# remove allows to remove something from a list
# print(fruit_list)
# fruit_list.remove("radio")
# print(fruit_list)
# sort, allows arrange items in an orderly manner
# print(new_list)
# new_list.sort()
# print(new_list)
# print(dir(fruit_list))

# packing and unpacking of items
# unpacking of items 
print(fruit_list)
# to unpack we use a combination of variables, * and =
# take out one item and leave the rest in a list
# one_item, *remaining_item = fruit_list
# print(one_item)
# print(remaining_item)
# first, second, *remaining = fruit_list
# print(first)
# print(second)
# print(remaining)
# item_1, *remaining, item_2 = fruit_list

item_1, item_2, item_3, item_4, *item_5 = "germany"
print(item_1)
print(item_2)
print(item_3)
print(item_4)
print(item_5)