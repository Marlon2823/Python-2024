print("¿Que operación desea realizar, 1.Suma, 2.Resta,3Multiplicacion,4.Division")
opcion = int(input("Ingrese el número de la opción deseada: "))
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if opcion == 1:
     Suma = num1 + num2
     print(f"El resultado de la suma es: {Suma}")
elif opcion == 2:
     Resta = num1 - num2
     print(f"El resultado de la resta es: {Resta}")
elif opcion == 3:
     Multiplicacion = num1 * num2
     print(f"El resultado de la multiplicación es: {Multiplicacion}")
elif opcion == 4:
     Division = num1 / num2
     print(f"El resultado de la multiplicación es: {Division}")

