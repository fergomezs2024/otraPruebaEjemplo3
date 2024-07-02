ciudadanos_registrados = []
def menu_principal():
    print("*"*50)
    print("Ingrese una opcion : ")
    print("1) grabar ")
    print("2) Buscar : ")
    print("3) Crear archivo")
    print("4) Salir: \n ")

def validaDatos(data):

    if len(data['nombre'])<0:
        return [False,"Nombre invalido"]
    else:
        if int(data['edad'])<15:
            return [False,"edad no valida"]
        else:
            if not data['nif'][:8].isdigit() and len(data['nif'])!= 12:
                return [False,"Nif no valido"]
            else:
                return [True,data]
while True :
    menu_principal()
    opcion = input("")

    if opcion == "1":
        nombre = input("Ingrese nombre y apellido")
        edad = input("Ingrese edad")
        nif = input("Ingrese nif")

        datos = {"nombre":nombre,
                 "edad":edad,
                 "nif":nif}
        
        res = validaDatos(datos)
        print('res',res)
        if res[0] :
            print("Datos validos")
            ciudadanos_registrados.append(res[1])
        else:
            print("Datos incorrectos",res[1])
    if opcion =="2":
        print(ciudadanos_registrados)
        
