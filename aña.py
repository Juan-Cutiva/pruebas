import os
from print import lobby_image, final_image

def conversor(tipo_moneda, valor_dolar):
    os.system("cls")
    pesos = float(input("¿Cuántos " + tipo_moneda + " tienes?: "))
    dolares = pesos / valor_dolar
    dolares = str(round(dolares, 2))
    os.system("cls")    
    result = print("Tienes $" + dolares + " dólares" + final_image)
 

os.system("cls")
lobby_image = int(input(lobby_image))


if lobby_image == 1:
    conversor("Pesos Colombiano", 4856.92)
elif lobby_image == 2:
    conversor("Pesos Argentinos", 156.90)
elif lobby_image == 3:
    conversor("Pesos Mexicanos", 19.70)
elif lobby_image == 4:
    conversor("Euros", 1.01)
elif lobby_image == 5:
    conversor("Rublos Rusos", 62.05)
elif lobby_image == 6:
    conversor("Yenes Japones", 148.63)
else:
    print('Ingresa una opción correcta por favor')