import sys
from controller.alumno import AlumnoController

def modulo_alumnos():
    print("--------------------------------------------------------------------------------")
    print("MANTENIMIENTO DE ALUMNOS")
    print("1: Crear alumno")
    print("2: Modificar alumno")
    print("3: Eliminar alumno")
    print("4: Consultar alumno")
    try:
        
        option = input(f"Ingrese el número de la opción que desea: ")
        print("--------------------------------------------------------------------------------")
        if (option=="1"):
            while True:
                crear_alumno()
                opc = continuar_mensaje('Registrando')
                if (opc=="1"):
                    continue
                elif (opc=="2"):
                    break
        elif (option=="2"):
            modificar_alumno()
        elif (option=="3"):
            eliminar_alumno()
        elif (option=="4"):
            consultar_alumno()
        else:
            print("Debe escoger una opción de la lista.")
            return modulo_alumnos()
    except KeyboardInterrupt:
        print('\n')
        print("Proceso terminado.")
        sys.exit()
    except ValueError as e:
      print(f'Ocurrio un problema, solo debes ingresar números, vuelve a ingresar todos los datos')
      modulo_alumnos()

def crear_alumno():
    alumnoControler = AlumnoController()
    print("NUEVO ALUMNO")
    print("--------------------------------------------------------------------------------")
    nombre = input(f"Ingrese el Nombre del alumno: ")
    edad = int(input(f"Ingrese la edad del alumno: "))
    if( (0 > edad) or (edad >= 120)):
        print(f'Ocurrio un problema..¡¡¡¡, la edad ingresada debe de estar en el rango de  0 y 120 , vuelve a ingresar todos los datos ')
        modulo_alumnos()
    correo = input(f"Ingrese el Correo del alumno: ")
    alumnoControler.insert_alumno({
        "NOMBRE": nombre,
        "EDAD": edad,
        "CORREO": correo
    })

def modificar_alumno():
    alumnoControler = AlumnoController()
    print("MODIFICAR ALUMNO")
    print("--------------------------------------------------------------------------------")
    print("PASO 1 : Seleccione el ALumno que desea Modificar")
    print("--------------------------------------------------------------------------------")
    alumnoControler.list_alumnos()
    print("----------------------------")
    id = input(f"Ingrese el ID del Alumno:  ")
    print("----------------------------")
    alumno_model = alumnoControler.list_alumno(id)
    if(alumno_model == None):
        print("-------------------------------------------------------------")
        print(f"====>  EL ALUMNO DE ID {id} NO EXISTE, SELECCIONE OTRO ID <====")
        print("-------------------------------------------------------------")
        modificar_alumno()
    else:
        print("-------------------------------------------------------------------------------------------------")
        print("ALUMNO SELECCIONADO ( NOMBRE | EDAD | ID | CORREO ) : ", alumno_model)
        print("-------------------------------------------------------------------------------------------------")
    print("------------------------------------------")
    print("PASO 2 : Ingrese los Campos a Modificar")
    print("------------------------------------------")
    nombre = input(f"Ingrese el Nombre del Alumno: ")
    edad = int(input(f"Ingrese la edad del Alumno: "))
    if( (0 > edad) or (edad >= 120)):
        print(f'Ocurrio un problema..¡¡¡¡, la edad ingresada debe de estar en el rango de  0 y 120 , vuelve a ingresar todos los datos. ')
        modificar_alumno()
    correo = input(f"Ingrese el Correo del Alumno: ")
    alumnoControler.update_alumno({"ID_ALUMNO" : id }, {
        "NOMBRE": nombre,
        "EDAD": edad,
        "CORREO": correo
    })


def eliminar_alumno():
    alumnoControler = AlumnoController()
    print("ELIMINAR ALUMNO")
    print("--------------------------------------------------------------------------------")
    print("PASO 1 : Seleccione el ALumno que desea Eliminar")
    print("--------------------------------------------------------------------------------")
    alumnoControler.list_alumnos()
    print("----------------------------")
    id = input(f"Ingrese el ID del Alumno:  ")
    print("----------------------------")
    alumno_model = alumnoControler.list_alumno(id)
    if(alumno_model == None):
        print("-------------------------------------------------------------")
        print(f"====>  EL ALUMNO DE ID {id} NO EXISTE, SELECCIONE OTRO ID <====")
        print("-------------------------------------------------------------")
        eliminar_alumno()
    else:
        print("-------------------------------------------------------------------------------------------------")
        print("ALUMNO SELECCIONADO ( NOMBRE | EDAD | ID | CORREO ) : ", alumno_model)
        print("-------------------------------------------------------------------------------------------------")
    print("------------------------------------------")
    print("PASO 2 : Confirme Eliminacion")
    print("------------------------------------------")
    opc_eli = continuar_mensaje('con la eliminacion')
    if (opc_eli=="1"):
        alumnoControler.delete_alumno({"ID_ALUMNO" : id })

def consultar_alumno():
    alumnoControler = AlumnoController()
    print("CONSULTAR ALUMNO")
    print("--------------------------------------------------------------------------------")
    print("Ingrese el Nombre del ALumno que desea Consultar")
    print("--------------------------------------------------------------------------------")
    print("----------------------------")
    nombre = input(f"Ingrese el nombre del Alumno:  ")
    print("----------------------------")
    alumnos_model = alumnoControler.list_alumno_columns({'NOMBRE': nombre})

    if(alumnos_model == []):
        print("-------------------------------------------------------------")
        print(f"====>  EL ALUMNO DE NOMBRE {nombre} NO EXISTE, INGRESE OTRO NOMBRE <====")
        print("-------------------------------------------------------------")
    else:
        print("-------------------------------------------------------------------------------------------------")
        print(f"====>  EL ALUMNO {nombre} ENCONTRADO  <====")
        print("( NOMBRE | EDAD | ID | CORREO ) \n", alumnos_model)
        print("-------------------------------------------------------------------------------------------------")
    opc_eli = continuar_mensaje('Consultando')
    if (opc_eli=="1"):
        consultar_alumno()
    

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

def ejecuta_modulo_alumnos():
    while True:
        modulo_alumnos()
        op_r = continuar_mensaje('con el Mantenimiento de Alumnos ?')
        if (op_r=="2"):
            print("--------------------------------------------------------------------------------")
            print("SALIO DEL MODULO DE MANTENIMIENTO DE ALUMNOS")
            print("--------------------------------------------------------------------------------")
            break

# ejecuta_modulo_alumnos()