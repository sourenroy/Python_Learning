d = {} #Empty Dictionarie

marks = {
    "Souren" : 100,
    "Raj": 70,
    "Rahul":90
}

print(marks.items())
print(marks.keys())
print(marks.values())

marks.update({"Rahul":70, "Rimi": 99})
print(marks)

print(marks.get("Souren"))
