'''numbers = [5, 2, 1, 5, 7, 4]
numbers2 = numbers.copy()
numbers.append(10)
print(numbers)
print(numbers2) '''

'''
Possible operations:

numbers.append(10), adds a new item to the list.
numbers.insert(0, 10), inserts a number in a specific index
numbers.remove(10), removes an items
numbers.clear(), deletes all the items in the list
numbers.pop(), removes the last item in a list
numbers.index(10), searchs the item in the list and returns the index of that item. 
If more than 1, returns the first one.
numbers.count(10), counts how many of those items are in the list
numbers.sort(), sorts the list, ascending
numbers.reverse(), reverses the items, descending
numbers2 = numbers.copy(), copies... duh.
'''


numbers = [1, 5, 5, 4, 7, 1, 8, 2, 7]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
