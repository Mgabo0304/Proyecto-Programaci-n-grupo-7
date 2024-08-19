# Variable para almacenar los usuarios registrados
usuarios_registrados = []

def encontrar_usuario(nombre_usuario):
    # Buscar un usuario en la lista de usuarios registrados
    for usuario in usuarios_registrados:
        if usuario["nombre_usuario"] == nombre_usuario:
            return usuario
    return None

def registrar_usuario():
    # Registrar un nuevo usuario
    nuevo_usuario = input("Ingrese un nombre de usuario nuevo: ")
    usuario_encontrado = encontrar_usuario(nuevo_usuario)
    if usuario_encontrado:
        print("El nombre de usuario ya está en uso. Inténtelo de nuevo.")
    else:
        nombre = input("Ingrese su nombre: ")
        pin = input("Ingrese su pin: ")
        usuario = {
            "nombre_usuario": nuevo_usuario,
            "nombre": nombre,
            "pin": pin,
            "casas": []
        }
        usuarios_registrados.append(usuario)
        print("Registro exitoso.")

def iniciar_sesion():
    # Iniciar sesión con un usuario existente
    usuario_existente = input("Ingrese el nombre de usuario existente: ")
    piningreso = input("Ingrese el pin de su usuario: ")
    usuario = encontrar_usuario(usuario_existente)
    if usuario and piningreso == usuario["pin"]:
        print("Bienvenido, " + usuario["nombre"] + "!")
        menu_casas(usuario)
    else:
        print("Usuario o pin incorrecto. Por favor inténtelo de nuevo.")

def menu_casas(usuario):
    # Menú para gestionar casas del usuario
    while True:
        print("\nMenú de casas:")
        print("1. Acceder a una casa")
        print("2. Registrar una nueva casa")
        print("3. Ver casas registradas")
        print("4. Volver al menú principal")
        
        opcion_menu = input("Seleccione una opción (1/2/3/4): ")
        
        if opcion_menu == "1":
            listar_casas(usuario)
        elif opcion_menu == "2":
            registrar_casa(usuario)
        elif opcion_menu == "3":
            ver_casas_registradas(usuario)
        elif opcion_menu == "4":
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

def listar_casas(usuario):
    # Listar casas del usuario y permitir acceso a una casa específica
    print("\nCasas disponibles:")
    casas = usuario["casas"]
    if len(casas) > 0:
        for i in range(len(casas)):
            print(casas[i]["nombre"])
    else:
        print("No hay casas registradas.")
    
    nombre_casa = input("Ingrese el nombre de la casa a la que desea acceder: ")
    casa_encontrada = None
    for casa in casas:
        if casa["nombre"] == nombre_casa:
            casa_encontrada = casa
            break
    if casa_encontrada:
        menu_habitaciones(usuario, casa_encontrada)
    else:
        print("La casa no existe. Inténtelo de nuevo.")

def registrar_casa(usuario):
    # Registrar una nueva casa
    nueva_casa = input("Ingrese el nombre de la nueva casa: ")
    casas = usuario["casas"]
    casa_existe = False
    for casa in casas:
        if casa["nombre"] == nueva_casa:
            casa_existe = True
            break
    if casa_existe:
        print("El nombre de la casa ya está en uso. Inténtelo de nuevo.")
    else:
        nueva_casa = {
            "nombre": nueva_casa,
            "habitaciones": []
        }
        usuario["casas"].append(nueva_casa)
        print("Casa '" + nueva_casa["nombre"] + "' registrada correctamente.")

def ver_casas_registradas(usuario):
    # Ver casas registradas por el usuario
    print("\nCasas registradas:")
    casas = usuario["casas"]
    if len(casas) > 0:
        for i in range(len(casas)):
            print("Casa: " + casas[i]["nombre"])
            habitaciones = casas[i]["habitaciones"]
            if len(habitaciones) > 0:
                for j in range(len(habitaciones)):
                    print("  - Habitación: " + habitaciones[j]["nombre"])
                    dispositivos = habitaciones[j]["dispositivos"]
                    if len(dispositivos) > 0:
                        for dispositivo, info in dispositivos.items():
                            estado = info["estado"]
                            programacion = info.get("programacion", "No programado")
                            print(f"    - Dispositivo: {dispositivo}, Estado: {estado}, Programado para: {programacion}")
                    else:
                        print("    No hay dispositivos registrados en esta habitación.")
            else:
                print("  No hay habitaciones registradas en esta casa.")
    else:
        print("No tiene casas registradas.")

def menu_habitaciones(usuario, casa):
    # Menú para gestionar habitaciones dentro de una casa
    while True:
        print("\nHabitaciones de la casa '" + casa["nombre"] + "':")
        habitaciones = casa["habitaciones"]
        if len(habitaciones) > 0:
            for i in range(len(habitaciones)):
                print(habitaciones[i]["nombre"])
        else:
            print("No hay habitaciones registradas en esta casa.")
        
        print("\nMenú de habitaciones:")
        print("1. Registrar una nueva habitación")
        print("2. Ingresar a una habitación")
        print("3. Ver habitaciones registradas")
        print("4. Volver al menú de casas")
        
        opcion_habitacion = input("Seleccione una opción (1/2/3/4): ")
        
        if opcion_habitacion == "1":
            registrar_habitacion(usuario, casa)
        elif opcion_habitacion == "2":
            ingresar_habitacion(usuario, casa)
        elif opcion_habitacion == "3":
            ver_habitaciones_registradas(casa)
        elif opcion_habitacion == "4":
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

def registrar_habitacion(usuario, casa):
    # Registrar una nueva habitación en una casa
    nueva_habitacion = input("Ingrese el nombre de la nueva habitación: ")
    habitaciones = casa["habitaciones"]
    habitacion_existe = False
    for habitacion in habitaciones:
        if habitacion["nombre"] == nueva_habitacion:
            habitacion_existe = True
            break
    if habitacion_existe:
        print("La habitación ya existe. Inténtelo de nuevo.")
    else:
        nueva_habitacion = {
            "nombre": nueva_habitacion,
            "dispositivos": {}
        }
        casa["habitaciones"].append(nueva_habitacion)
        print("Habitación '" + nueva_habitacion["nombre"] + "' registrada correctamente.")

def ver_habitaciones_registradas(casa):
    # Ver habitaciones registradas en una casa
    print("\nHabitaciones en la casa '" + casa["nombre"] + "':")
    habitaciones = casa["habitaciones"]
    if len(habitaciones) > 0:
        for i in range(len(habitaciones)):
            print("Habitación: " + habitaciones[i]["nombre"])
            dispositivos = habitaciones[i]["dispositivos"]
            if len(dispositivos) > 0:
                for dispositivo, info in dispositivos.items():
                    estado = info["estado"]
                    programacion = info.get("programacion", "No programado")
                    print(f"  - Dispositivo: {dispositivo}, Estado: {estado}, Programado para: {programacion}")
            else:
                print("  No hay dispositivos registrados en esta habitación.")
    else:
        print("No hay habitaciones registradas en esta casa.")

def ingresar_habitacion(usuario, casa):
    # Ingresar a una habitación específica y gestionar dispositivos
    nombre_habitacion = input("Ingrese el nombre de la habitación a la que desea ingresar: ")
    habitaciones = casa["habitaciones"]
    habitacion_encontrada = None
    for habitacion in habitaciones:
        if habitacion["nombre"] == nombre_habitacion:
            habitacion_encontrada = habitacion
            break
    if habitacion_encontrada:
        print("Bienvenido a la habitación '" + nombre_habitacion + "' de la casa '" + casa["nombre"] + "'.")
        menu_dispositivos(usuario, casa, habitacion_encontrada)
    else:
        print("La habitación no existe. Inténtelo de nuevo.")

def menu_dispositivos(usuario, casa, habitacion):
    # Menú para gestionar dispositivos dentro de una habitación
    while True:
        print("\nDispositivos en la habitación '" + habitacion["nombre"] + "':")
        dispositivos = habitacion["dispositivos"]
        if len(dispositivos) > 0:
            for dispositivo, info in dispositivos.items():
                estado = info["estado"]
                programacion = info.get("programacion", "No programado")
                print(f"Dispositivo: {dispositivo}, Estado: {estado}, Programado para: {programacion}")
        else:
            print("No hay dispositivos registrados en esta habitación.")
        
        print("\nMenú de dispositivos:")
        print("1. Registrar un nuevo dispositivo")
        print("2. Ver dispositivos registrados")
        print("3. Volver al menú de habitaciones")
        
        opcion_dispositivo = input("Seleccione una opción (1/2/3): ")
        
        if opcion_dispositivo == "1":
            registrar_dispositivo(usuario, casa, habitacion)
        elif opcion_dispositivo == "2":
            ver_dispositivos_registrados(habitacion)
        elif opcion_dispositivo == "3":
            break
        else:
            print("Opción inválida. Inténtelo de nuevo.")

def registrar_dispositivo(usuario, casa, habitacion):
    # Registrar un nuevo dispositivo en una habitación
    nombre_dispositivo = input("Ingrese el nombre del nuevo dispositivo: ")
    dispositivos = habitacion["dispositivos"]
    if nombre_dispositivo in dispositivos:
        print("El dispositivo ya existe. Inténtelo de nuevo.")
    else:
        estado = input("Ingrese el estado inicial del dispositivo (encendido/apagado): ")
        if estado != "encendido" and estado != "apagado":
            print("Estado inválido. Debe ser 'encendido' o 'apagado'.")
            return
        programacion = ""
        programar = input("¿Desea programar el dispositivo? (si/no): ")
        if programar == "si":
            dia = input("Ingrese el día de la semana (lunes, martes, etc.): ")
            hora = input("Ingrese la hora de encendido (HH:MM): ")
            programacion = dia + " a las " + hora
        dispositivos[nombre_dispositivo] = {
            "estado": estado,
            "programacion": programacion
        }
        print("Dispositivo '" + nombre_dispositivo + "' registrado correctamente.")

def ver_dispositivos_registrados(habitacion):
    # Ver dispositivos registrados en una habitación
    print("\nDispositivos en la habitación '" + habitacion["nombre"] + "':")
    dispositivos = habitacion["dispositivos"]
    if len(dispositivos) > 0:
        for dispositivo, info in dispositivos.items():
            estado = info["estado"]
            programacion = info.get("programacion", "No programado")
            print(f"Dispositivo: {dispositivo}, Estado: {estado}, Programado para: {programacion}")
    else:
        print("No hay dispositivos registrados en esta habitación.")

def ver_usuarios_registrados():
    # Ver usuarios registrados en el sistema
    print("\nUsuarios registrados:")
    if len(usuarios_registrados) > 0:
        for usuario in usuarios_registrados:
            print("Nombre de usuario: " + usuario["nombre_usuario"] + ", Nombre: " + usuario["nombre"])
            print("  Casas registradas:")
            for casa in usuario["casas"]:
                print("    Casa: " + casa["nombre"])
                for habitacion in casa["habitaciones"]:
                    print("      Habitación: " + habitacion["nombre"])
                    for dispositivo, info in habitacion["dispositivos"].items():
                        estado = info["estado"]
                        programacion = info.get("programacion", "No programado")
                        print(f"        Dispositivo: {dispositivo}, Estado: {estado}, Programado para: {programacion}")
    else:
        print("No hay usuarios registrados.")

# Ciclo principal para el registro o ingreso de usuarios
while True:
    print("\nBienvenido al sistema de registro y acceso.")
    print("1. Iniciar sesión con usuario existente")
    print("2. Registrarse como nuevo usuario")
    print("3. Ver usuarios registrados")
    print("4. Salir")

    opcion = input("Seleccione una opción (1/2/3/4): ")
    
    if opcion == "1":
        iniciar_sesion()
    elif opcion == "2":
        registrar_usuario()
    elif opcion == "3":
        ver_usuarios_registrados()
    elif opcion == "4":
        print("Gracias por usar nuestro sistema.")
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")
