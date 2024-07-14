#variable para almacenar los usuarios que se registren
usuarios_registrados = {
}

#primer ciclo para el registro o ingreso de usuarios
while True:
    print("\nBienvenido al sistema de registro y acceso.")
    print("1. Iniciar sesión con usuario existente")
    print("2. Registrarse como nuevo usuario")
    print("3. Salir")
    
    opcion = input("Seleccione una opción (1/2/3): ")
    
    #if para iniciar el acceso a los usuarios
    if opcion == "1":
        usuario_existente = input("Ingrese el nombre de usuario existente: ")
        piningreso = input("Ingrese el pin de su usuario" )
        if usuario_existente in usuarios_registrados and piningreso == pin :
            print(f"Bienvenido, {usuarios_registrados[usuario_existente]['nombre']}!")
            #segundo ciclo para iniciar el acceso o registro de casas 
            while True:
                print("\nMenú de opciones:")
                print("1. Acceder a una casa")
                print("2. Registrar una nueva casa")
                print("3. Volver al menú principal")
                
                opcion_menu = input("Seleccione una opción (1/2/3): ")
                #if para el ingreso a la casa
                if opcion_menu == "1":
                    print("\nCasas disponibles:")
                    for casa in usuarios_registrados[usuario_existente]["casas"]:
                        print(casa)
                    
                    nombre_casa = input("Ingrese el nombre de la casa a la que desea acceder: ")
                    if nombre_casa in usuarios_registrados[usuario_existente]["casas"]:
                        #tercer ciclo para el acceso y registro de las casa
                        while True:
                            print(f"\nHabitaciones de la casa '{nombre_casa}':")
                            for habitacion in usuarios_registrados[usuario_existente]["casas"][nombre_casa]["habitaciones"]:
                                print(habitacion)
                            
                            print("\nMenú de opciones:")
                            print("1. Registrar una nueva habitación")
                            print("2. Ingresar a una habitación")
                            print("3. Volver al menú de casas")
                            
                            opcion_habitacion = input("Seleccione una opción (1/2/3): ")
                            
                            #if para registrar una habitación, 
                            if opcion_habitacion == "1":
                                nueva_habitacion = input("Ingrese el nombre de la nueva habitación: ")
                                usuarios_registrados[usuario_existente]["casas"][nombre_casa]["habitaciones"].append(nueva_habitacion)
                                print(f"Habitación '{nueva_habitacion}' registrada correctamente.")
                            #if para ingresar a una habitación
                            elif opcion_habitacion == "2":
                                nombre_habitacion = input("Ingrese el nombre de la habitación a la que desea ingresar: ")
                                if nombre_habitacion in usuarios_registrados[usuario_existente]["casas"][nombre_casa]["habitaciones"]:
                                    print(f"Bienvenido a la habitación '{nombre_habitacion}' de la casa '{nombre_casa}'.")
                                    # Futuro añadir los dispositivos y sus funcionalidades
                                else:
                                    print("La habitación no existe. Inténtelo de nuevo.")
                            
                            elif opcion_habitacion == "3":
                                break
                            
                            else:
                                print("Opción no válida. Inténtelo de nuevo.")
                    
                    else:
                        print("La casa no existe. Inténtelo de nuevo.")
                #if registrar la nueva casa
                elif opcion_menu == "2":
                    nueva_casa = input("Ingrese el nombre de la nueva casa: ")
                    if nueva_casa in usuarios_registrados[usuario_existente]["casas"]:
                        print("El nombre de la casa ya está en uso. Inténtelo de nuevo.")
                    else:
                        usuarios_registrados[usuario_existente]["casas"][nueva_casa] = {"habitaciones": []}
                        print(f"Casa '{nueva_casa}' registrada correctamente.")
                
                elif opcion_menu == "3":
                    break
                
                else:
                    print("Opción no válida. Inténtelo de nuevo.")
        
        else:
            print("El usuario no existe. Inténtelo de nuevo.")
    #if registrar el nuevo usuario
    elif opcion == "2":
        nuevo_usuario = input("Ingrese un nombre de usuario nuevo: ")
        if nuevo_usuario in usuarios_registrados:
            print("El nombre de usuario ya está en uso. Inténtelo de nuevo.")
        else:
            nombre = input("Ingrese su nombre: ")
            pin = input("Ingrese su pin: ") 
            usuarios_registrados[nuevo_usuario] = {"nombre": nombre, "pin": pin, "casas": {}}
            print("Registro exitoso.")
    
    elif opcion == "3":
        print("Gracias por usar nuestro sistema.")
        break
    
    else:
        print("Opción no válida. Inténtelo de nuevo.")
