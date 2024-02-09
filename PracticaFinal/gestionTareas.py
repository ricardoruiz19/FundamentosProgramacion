#Programa que permite gestionar una lista de tareas pendientes. El usuario puede agregar, eliminar y listar tareas.
#Autor: Ricardo Ruiz Cortés
#Fecha: 09 febrero 2024
#Versión: 1.0


tareas = []

def agregar_tarea():
    tarea = input("Ingrese la nueva tarea: ")
    tareas.append(tarea)
    print("Tarea agregada correctamente.")

def eliminar_tarea():
    tarea = input("Ingrese la tarea a eliminar: ")
    if tarea in tareas:
        tareas.remove(tarea)
        print("Tarea eliminada correctamente.")
    else:
        print("La tarea no existe.")

def listar_tareas():
    print("Tareas pendientes:")
    for i, tarea in enumerate(tareas, 1):
        print(f"{i}. {tarea}")

while True:
    print("\n1. Agregar tarea")
    print("2. Eliminar tarea")
    print("3. Listar tareas")
    print("4. Salir")

    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        agregar_tarea()
    elif opcion == 2:
        eliminar_tarea()
    elif opcion == 3:
        listar_tareas()
    elif opcion == 4:
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
