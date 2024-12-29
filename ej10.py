#Ask the user for a number and verify that that number is even or odd

def verif_number(number):
    """
    Prompts the user for a number and checks if it's even or odd.
    """
    number = float(input("Dame el numero: "))
    if number % 2 == 0:
        print("Tu numero es par")
    else:
        print("Tu numero es inpar")



verif_number(20)