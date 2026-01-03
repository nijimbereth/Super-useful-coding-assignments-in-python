#Selecting students living in the same city, using filter()

students = [
    {"name": "Enock", "house": "Edewecht"},
    {"name": "Erick", "house":"Bad Zwichenahn"},
    {"name": "John", "house": "Oldenburg"},
    {"name": "Peter", "house": "Oldenburg"},
    {"name": "Mwamba", "house": "Bad Zwischenahn"},
    {"name": "Thomas", "house": "Bremen"}
]

def is_in_Oldenburg(n):
    return n["house"] == "Oldenburg"

Oldenburgs = filter(is_in_Oldenburg, students)

for oldenburg in sorted(Oldenburgs, key=lambda s: s["name"], reverse=False):
    print(f'{oldenburg["name"]} lives in {oldenburg["house"]}')
