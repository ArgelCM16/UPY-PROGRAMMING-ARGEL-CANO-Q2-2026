#Digito verificador

#INPUT
rol_completo = input("Ingrese el rol con su digito verificador (formato XXXXXXXXX-X): ")

#PROCESS
partes = rol_completo.split("-")

if len(partes) != 2:
    print("Rol inválido: No tiene el formato XXXXXXXXX-X")
else:
    rol = partes[0]
    digito_ingresado = partes[1]

    if not rol.isdigit():
        print("Los digitos del rol deben ser numéricos")
    elif not (digito_ingresado.isdigit() or digito_ingresado.upper() == "K"):
        print("El digito verificador debe ser numérico")
    else:
        rol_invertido = rol[::-1]
        multiplicadores = [2, 3, 4, 5, 6, 7]
        suma = 0
        for i in range(len(rol_invertido)):
            digito = int(rol_invertido[i])
            multiplicador = multiplicadores[i % len(multiplicadores)]
            suma += digito * multiplicador

        resto = suma % 11
        if resto == 0:
            digito_verificador = "0"
        elif resto == 1:
            digito_verificador = "K"
        else:
            digito_verificador = str(11 - resto)

        #OUTPUT
        if digito_ingresado.upper() != digito_verificador:
            print(f"Error: El dígito verificador no conicide, se esperaba {digito_verificador}")
        else:
            print(rol_completo)
