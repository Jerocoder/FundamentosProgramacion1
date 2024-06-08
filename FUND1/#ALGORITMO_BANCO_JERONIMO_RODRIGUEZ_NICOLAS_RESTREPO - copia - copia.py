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
""" USER = [0] Id, [1] Primer Nombre, [2] Primer Apellido, [3] Numero Tarjeta, [4] Pw Tarjeta, 
            [5] Saldo Cuenta Ahorros, [6] Saldo Prestamo LI, [7] Numero Cuotas Prestamo  
"""

print("Bienvenido a BancaIUD")
print("En este portal usted podrá realizar las operaciones financieras relacionadas a su producto.")

class Usuario:
    def __init__(self, id, primer_nombre, primer_apellido, numero_tarjeta, pw_tarjeta, saldo_ahorro, saldo_prestamo, numero_cuotas):
        self.id = id
        self.primer_nombre = primer_nombre
        self.primer_apellido = primer_apellido
        self.numero_tarjeta = numero_tarjeta
        self.pw_tarjeta = pw_tarjeta
        self.saldo_ahorro = saldo_ahorro
        self.saldo_prestamo = saldo_prestamo
        self.numero_cuotas = numero_cuotas
        
usuario_1035103105 = Usuario(1035103105, "Sharon", "Karin", '1111222233334444', '1234', 10000000, 500000, 6)

#VECTORES DE LA ENTREGA ANTERIOR
usuario_00000001 = [1035103105, "Sharon", "Karin", '1111222233334444', '1234', 10000000, 500000, 6]
usuario_00000002 = [1035103106, "Laura", "Mejia", '1111222233335555', '1235', 900000, 80000, 16]
usuario_00000003 = [1035103107, "Nicole", "Gil", '1111222233336666', '1236', 98500000, 5500000, 8]
usuario_00000004 = [1035103108, "Mariana", "Zapata", '1111222233337777', '1237', 2360000, 895000, 24]
usuario_00000005 = [1035103109, "Mafe", "Gil", '1111222233338888', '1238', 7540000, 2563000, 10]

validar_id = False

while validar_id == False:
    num_tarj = input("\nIngrese los dieciséis (16) dígitos de su tarjeta débito para ingresar.\n   NUMERO: ")
    password_tarj = input("Ingrese los cuatro (4) digitos de su clave de operaciones.\n   PASSWORD: ")
    if num_tarj == usuario_1035103105.numero_tarjeta and password_tarj == usuario_1035103105.pw_tarjeta:
        print("\nHa ingresado sus credenciales correctamente...")
        validar_id = True
    else:
        print("\nCredenciales de acceso erróneas.\nPor favor verifique el número y password de su tarjeta débito.")

while validar_id == True:
    print("\nSeleccione la accion que desea realizar:\n")
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
            if monto_retiro < usuario_1035103105.saldo_ahorro:
                usuario_1035103105.saldo_ahorro = usuario_1035103105.saldo_ahorro - monto_retiro
                print("\nEl retiro de efectivo se ha realizado de manera exitosa.")
                print("Valor de su retiro es: " + str(monto_retiro))
                print("Saldo actual disponible: " + str(usuario_1035103105.saldo_ahorro))
                retiro_exitoso = True
            else: 
                print("El monto a retirar excede el saldo disponible de su cuenta de ahorros.")
    #OPCION 2
    elif opcion_menu == "2":
        print("\nEl saldo actual de su cuenta de ahorros es: " + str(usuario_1035103105.saldo_ahorro))
    #OPCION 3
    elif opcion_menu == "3":
        print("\nEl saldo actual de su prestamo es: " + str(usuario_1035103105.saldo_prestamo))
    #OPCION 4
    elif opcion_menu == "4":
        abono_exitoso = False
        while abono_exitoso == False:
            print("\nEl saldo actual de su prestamo es: " + str(usuario_00000001[6]))
            print("Ingrese el monto que desea abonar a su prestamo: ")
            abono_prestamo = int(input("Valor: "))
            if abono_prestamo < usuario_1035103105.saldo_ahorro:
                usuario_1035103105.saldo_prestamo = usuario_1035103105.saldo_prestamo - abono_prestamo
                usuario_1035103105.saldo_ahorro = usuario_1035103105.saldo_ahorro - abono_prestamo
                print("El abono a su prestamo se ha realizado de forma correcta.")
                print("El saldo actual de su prestamo es: " + str(usuario_1035103105.saldo_prestamo))
                abono_exitoso = True
            else:
                print("\nEl valor a abonar excede el saldo disponible de su cuenta de ahorros.")
    #OPCION 5
    elif opcion_menu == "5":
        pago_exitoso = False
        while pago_exitoso == False:
            print("\nIngrese el codigo de convenio del servicio a pagar.")
            servicio = input("Convenio: ")
            print("Ingrese el monto que desea pagar al convenio #" + str(servicio))
            pago_servicio = int(input("Valor: "))
            if pago_servicio < usuario_1035103105.saldo_ahorro:
                usuario_1035103105.saldo_ahorro = usuario_1035103105.saldo_ahorro - pago_servicio
                print("El pago del servicio con convenio #" + str(servicio) + " se realizó de forma correcta.")
                print(f"Valor pagado: {pago_servicio}")
                pago_exitoso = True
            else:
                print("\nEl valor a pagar excede el saldo disponible de su cuenta de ahorros.")
    #OPCION 6
    elif opcion_menu == "6":
        print("\nEl número de cuotas de su prestamo es: " + str(usuario_1035103105.numero_cuotas))
    else:
        print("\nPor favor ingrese una opción válida.")
    
    print("\n¿Desea realizar otra transacción?")
    print("[1] SI")
    print("[2] NO")
    continua_proceso = input("\nOPCIÓN: ")
    if continua_proceso == "1":
        validar_id = True
    elif continua_proceso == "2":
        validar_id = False
    else:
        print("\nPor favor ingrese una opción válida.")

    
#print("ok")