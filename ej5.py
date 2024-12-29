#Solicita tres números, calcula su suma y, si todos son iguales, multiplica la suma por 3. Si no, muestra la suma normal.
def suma():
    suma_total = 0
    numeros = []

    for _ in range(3):
        numero = float(input("Dame un numero: "))
        numeros.append(numero)
        suma_total += numero

    if numeros[0] == numeros[1] == numeros[2]:
        print("La suma total multiplicada por 3 es: ", suma_total * 3)
    else:
        print("La suma total es: ", suma_total)

# Llamada a la función
suma()
