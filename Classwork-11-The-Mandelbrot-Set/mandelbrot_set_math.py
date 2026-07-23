# INPUT
try:
    with open("config.txt", "r") as archivo:
        lineas = archivo.readlines()
except FileNotFoundError:
    lineas = None
    print("No se encontró el archivo config.txt")

if lineas is not None:
    config = None
    try:
        config = {}
        for linea in lineas:
            linea = linea.strip()
            if not linea:
                continue
            clave, valor = linea.split("=")
            config[clave.strip()] = valor.strip()
    except ValueError:
        config = None
        print("El archivo de configuración está mal formado")

    if config is not None:
        parametros = None
        try:
            ancho = int(config["ancho"])
            alto = int(config["alto"])
            max_iter = int(config["max_iter"])
            real_min = float(config["real_min"])
            real_max = float(config["real_max"])
            imag_min = float(config["imag_min"])
            imag_max = float(config["imag_max"])
            parametros = (ancho, alto, max_iter, real_min, real_max, imag_min, imag_max)
        except KeyError as error:
            print(f"Falta el parámetro {error} en config.txt")
        except ValueError:
            print("\"ancho\" y \"alto\" deben ser números enteros")

        if parametros is not None:
            ancho, alto, max_iter, real_min, real_max, imag_min, imag_max = parametros

            # PROCESS
            with open("mandelbrot.csv", "w") as archivo:
                archivo.write("row,column,iterations\n")
                for fila in range(alto):
                    for columna in range(ancho):
                        x0 = real_min + (columna / ancho) * (real_max - real_min)
                        y0 = imag_min + (fila / alto) * (imag_max - imag_min)

                        zx, zy = 0.0, 0.0
                        iteracion = 0
                        while zx * zx + zy * zy <= 4 and iteracion < max_iter:
                            zx, zy = zx * zx - zy * zy + x0, 2 * zx * zy + y0
                            iteracion += 1

                        # OUTPUT
                        archivo.write(f"{fila},{columna},{iteracion}\n")

            print("mandelbrot.csv generado correctamente")
