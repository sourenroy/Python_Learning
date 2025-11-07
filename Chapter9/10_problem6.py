with open("log.txt") as f:
    content = f.read()

if ("python" in content):
    print("Yes! Python is Availavel")
else:
    print("No Python is not Present")