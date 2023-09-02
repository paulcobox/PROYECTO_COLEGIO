import sys
from controller.salon import SalonController

def modulo_salon():
    print("--------------------------------------------------------------------------------")
    print("MANTENIMIENTO DE SALONES")
    print("1: Crear salon")
    print("2: Modificar salon")
    print("3: Eliminar salon")
    print("4: Consultar salon")
    try:
        
        option = input(f"Ingrese el número de la opción que desea: ")
        print("--------------------------------------------------------------------------------")
        if (option=="1"):
            while True:
                crear_salon()
                opc = continuar_mensaje('Registrando')
                if (opc=="1"):
                    continue
                elif (opc=="2"):
                    break
        elif (option=="2"):
            modificar_salon()
        elif (option=="3"):
            eliminar_salon()
        elif (option=="4"):
            consultar_salon()
        else:
            print("Debe escoger una opción de la lista.")
            return modulo_salon()
    except KeyboardInterrupt:
        print('\n')
        print("Proceso terminado.")
        sys.exit()
    except ValueError as e:
      print(f'Ocurrio un problema, solo debes ingresar números, vuelve a ingresar todos los datos')
      modulo_profesor()

def crear_salon():
    salonControler = SalonController()
    print("NUEVO SALON")
    print("--------------------------------------------------------------------------------")
    nombre = input(f"Ingrese el Nombre del salon: ")
    salonControler.insert_salon({
        "NOMBRE": nombre
    })

def modificar_salon():
    salonControler = SalonController()
    print("MODIFICAR SALON")
    print("--------------------------------------------------------------------------------")
    print("PASO 1 : Seleccione el Salon que desea Modificar")
    print("--------------------------------------------------------------------------------")
    salonControler.list_salones()
    print("----------------------------")
    id = input(f"Ingrese el ID del Salon:  ")
    print("----------------------------")
    salon_model = salonControler.list_salon(id)
    if(salon_model == None):
        print("-------------------------------------------------------------")
        print(f"====>  EL SALON DE ID {id} NO EXISTE, SELECCIONE OTRO ID <====")
        print("-------------------------------------------------------------")
        modificar_salon()
    else:
        print("-------------------------------------------------------------------------------------------------")
        print("SALON SELECCIONADO ( ID | NOMBRE ) : ", salon_model)
        print("-------------------------------------------------------------------------------------------------")
    print("------------------------------------------")
    print("PASO 2 : Ingrese los Campos a Modificar")
    print("------------------------------------------")
    nombre = input(f"Ingrese el Nombre del Salon: ")
    salonControler.update_salon({"ID_SALON" : id }, {
        "NOMBRE": nombre
    })


def eliminar_salon():
    salonController = SalonController()
    print("ELIMINAR SALON")
    print("--------------------------------------------------------------------------------")
    print("PASO 1 : Seleccione el Salon que desea Eliminar")
    print("--------------------------------------------------------------------------------")
    salonController.list_salones()
    print("----------------------------")
    id = input(f"Ingrese el ID del Salon:  ")
    print("----------------------------")
    salon_model = salonController.list_salon(id)
    if(salon_model == None):
        print("-------------------------------------------------------------")
        print(f"====>  EL SALON DE ID {id} NO EXISTE, SELECCIONE OTRO ID <====")
        print("-------------------------------------------------------------")
        eliminar_salon()
    else:
        print("-------------------------------------------------------------------------------------------------")
        print("SALON SELECCIONADO ( ID | NOMBRE  ) : ", salon_model)
        print("-------------------------------------------------------------------------------------------------")
    print("------------------------------------------")
    print("PASO 2 : Confirme Eliminacion")
    print("------------------------------------------")
    opc_eli = continuar_mensaje('con la eliminacion')
    if (opc_eli=="1"):
        salonController.delete_salon({"ID_SALON" : id })

def consultar_salon():
    salonController = SalonController()
    print("CONSULTAR SALON")
    print("--------------------------------------------------------------------------------")
    print("Ingrese el Nombre del Salon que desea Consultar")
    print("--------------------------------------------------------------------------------")
    print("----------------------------")
    nombre = input(f"Ingrese el nombre del Salon:  ")
    print("----------------------------")
    salones_model = salonController.list_salon_columns({'NOMBRE': nombre})

    if(salones_model == []):
        print("-------------------------------------------------------------")
        print(f"====>  EL SALON DE NOMBRE {nombre} NO EXISTE, INGRESE OTRO NOMBRE <====")
        print("-------------------------------------------------------------")
    else:
        print("-------------------------------------------------------------------------------------------------")
        print(f"====>  EL SALON {nombre} ENCONTRADO  <====")
        print("( ID | NOMBRE  ) \n", salones_model)
        print("-------------------------------------------------------------------------------------------------")
    opc_eli = continuar_mensaje('Consultando')
    if (opc_eli=="1"):
        consultar_salon()
    

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

def ejecuta_modulo_salon():
    while True:
        modulo_salon()
        op_r = continuar_mensaje('con el Mantenimiento de Salones ?')
        if (op_r=="2"):
            print("--------------------------------------------------------------------------------")
            print("SALIO DEL MODULO DE MANTENIMIENTO DE SALONES")
            print("--------------------------------------------------------------------------------")
            break

# ejecuta_modulo_salon()