# Define a class
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def greet(self) -> str:
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

# Create an instance
person = Person("Alice", 25)
print(person.greet())
