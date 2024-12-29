#Bucle infinito para pedir nombre
names = []
while True:
    name =input('ingresa un nombre: ')
    if name == "":
        break

    names.append(name)

    print(names)
    print(tuple(names))
    print(set(names))