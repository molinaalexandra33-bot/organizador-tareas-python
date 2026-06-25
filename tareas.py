lista_de_tareas = []

def agregar_tarea():
    tarea = input("ingresa la tarea que deseas agregar:")
    print("tarea Agregada:", tarea)
    lista_de_tareas.append(tarea)
    return tarea

def contar_tareas(lista):
    return len(lista)

def mostrar_tareas(lista):
    print("tareas pendientes:")
    for tarea in lista:
        print(f"- {tarea}")

def marcar_completada(lista):
    tarea = input("ingresa la tarea que deseas marcar como completada:")
    if tarea in lista:
        lista.remove(tarea)
        print("tarea marcada como completada:", tarea)
    else:
        print("tarea no encontrada en la lista de tareas pendientes.")

while True: 
       
    print("bienvenido a tu lista de tareas")

    print("1.Agregar tarea ")

    print("2.Marcar tarea como completada ")

    print("3.Ver tareas pendientes ")

    print("4.salir")

    opciones= input("¿que opcion eliges?")

    if opciones == "1":
        agregar_tarea()

        
    elif opciones== "2": 
            marcar_completada(lista_de_tareas)

    elif opciones == "3":
            mostrar_tareas(lista_de_tareas)

    elif opciones == "4":
            print("Buen trabajo...")
            break
else:
    print("opcion no valida")
        