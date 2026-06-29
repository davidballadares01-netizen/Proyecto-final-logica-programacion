import random #encarga de la aleatoriedad
#definimos nuestra variable generar contrasen
def generar_contrasena ():
    abecedario = "0123456789ABCDEJGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz%&¿?+*"
    
    #solicitamos los datos al usiario pero definimos strip() para eliminar espacios 
    usuario = input("Ingrese su Usuario: ").strip()
    #para evitar errores como en el anterior codigo generamos dos bucles while
    while not usuario:
        usuario = input("Error: El usuario no puede estar vacío: ").strip()
        #si el usuario no ingresa nada (falso) automaticamente entra en bucle hasta poner algun dato (verdadero)
    # Validación robusta de longitud
    while True:
        try: #convierte lo que se ingresa en un int (entero)
            longitud = int(input("Ingrese el tamaño de su contraseña: "))
            #bucle para evitar errores y usar excepciones
            if longitud > 0: break #si el numero no es mayor que 0 significa que ingreso 0
            print("Debe ser un número mayor a 0.") 
        except ValueError: # el except evita que el codigo colapse si el usuario no ingresa un numero
            #en cuanto se genere el error por poner letras no colapsa se muestra el print y pide de nuevo
            print("Error: Ingrese solo números enteros.")

     #Generación de contraseña random
    contrasena1 = ""
    #Usamos el bucle for porque dependiendo de la longitu ingresada se repetira este bucle
    for i in range(longitud): #se genera una lista de numeros por range
        contrasena1 += random.choice(abecedario) #choice es una funcion directa de python elige un valor al azar en la variable abecedario
        
    while True:#este bucle repite la accion si la contraseña repite algun caracter dos veces
        contrasena1 = ""
        for i in range(longitud):
            contrasena1 += random.choice(abecedario)
        primer_caracter = contrasena1[0] #se compara el primer caracter con el caracter de la posicion 1
        igualdad = 0  # contador
        for caracter in contrasena1:
            if caracter == primer_caracter: #se 
                igualdad += 1
        if igualdad < longitud: #si la igualdad es menor que la longitud significa que por lo menos hay dos caracteres difertentes
            break 
        # Si no el bucle vuelve a empezar y genera una nueva contraseña
    contrasena_encriptada = ""
    for caracter in contrasena1:
        indice = abecedario.find(caracter)
        # El operador % (módulo) asegura que no nos salgamos del abecedario
        encriptacion = (indice + 1) % len(abecedario) # Sumamos 1 al índice de cada carácter para "ocultar" la clave
        contrasena_encriptada += abecedario[encriptacion]

    print("\n CONTRASEÑAS ")
    print("Usuario:", usuario)
    print("Contraseña Normal (oculta):",contrasena1) # Esta seria la contraseña normal que saldria sin encriptar
    print("Contraseña Encriptada (final):",contrasena_encriptada) # y esta es la contraseña "encriptada" el metodo usado se llama ofuscasion.

    #Verificamos que tenga la longitud minima requerida
    if longitud < 8:
        print("Seguridad: DÉBIL, se recomienda utilizar 8 caracteres minimo.")
    else:
        print("Seguridad: FUERTE , se cumple con todos los requisitos de seguridad.")

generar_contrasena() #llama al def

