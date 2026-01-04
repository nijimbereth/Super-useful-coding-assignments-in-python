#Removing duplicates in a list

def unique_numbers(n):
    unique_items = []

    for item in n:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items

numbers = [1, 1, 2, 3, 4, 3, 4, 4, 5, 5, 6, 7, 7,]

result = unique_numbers(numbers)
print(result)