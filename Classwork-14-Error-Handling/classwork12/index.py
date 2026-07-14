from PIL import Image

config = {}

archivo = open("config.txt", 'r')

for line in archivo:
    if "=" in line:
        key, value = line.strip().split("=")
        config[key] = float(value) if "." in value else int(value)

archivo.close()

# print(config)

with open("clase.csv", 'r') as data:
    datos = data.readlines()

alto = int(config["alto"])
ancho = int(config["ancho"])    
config["max_iter"] = int(config["max_iter"])

# Crear una imagen en blanco con el tamaño especificado en la configuración
img = Image.new('HSV', (ancho, alto))

datos.pop(0)  # Eliminar la primera línea (encabezado)

for dato in datos:
    fila, columna, iteraciones = map(int, dato.strip().split(","))

    brillo = 0 if iteraciones == config["max_iter"] else iteraciones * 255 // config["max_iter"]
    
    img.putpixel((columna, fila), (brillo, 255, 255))  # Usar el brillo calculado para el canal H

img_rgb = img.convert('RGB')  # Convertir la imagen de HSV a RGB
img_rgb.save("fractal.png")  # Guardar la imagen en formato PNG

print("done")