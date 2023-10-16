import aplicacion as ap


def listar_persona(archivo1,archivo2,archivo3):
    dni = []
    nombre = []
    apellidos = []
    print("***REPORTE DE DATOS***")
    try:
        # DNI
        with open(archivo1, "r") as archivo1:
            # Itera a través de las líneas y muestra cada registro
            for linea in archivo1:
                dni.append(linea.strip())
                

        with open(archivo2, "r") as archivo2:
            # Itera a través de las líneas y muestra cada registro
            for linea in archivo2:
                nombre.append(linea.strip())     
                
        with open(archivo3, "r") as archivo3:
            # Itera a través de las líneas y muestra cada registro
            for linea in archivo3:
                apellidos.append(linea.strip()) 
                
        num = len(dni)
        
        for i in range(num):
            print(f"|{dni[i]}|\t\t{nombre[i]}\t\t|\t\t{apellidos[i]}\t\t|")

    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")
    
   
def agregar_persona():
    print("--AGREGAR PERSONA--")
    dni = input("\nIngrese dni: ")
    nombre = input("\nIngrese nombre: ")
    apellido = input("\nIngrese apellido: ")
    
    #DNI
    archivo1 = open("dni.txt","at")
    # \n es para agregar el contenido en una línea al final
    contenido1="\n"+dni

    archivo1.write(contenido1)

    archivo1.close()
    
    #NOMBRE
    archivo2 = open("nombre.txt","at")
    # \n es para agregar el contenido en una línea al final
    contenido2="\n"+nombre

    archivo2.write(contenido2)

    archivo2.close()
    
    #APELLIDO
    archivo3 = open("apellido.txt","at")
    # \n es para agregar el contenido en una línea al final
    contenido3="\n"+apellido

    archivo3.write(contenido3)

    archivo3.close()

def salir():
    print("Gracias por su visita....")


opcion = 1

while opcion!=3:
    ap.mostrar_menu()
    opcion = int(input("Ingrese opción: "))
    if opcion == 1:
        listar_persona("dni.txt","nombre.txt","apellido.txt")
    elif opcion == 2:
        agregar_persona()
    elif opcion == 3:
        salir()
    else:
        print("Opción no válida")
    






