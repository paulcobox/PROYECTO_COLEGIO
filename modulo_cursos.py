import sys
from controller.curso import CursoController

def modulo_curso():
    print("--------------------------------------------------------------------------------")
    print("MANTENIMIENTO DE CURSOS")
    print("1: Crear curso")
    print("2: Modificar curso")
    print("3: Eliminar curso")
    print("4: Consultar curso")
    try:
        
        option = input(f"Ingrese el número de la opción que desea: ")
        print("--------------------------------------------------------------------------------")
        if (option=="1"):
            while True:
                crear_curso()
                opc = continuar_mensaje('Registrando')
                if (opc=="1"):
                    continue
                elif (opc=="2"):
                    break
        elif (option=="2"):
            modificar_curso()
        elif (option=="3"):
            eliminar_curso()
        elif (option=="4"):
            consultar_curso()
        else:
            print("Debe escoger una opción de la lista.")
            return modulo_curso()
    except KeyboardInterrupt:
        print('\n')
        print("Proceso terminado.")
        sys.exit()
    except ValueError as e:
      print(f'Ocurrio un problema, solo debes ingresar números, vuelve a ingresar todos los datos')
      modulo_profesor()

def crear_curso():
    cursoControler = CursoController()
    print("NUEVO CURSO")
    print("--------------------------------------------------------------------------------")
    nombre = input(f"Ingrese el Nombre del curso: ")
    cursoControler.insert_curso({
        "NOMBRE": nombre
    })

def modificar_curso():
    cursoControler = CursoController()
    print("MODIFICAR CURSO")
    print("--------------------------------------------------------------------------------")
    print("PASO 1 : Seleccione el Curso que desea Modificar")
    print("--------------------------------------------------------------------------------")
    cursoControler.list_cursos()
    print("----------------------------")
    id = input(f"Ingrese el ID del Curso:  ")
    print("----------------------------")
    curso_model = cursoControler.list_curso(id)
    if(curso_model == None):
        print("-------------------------------------------------------------")
        print(f"====>  EL CURSO DE ID {id} NO EXISTE, SELECCIONE OTRO ID <====")
        print("-------------------------------------------------------------")
        modificar_curso()
    else:
        print("-------------------------------------------------------------------------------------------------")
        print("CURSO SELECCIONADO ( ID | NOMBRE) : ", curso_model)
        print("-------------------------------------------------------------------------------------------------")
    print("------------------------------------------")
    print("PASO 2 : Ingrese los Campos a Modificar")
    print("------------------------------------------")
    nombre = input(f"Ingrese el Nombre del Curso: ")
    cursoControler.update_curso({"ID_CURSO" : id }, {
        "NOMBRE": nombre
    })


def eliminar_curso():
    cursoControler = CursoController()
    print("ELIMINAR CURSO")
    print("--------------------------------------------------------------------------------")
    print("PASO 1 : Seleccione el Curso que desea Eliminar")
    print("--------------------------------------------------------------------------------")
    cursoControler.list_cursos()
    print("----------------------------")
    id = input(f"Ingrese el ID del Curso:  ")
    print("----------------------------")
    curso_model = cursoControler.list_curso(id)
    if(curso_model == None):
        print("-------------------------------------------------------------")
        print(f"====>  EL CURSO DE ID {id} NO EXISTE, SELECCIONE OTRO ID <====")
        print("-------------------------------------------------------------")
        eliminar_curso()
    else:
        print("-------------------------------------------------------------------------------------------------")
        print("CURSO SELECCIONADO ( ID | NOMBRE ) : ", curso_model)
        print("-------------------------------------------------------------------------------------------------")
    print("------------------------------------------")
    print("PASO 2 : Confirme Eliminacion")
    print("------------------------------------------")
    opc_eli = continuar_mensaje('con la eliminacion')
    if (opc_eli=="1"):
        cursoControler.delete_curso({"ID_CURSO" : id })

def consultar_curso():
    cursoControler = CursoController()
    print("CONSULTAR CURSO")
    print("--------------------------------------------------------------------------------")
    print("Ingrese el Nombre del Curso que desea Consultar")
    print("--------------------------------------------------------------------------------")
    print("----------------------------")
    nombre = input(f"Ingrese el nombre del Curso:  ")
    print("----------------------------")
    cursos_model = cursoControler.list_curso_columns({'NOMBRE': nombre})

    if(cursos_model == []):
        print("-------------------------------------------------------------")
        print(f"====>  EL CURSO DE NOMBRE {nombre} NO EXISTE, INGRESE OTRO NOMBRE <====")
        print("-------------------------------------------------------------")
    else:
        print("-------------------------------------------------------------------------------------------------")
        print(f"====>  EL CURSO {nombre} ENCONTRADO  <====")
        print("( ID | NOMBRE  ) \n", cursos_model)
        print("-------------------------------------------------------------------------------------------------")
    opc_eli = continuar_mensaje('Consultando')
    if (opc_eli=="1"):
        consultar_curso()
    

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

def ejecuta_modulo_cursos():
    while True:
        modulo_curso()
        op_r = continuar_mensaje('con el Mantenimiento de Cursos ?')
        if (op_r=="2"):
            print("--------------------------------------------------------------------------------")
            print("SALIO DEL MODULO DE MANTENIMIENTO DE CURSOS")
            print("--------------------------------------------------------------------------------")
            break

# ejecuta_modulo_cursos()