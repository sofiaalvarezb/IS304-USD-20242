#Sofia Alvarez 

class CuentaBancaria:

    def _init_(self, numeroCta=None, nombreCliente=None, fechaApertura=None, saldo=0):

        self.__numeroCta = numeroCta

        self.__nombreCliente = nombreCliente

        self.__fechaApertura = fechaApertura

        self.__saldo = saldo

    def get_numeroCta(self):

        return self.__numeroCta


    def get_nombreCliente(self):

        return self.__nombreCliente


    def get_fechaApertura(self):

        return self.__fechaApertura


    def get_saldo(self):

        return self.__saldo


    def set_numeroCta(self, numeroCta):

        self.__numeroCta = numeroCta


    def set_nombreCliente(self, nombreCliente):

        self.__nombreCliente = nombreCliente


    def set_fechaApertura(self, fechaApertura):

        self.__fechaApertura = fechaApertura


    def set_saldo(self, saldo):

        self.__saldo = saldo


    def abrir_cuenta(self, numeroCta, nombreCliente, fechaApertura, saldoInicial):

        if saldoInicial >= 100000:

            self.__numeroCta = numeroCta

            self.__nombreCliente = nombreCliente

            self.__fechaApertura = fechaApertura

            self.__saldo = saldoInicial

            print("Cuenta abierta con éxito.")

        else:

            print("Error: El saldo inicial debe ser al menos de 100,000 pesos.")


    def consignar(self, monto):

        if monto > 0:

            self.__saldo += monto

            print(f"Consignación exitosa. Nuevo saldo: {self.__saldo}")

        else:

            print("Error: La consignación debe ser un valor positivo.")


    def retirar(self, monto):

        if monto > 0 and monto <= self.__saldo:

            self.__saldo -= monto

            print(f"Retiro exitoso. Nuevo saldo: {self.__saldo}")

        elif monto > self.__saldo:

            print("Error: Fondos insuficientes.")

        else:

            print("Error: El monto de retiro debe ser positivo.")

def menu():

    cuenta = None


    while True:

        print("\n--- Menú Cuenta Bancaria ---")

        print("1. Abrir cuenta")

        print("2. Consignar dinero")

        print("3. Retirar dinero")

        print("4. Consultar saldo")

        print("5. Salir")

        opcion = input("Seleccione una opción: ")


        if opcion == '1':

            numeroCta = input("Ingrese el número de cuenta: ")

            nombreCliente = input("Ingrese el nombre del cliente: ")

            fechaApertura = input("Ingrese la fecha de apertura (dd/mm/aaaa): ")

            saldoInicial = float(input("Ingrese el saldo inicial: "))

            cuenta = CuentaBancaria()

            cuenta.abrir_cuenta(numeroCta, nombreCliente, fechaApertura, saldoInicial)

        
        elif opcion == '2':

            if cuenta:

                monto = float(input("Ingrese el monto a consignar: "))

                cuenta.consignar(monto)

            else:

                print("Debe abrir una cuenta primero.")

        
        elif opcion == '3':

            if cuenta:

                monto = float(input("Ingrese el monto a retirar: "))

                cuenta.retirar(monto)

            else:

                print("Debe abrir una cuenta primero.")

        
        elif opcion == '4':

            if cuenta:

                print(f"Saldo actual: {cuenta.get_saldo()}")

            else:

                print("Debe abrir una cuenta primero.")

        
        elif opcion == '5':

            print("Saliendo del sistema...")

            break

        
        else:

            print("Opción no válida, intente de nuevo.")

menu()
