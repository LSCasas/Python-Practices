koders = [
    "Luis", "Antonio", "Marco", "Alexis", "Ana", "Martin"
]

edades = [
    15, 16, 20, 45, 61, 51
]

# Create a new list with tuples (name - age)
nueva_lista = [(koder, edad) for koder, edad in zip(koders, edades)]


#Create a new list, with tuples, but without the structure of a tuple
message = "Hola koders\nLa lista completa es:\n"
koder_ages = zip(koders, edades)
for pair in koder_ages:
    message += f"{pair[0]} - {pair[1]}\n"


# Print the output
print(nueva_lista)
print(message)
