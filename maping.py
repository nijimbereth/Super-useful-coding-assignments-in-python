#creating a function that applies an action to all elements of a list
#using filter() method

students = [
    {"name": "Enock", "house": "Edewecht"},
    {"name": "Erick", "house":"Bad Zwichenahn"},
    {"name": "John", "house": "Oldenburg"},
    {"name": "Peter", "house": "Oldenburg"},
    {"name": "Mwamba", "house": "Bad Zwischenahn"},
    {"name": "Thomas", "house": "Bremen"}
]


Oldenburgs = [student["name"] for student in students if student["house"] == "Oldenburg"]

for oldenburg in sorted(Oldenburgs, reverse=False):
    print(oldenburg)
