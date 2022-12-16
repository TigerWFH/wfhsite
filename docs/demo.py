class Person(object):
    name = 'default'
    age = 'default age'
    def __init__(self, name):
        self.name = name

p = Person('monkey')
print(p.name)
print(p.age)
print(Person.name)
print(Person.age)