from backend import (
    crearTablaContactos,
    agregarContactos,
    mostrarContactos,
    buscarContactos,
    eliminarContactos
)

crearTablaContactos()


agenda=[] #se crea como lista, ya que, siendo solo dict, se guarda 1 solo contacto, en cambio se hara una lista de diccionarios. Lista el indice y el diccionario la info del contacto

while True:
    print("BIENVENIDO A SU AGENDA SELECCIONE OPCION:")
    print("1.-AGREGAR CONTACTOS")
    print("2.-BUSCAR CONTACTOS")
    print("3.-VER CONTACTOS")
    print("4.-ELIMINAR CONTACTOS")
    print("5.-Salir")
    opcion=input()
    if opcion.isdigit():
        opcion=int(opcion)
    else:
        print("INGRESE UNA OPCION VALIDA!")
        continue
    if opcion==1:
        nombre=input("INGRESE NOMBRE DE CONTACTO:")
        numero=input("INGRESE NUMERO DE CONTACTO:") 
        while len(numero)!=9:
            print("NUMERO NO VALIDO, VUELVA A INTENTAR")
            numero=input("INGRESE NUMERO DE CONTACTO:")
        while True:
            email=input("INGRESE EMAIL:")
            if "@" in email and " " not in email:
                break
            else:
                print("INGRESE CORREO VALIDO")
        nuevo_contacto={'NOMBRE':nombre,'NUMERO':numero,'CORREO':email}
        agenda.append(nuevo_contacto)
        print("CONTACTO AGREGADO EXITOSAMENTE!")
        
    elif opcion ==2:
        nombre2=input("INGRESE ID O NOMBRE DE CONTACTO:")
        encontrado=False
        for i in agenda:
            if i['NOMBRE'] == nombre2:
                print(f"CONTACTO ENCONTRADO NOMBRE:{i['NOMBRE']}")
                print(f"CONTACTO ENCONTRADO NUMERO:{i['NUMERO']}")
                print(f"CONTACTO ENCONTRADO CORREO:{i['CORREO']}")
                encontrado=True
                break
        if not encontrado:
            print("CONTACTO NO ENCONTRADO")
        continue
    elif opcion ==3:
        for i,x in enumerate(agenda):
            print(f"CONTACTO N°: {i+1}")
            print(f"NOMBRE:{x["NOMBRE"]}")
            print(f"FONO:{x["NUMERO"]}")
            print(f"EMAIL:{x["CORREO"]}")
        continue
    elif opcion==4:
        nombre3=input("INGRESE NOMBRE DE CONTACTO A ELIMINAR:")
        agenda2=[i for i in agenda if i['NOMBRE']!=nombre3]
        if len(agenda2)<len(agenda):
            agenda=agenda2
            print("CONTACTO ELIMINADO CORRECTAMENTE")
            print("---------------------------------")
        else:
            print("CONTACTO NO EXISTE")
    elif opcion==5:
        print("GRACIAS POR USAR LA AGENDA, SALIENDO...")
        break
    else:
        print("OPCION NO VALIDA!")