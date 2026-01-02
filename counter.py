'''Counting the number of items that appear more than once'''

def unique_numbers(numbers):
    unique_num = 0

    for num in set(numbers):
        if numbers.count(num) > 1:
            unique_num += 1
    return unique_num
numbers = [1, 2, 3, 4, 2, 2, 4, 4, 1, 6, 7, 6]

result = unique_numbers(numbers)
print(f"The answer is: {result}")