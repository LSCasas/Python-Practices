class User:
    race = "Human"

    def __init__(self, username, name, last_name, password="123"):
        self.username = username
        self.name = name
        self.last_name = last_name
        self.password = password

    def saludar(self):
        print(f"Hola, mi nombre es: {self.name}")

# class: PascalCase
# vars: snake_case
# const: UPPER_CASE

# Instancias de User
alfredo = User("alfredo123", "Alfredo", "Altamirano")
francisco = User("francisco123", "Francisco", "Rivera")

print(alfredo.name, alfredo.race)
print(francisco.name, francisco.race)
