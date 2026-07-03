config = {}

# 1. Leer el archivo de forma segura (previniendo líneas en blanco)
with open("config.txt", 'r') as archivo:
    for linea in archivo:
        if "=" in linea:
            clave, valor = linea.strip().split("=")
            config[clave] = float(valor)

# Mostrar la configuración leída
for clave, valor in config.items():
    print(f"{clave}={valor}")
    
# Pasar a enteros
ancho = int(config["ancho"])
alto = int(config["alto"])
max_iter = int(config["max_iter"])

# 2. Manejo de archivo con 'with open' para cierre automático
with open("clase.csv", 'w') as salida:
    salida.write("fila,columna,iteraciones\n")
    
    # Mapear enteros a pixel
    for fila in range(alto):
        for columna in range(ancho):
            
            # Cálculo de los números complejos (eje X e Y)
            real = config["real_min"] + (columna / ancho) * (config["real_max"] - config["real_min"])
            
            # 3. CORRECCIÓN: Aquí estabas usando 'columna/ancho', debe ser 'fila/alto'
            imag = config["imag_min"] + (fila / alto) * (config["imag_max"] - config["imag_min"])
            
            c = complex(real, imag)
            z = 0 + 0j
            iteraciones = 0
            
            # Cálculo del fractal
            while (abs(z) <= 2) and (iteraciones < max_iter):
                z = z * z + c
                iteraciones += 1
                
            # 4. CORRECCIÓN: Te faltaba guardar los datos en el CSV por cada pixel
            salida.write(f"{fila},{columna},{iteraciones}\n")

print("DONE")