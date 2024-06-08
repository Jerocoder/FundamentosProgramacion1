#ALGORITMO BANCO
"""
    // Desarrollar un programa en Python para un cajero de un banco. 
	// El sistema podrá realizar lo siguiente: 
	// 1.-Identificación de número de tarjeta de crédito y password 
	// 3.-Realizar Retiro de Dinero
	// 4.-Imprimir el saldo del cliente 
	// 5.-Pagar Préstamo de Banco
	// 6.-Consulta de Cuota de Pago de Préstamo
	// 7.-Pagos de Servicios Agua Luz Teléfono Cable
	// 8. Realizar Pago de Colegio y Universidad 
	// 9.-Mostrar número de cuotas de pago de préstamos
"""
""" USER = Id, Primer Nombre, Primer Apellido, Numero Tarjeta, Pw Tarjeta, Saldo Cuenta Ahorros, Saldo Prestamo LI, Numero Cuotas Prestamo  
"""

print("Bienvenido a BancaIUD")
print("En este portal usted podrá realizar las operaciones financieras relacionadas a su producto.")

saldo_prestamo = 9899990
num_cuotas_prestamo = 12
saldo_cuenta_ahorro = 12350000
validar_id = False
num_tarj_registrado = '1111222233334444'
password_tarj_registrado = '1234'

while validar_id == False:
    num_tarj = input("\nIngrese los dieciséis (16) dígitos de su tarjeta débito para ingresar.\n   NUMERO: ")
    password_tarj = input("Ingrese los cuatro (4) digitos de su clave de operaciones.\n   PASSWORD: ")
    if num_tarj_registrado == num_tarj and password_tarj_registrado == password_tarj:
        validar_id = True
    else:
        print("\nCredenciales de acceso erróneas.\nPor favor verifique el número y password de su tarjeta débito.")

while validar_id == True:
    print("\nHa ingresado sus credenciales correctamente...\n")
    print("Seleccione la accion que desea realizar:\n")
    print("[1] Retiro de Dinero")
    print("[2] Consulta de Saldo ahorro")
    print("[3] Consulta de Saldo del Prestamo")
    print("[4] Pagar Prestamos")
    print("[5] Pago de Servicios")
    print("[6] Consulta de numero de cuotas de Prestamo")
    
    opcion_menu = input("\nOPCIÓN: ")
    #OPCION 1
    if opcion_menu == "1":
        retiro_exitoso = False
        while retiro_exitoso == False:
            print("\nIngrese el monto que desea retirar.")
            monto_retiro = int(input("Valor: "))
            if monto_retiro < saldo_cuenta_ahorro:
                saldo_cuenta_ahorro = saldo_cuenta_ahorro - monto_retiro
                print("\nEl retiro de efectivo se ha realizado de manera exitosa.")
                print("Valor de su retiro es: " + str(monto_retiro))
                print("Saldo actual disponible: " + str(saldo_cuenta_ahorro))
                retiro_exitoso = True
            else: 
                print("El monto a retirar excede el saldo disponible de su cuenta de ahorros.")
    #OPCION 2
    elif opcion_menu == "2":
        print("El saldo actual de su cuenta de ahorros es: " + str(saldo_cuenta_ahorro))
    #OPCION 3
    elif opcion_menu == "3":
        print("El saldo actual de su prestamo es: " + str(saldo_prestamo))
    #OPCION 4
    elif opcion_menu == "4":
        abono_exitoso = False
        while abono_exitoso == False:
            print("El saldo actual de su prestamo es: " + str(saldo_prestamo))
            print("Ingrese el monto que desea abonar a su prestamo: ")
            abono_prestamo = int(input("Valor: "))
            if abono_prestamo < saldo_cuenta_ahorro:
                saldo_prestamo = saldo_prestamo - abono_prestamo
                saldo_cuenta_ahorro = saldo_cuenta_ahorro - abono_prestamo
                print("El abono a su prestamo se ha realizado de forma correcta.")
                print("El saldo actual de su prestamo es: " + str(saldo_prestamo))
                abono_exitoso = True
            else:
                print("El valor a abonar excede el saldo disponible de su cuenta de ahorros.")
    #OPCION 5
    elif opcion_menu == "5":
        pago_exitoso = False
        while pago_exitoso == False:
            print("Ingrese el codigo de convenio del servicio a pagar.")
            servicio = input("Convenio: ")
            print("Ingrese el monto que desea pagar al convenio #" + str(servicio))
            pago_servicio = int(input("Valor: "))
            if pago_servicio < saldo_cuenta_ahorro:
                saldo_cuenta_ahorro = saldo_cuenta_ahorro - pago_servicio
                print("El pago del servicio con convenio #" + str(servicio) + " se realizó de forma correcta.")
                pago_exitoso = True
            else:
                print("El valor a pagar excede el saldo disponible de su cuenta de ahorros.")
    #OPCION 6
    elif opcion_menu == "6":
        print("El número de cuotas de su prestamo es: " + str(num_cuotas_prestamo))
    else:
        print("Por favor ingrese una opción válida.")
    
    print("\n¿Desea realizar otra transacción?")
    print("[1] SI")
    print("[2] NO")
    continua_proceso = input("\nOPCIÓN: ")
    if continua_proceso == "1":
        validar_id = True
    elif continua_proceso == "2":
        validar_id = False
    else:
        print("Por favor ingrese una opción válida.")

    
#print("ok")
