#using map() method to apply action on all the items of a list or list of dictionaries

students = [
    {"name": "Enock", "house": "Oldenburg"},
    {"name": "Erick", "house":"Bad Zwichenahn"},
    {"name": "John", "house": "Oldenburg"},
    {"name": "Peter", "house": "Oldenburg"},
    {"name": "Mwamba", "house": "Bad Zwischenahn"},
    {"name": "Thomas", "house": "Bremen"}
]

new_student = list(map(lambda s:{**s, "name":"Thierry"}, students))

print("The list where all names are replaced by 'Thierry'")
for s in new_student:
    print(s)