import sys
from modulo_alumnos import ejecuta_modulo_alumnos
from modulo_cursos import ejecuta_modulo_cursos
from modulo_profesores import ejecuta_modulo_profesor
from modulo_salones import ejecuta_modulo_salon


def modulo_principal():
    print("--------------------------------------------------------------------------------")
    print("--------------------------------------------------------------------------------")
    print("            BIENVENIDO AL SISTEMA DE CONFIGURACION DEL COLEGIO")
    print("--------------------------------------------------------------------------------")
    try:
      while True:
        print("--------------------------------------------------------------------------------")
        print("1: Mantenimiento de Alumnos")
        print("2: Mantenimiento de Profesores")
        print("3: Mantenimiento de Cursos")
        print("4: Mantenimiento de Salones")
        option = input(f"Ingrese el número de la opción que desea: ")
        print("--------------------------------------------------------------------------------")
        if (option=="1"):
            ejecuta_modulo_alumnos()
        elif (option=="2"):
            ejecuta_modulo_profesor()
        elif (option=="3"):
            ejecuta_modulo_cursos()
        elif (option=="4"):
            ejecuta_modulo_salon()
        else:
            print("Debe escoger una opción de la lista.")
            return modulo_principal()

        op_m = continuar_mensaje('Realizando Matenimiento a Otros Modulos')
        if (op_m=="2"):
            print("--------------------------------------------------------------------------------")
            print("SALIO DEL MODULO DE COLEGIO")
            print("--------------------------------------------------------------------------------")
            break
        
    except KeyboardInterrupt:
        print('\n')
        print("Proceso terminado.")
        sys.exit()


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


modulo_principal()