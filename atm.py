# Simulación de Cajero Automático (ATM)

class ATM:
    def __init__(self, balance=0):
        # Saldo inicial
        self.balance = balance

    def check_balance(self):
        # Mostrar saldo actual
        print(f"Su saldo actual es: ${self.balance}")

    def deposit(self, amount):
        # Depositar dinero
        if amount > 0:
            self.balance += amount
            print(f"Depósito exitoso. Nuevo saldo: ${self.balance}")
        else:
            print("El monto a depositar debe ser mayor a 0.")

    def withdraw(self, amount):
        # Retirar dinero
        if amount > self.balance:
            print("Fondos insuficientes.")
        elif amount <= 0:
            print("El monto a retirar debe ser mayor a 0.")
        else:
            self.balance -= amount
            print(f"Retiro exitoso. Nuevo saldo: ${self.balance}")


if __name__ == "__main__":

    atm1 = ATM(50000)

    while True:

        print("\n--- CAJERO AUTOMÁTICO ---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            atm1.check_balance()

        elif opcion == "2":
            monto = float(input("Ingrese el monto a depositar: "))
            atm1.deposit(monto)

        elif opcion == "3":
            monto = float(input("Ingrese el monto a retirar: "))
            atm1.withdraw(monto)

        elif opcion == "4":
            print("Gracias por usar el cajero automático. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")