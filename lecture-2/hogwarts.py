students = ["Hermione", "Harry", "Ron", "Draco"]

print(students[0])

houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

#How to match students with houses? --> Use dict
students = {
    "Hermione": "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:
    print(student, students[student], sep = ", ")

#How to add more values to each key?
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep = ", ")