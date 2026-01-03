#important exercise for printing a selected set of elements

students = [
    {"name": "Enock", "house": "Edewecht"},
    {"name": "Erick", "house":"Bad Zwichenahn"},
    {"name": "John", "house": "Oldenburg"},
    {"name": "Peter", "house": "Oldenburg"},
    {"name": "Mwamba", "house": "Bad Zwischenahn"},
    {"name": "Thomas", "house": "Bremen"}
]


Oldenburgs = [student["name"] for student in students if student["house"] == "Oldenburg"]

print("Students living in Oldenburg are:")
for oldenburg in sorted(Oldenburgs, reverse=False):
    print(oldenburg)
