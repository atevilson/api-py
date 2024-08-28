from dataclasses import dataclass

@dataclass()
class Category:
    name: str
    email: str
    phone: str

print(Category('Atevilson', 'freitas.atevilson@gmail.com', '44999999999'))
