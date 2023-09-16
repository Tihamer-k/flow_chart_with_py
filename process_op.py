entry = int(input("[1] de millas a km [2] de C° a Fahrenheit. Selecciona conversión a usar: "))
if entry == 1:
    miles = input("Ingrese valor en millas: ")
    mile = 1.60934
    miles_entry = float(miles)
    res = round(miles_entry * mile)
    print(f"El valor en kilómetros por hora es {res}.")
elif entry == 2:
    c = input("Ingrese valor en grados centígrados: ")
    # ºF = ºC x 1.8 + 32
    f = c * 1.8 + 32
    print(f"El valor en Fahrenheit es {f}.")
else:
    print("ERROR: Valor ingresado incorrecto, intenta nuevamente.")
