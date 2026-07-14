import random

#Crear CSV
archivo=open("archivo.csv","w")

#Encabezados
archivo.write("x,y, COLOR\n")

for _ in range (10_000): #cuando la ariable auxiliar no se usa en loop usamos _ 
    x=random.uniform(-10,10)
    y=random.uniform(-10,10) #uniform es para que sea de forma uniorme o lo mas amplio posible
    
    distancia=(x*x + y*y)** 0.5
    iteraciones = 0
    color = 0
    
    while (distancia < 1) and (iteraciones <100):
        distancia = distancia * distancia
        iteraciones+= 1
        
    if distancia > 1 :
        color=255
    
    archivo.write(f"{x},{y}, {color}\n")
archivo.close()
print("Done")