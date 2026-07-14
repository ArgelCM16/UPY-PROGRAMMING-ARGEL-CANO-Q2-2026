rol = input("Ingrese rol: ")

suma = 0
secuencia = 2

for numero in rol[::-1]:
    suma += int(numero) * secuencia
    secuencia += 1
    if secuencia == 8:
        secuencia = 2

modulo = suma % 11
resta = 11 - modulo

if resta == 11:
    dv = "0"
elif resta == 10:
    dv = "K"
else:
    dv = str(resta)

print(rol + "-" + dv)