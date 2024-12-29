#Solicita nombres hasta recibir uno vacío. Luego muestra una lista, tupla y conjunto con los nombres, eliminando duplicados en el conjunto.
continuar = True
lista = []

while continuar:
    nombre = input('Ingresa el nombre')
    if nombre == "":
        continuar = False
    else:
        lista.append(nombre)

        tupla = tuple(lista)
        mi_set = set(lista)


        print("Lista: ", lista, "tupla: ", tupla, "set: ", mi_set)