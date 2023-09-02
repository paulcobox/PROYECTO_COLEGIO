import sys
from controller.profesor import ProfesorController

def modulo_profesor():
    print("--------------------------------------------------------------------------------")
    print("MANTENIMIENTO DE PROFESORES")
    print("1: Crear profesor")
    print("2: Modificar profesor")
    print("3: Eliminar profesor")
    print("4: Consultar profesor")
    try:
        
        option = input(f"Ingrese el número de la opción que desea: ")
        print("--------------------------------------------------------------------------------")
        if (option=="1"):
            while True:
                crear_profesor()
                opc = continuar_mensaje('Registrando')
                if (opc=="1"):
                    continue
                elif (opc=="2"):
                    break
        elif (option=="2"):
            modificar_profesor()
        elif (option=="3"):
            eliminar_profesor()
        elif (option=="4"):
            consultar_profesor()
        else:
            print("Debe escoger una opción de la lista.")
            return modulo_profesor()
    except KeyboardInterrupt:
        print('\n')
        print("Proceso terminado.")
        sys.exit()
    except ValueError as e:
      print(f'Ocurrio un problema, solo debes ingresar números, vuelve a ingresar todos los datos')
      modulo_profesor()

def crear_profesor():
    profesorControler = ProfesorController()
    print("NUEVO PROFESOR")
    print("--------------------------------------------------------------------------------")
    nombre = input(f"Ingrese el Nombre del profesor: ")
    edad = int(input(f"Ingrese la edad del profesor: "))
    if( (0 > edad) or (edad >= 120)):
        print(f'Ocurrio un problema..¡¡¡¡, la edad ingresada debe de estar en el rango de  0 y 120 , vuelve a ingresar todos los datos ')
        modulo_profesor()
    correo = input(f"Ingrese el Correo del profesor: ")
    profesorControler.insert_profesor({
        "NOMBRE": nombre,
        "EDAD": edad,
        "CORREO": correo
    })

def modificar_profesor():
    profesorControler = ProfesorController()
    print("MODIFICAR PROFESOR")
    print("--------------------------------------------------------------------------------")
    print("PASO 1 : Seleccione el Profesor que desea Modificar")
    print("--------------------------------------------------------------------------------")
    profesorControler.list_profesores()
    print("----------------------------")
    id = input(f"Ingrese el ID del Profesor:  ")
    print("----------------------------")
    profesor_model = profesorControler.list_profesor(id)
    if(profesor_model == None):
        print("-------------------------------------------------------------")
        print(f"====>  EL PROFESOR DE ID {id} NO EXISTE, SELECCIONE OTRO ID <====")
        print("-------------------------------------------------------------")
        modificar_profesor()
    else:
        print("-------------------------------------------------------------------------------------------------")
        print("PROFESOR SELECCIONADO ( ID | NOMBRE | EDAD | CORREO ) : ", profesor_model)
        print("-------------------------------------------------------------------------------------------------")
    print("------------------------------------------")
    print("PASO 2 : Ingrese los Campos a Modificar")
    print("------------------------------------------")
    nombre = input(f"Ingrese el Nombre del Profesor: ")
    edad = int(input(f"Ingrese la edad del Profesor: "))
    if( (0 > edad) or (edad >= 120)):
        print(f'Ocurrio un problema..¡¡¡¡, la edad ingresada debe de estar en el rango de  0 y 120 , vuelve a ingresar todos los datos. ')
        modificar_profesor()
    correo = input(f"Ingrese el Correo del Profesor: ")
    profesorControler.update_profesor({"ID_PROFESOR" : id }, {
        "NOMBRE": nombre,
        "EDAD": edad,
        "CORREO": correo
    })


def eliminar_profesor():
    profesorControler = ProfesorController()
    print("ELIMINAR PROFESOR")
    print("--------------------------------------------------------------------------------")
    print("PASO 1 : Seleccione el Profesor que desea Eliminar")
    print("--------------------------------------------------------------------------------")
    profesorControler.list_profesores()
    print("----------------------------")
    id = input(f"Ingrese el ID del Profesor:  ")
    print("----------------------------")
    profesor_model = profesorControler.list_profesor(id)
    if(profesor_model == None):
        print("-------------------------------------------------------------")
        print(f"====>  EL PROFESOR DE ID {id} NO EXISTE, SELECCIONE OTRO ID <====")
        print("-------------------------------------------------------------")
        eliminar_profesor()
    else:
        print("-------------------------------------------------------------------------------------------------")
        print("PROFESOR SELECCIONADO ( ID | NOMBRE | EDAD | CORREO  ) : ", profesor_model)
        print("-------------------------------------------------------------------------------------------------")
    print("------------------------------------------")
    print("PASO 2 : Confirme Eliminacion")
    print("------------------------------------------")
    opc_eli = continuar_mensaje('con la eliminacion')
    if (opc_eli=="1"):
        profesorControler.delete_profesor({"ID_PROFESOR" : id })

def consultar_profesor():
    profesorControler = ProfesorController()
    print("CONSULTAR PROFESOR")
    print("--------------------------------------------------------------------------------")
    print("Ingrese el Nombre del Profesor que desea Consultar")
    print("--------------------------------------------------------------------------------")
    print("----------------------------")
    nombre = input(f"Ingrese el nombre del Profesor:  ")
    print("----------------------------")
    profesores_model = profesorControler.list_profesor_columns({'NOMBRE': nombre})

    if(profesores_model == []):
        print("-------------------------------------------------------------")
        print(f"====>  EL PROFESOR DE NOMBRE {nombre} NO EXISTE, INGRESE OTRO NOMBRE <====")
        print("-------------------------------------------------------------")
    else:
        print("-------------------------------------------------------------------------------------------------")
        print(f"====>  EL PROFESOR {nombre} ENCONTRADO  <====")
        print("( ID | NOMBRE | EDAD | CORREO  ) \n", profesores_model)
        print("-------------------------------------------------------------------------------------------------")
    opc_eli = continuar_mensaje('Consultando')
    if (opc_eli=="1"):
        consultar_profesor()
    

def continuar_mensaje(mensaje):
    print("--------------------------------------------------------------------------------")
    print(f"¿Desea Continuar {mensaje}?")
    print("1: Sí")
    print("2: No")
    opc = input(f"Ingrese el número de la opción que desea: ")
    if (opc=="1" or opc=="2"):
        return opc
    else:
        print("Debe escoger una opción de la lista.")
        continuar_mensaje(mensaje)

def ejecuta_modulo_profesor():
    while True:
        modulo_profesor()
        op_r = continuar_mensaje('con el Mantenimiento de Profesores ?')
        if (op_r=="2"):
            print("--------------------------------------------------------------------------------")
            print("SALIO DEL MODULO DE MANTENIMIENTO DE PROFESORES")
            print("--------------------------------------------------------------------------------")
            break

# ejecuta_modulo_profesor()