
#La función recibe un número y devuelve la diferencia entre 17 y el número si es menor o igual a 17. Si es mayor, devuelve el doble de la diferencia

def funcion(number):
    if number <= 17:
        return 17 - number
    else:
        return (number - 17) * 2


print(funcion(19))  
print(funcion(35))  
print(funcion(4))  
