from PIL import Image

# INPUT
try:
    with open("config.txt", "r") as archivo:
        lineas_config = archivo.readlines()
except FileNotFoundError:
    lineas_config = None
    print("No se encontró el archivo config.txt")

if lineas_config is not None:
    config = {}
    for linea in lineas_config:
        linea = linea.strip()
        if not linea or "=" not in linea:
            continue
        clave, valor = linea.split("=", 1)
        config[clave.strip()] = valor.strip()

    ancho = int(config["ancho"])
    alto = int(config["alto"])
    max_iter = int(config["max_iter"])

    try:
        with open("mandelbrot.csv", "r") as archivo:
            lineas_csv = archivo.readlines()
    except FileNotFoundError:
        lineas_csv = None
        print("No se encontró el archivo mandelbrot.csv")

    if lineas_csv is not None:
        # PROCESS
        imagen = Image.new("L", (ancho, alto))

        try:
            for linea in lineas_csv[1:]:
                linea = linea.strip()
                if not linea:
                    continue
                campos = linea.split(",")
                fila = int(campos[0])
                columna = int(campos[1])
                iteraciones = int(campos[-1])

                if iteraciones >= max_iter:
                    brillo = 0
                else:
                    brillo = int(255 * iteraciones / max_iter)

                imagen.putpixel((columna, fila), brillo)

            # OUTPUT
            imagen.save("mandelbrot.png")
            print("mandelbrot.png generado correctamente")

        except IndexError:
            print("El archivo mandelbrot.csv no es consistente con el ancho/alto de config.txt")
        except ValueError:
            print("El archivo mandelbrot.csv está mal formado")
