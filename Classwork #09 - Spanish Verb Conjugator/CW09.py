#INPUT
verbo = input("ingresa el verbo:")

#PROCESS
if verbo != verbo.strip():
    print("El verbo no debe tener espacios extra")
elif verbo != verbo.lower():
    print("El verbo debe escribirse en minúsculas")
else:
    #lista
    pronombres = ["Yo", "Tú", "Él", "Nosotros", "Vosotros", "Ellos"]
    #diccionario
    terminaciones = {
        "ar": ["o", "as", "a", "amos", "ais", "an"],
        "er": ["o", "es", "e", "emos", "eis", "en"],
        "ir": ["o", "es", "e", "imos", "is", "en"]
    }

    #sacar raiz del verbo (todo menos las ultimas dos letras) y el final (ultimas dos letras del verbo)
    #ejemplo: AMAR, RAIZ= AM, FINAL= AR
    raiz_delverbo = verbo[:-2]
    final_delverbo = verbo[-2:]

    #buscar sus respectivas terminaciones del verbo y guardarla en una lista
    try:
        finaldelverbo_lista = terminaciones[final_delverbo]
    except KeyError:
        print("El verbo debe terminar en ar, er o ir")
    else:
        #OUTPUT
        for index, pronombre in enumerate(pronombres):
            terminacion = finaldelverbo_lista[index]
            print(f"{pronombre} {raiz_delverbo}{terminacion}")
