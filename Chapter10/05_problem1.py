class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
    
p = Programmer("Souren", 120000, 743372)
print(p.name, p.salary, p.pin)