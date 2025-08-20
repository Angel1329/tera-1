from figuras import Cuadrado, Rectangulo, Triangulo, Circulo

def main():
    while True:  # Esto hace que el programa siga corriendo
        print("\n=== Calculadora de Áreas ===")
        print("1. Cuadrado")
        print("2. Rectángulo")
        print("3. Triángulo")
        print("4. Círculo")
        print("5. Salir")  # Opción para salir del programa

        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            lado = float(input("Ingresa el lado: "))
            figura = Cuadrado(lado)
        elif opcion == 2:
            base = float(input("Ingresa la base: "))
            altura = float(input("Ingresa la altura: "))
            figura = Rectangulo(base, altura)
        elif opcion == 3:
            base = float(input("Ingresa la base: "))
            altura = float(input("Ingresa la altura: "))
            figura = Triangulo(base, altura)
        elif opcion == 4:
            radio = float(input("Ingresa el radio: "))
            figura = Circulo(radio)
        elif opcion == 5:
            print("¡Gracias por usar la calculadora! Adiós 😎")
            break  # Esto termina el bucle y cierra el programa
        else:
            print("Opción inválida")
            continue  # Vuelve a mostrar el menú

        print("El área es:", figura.area())

if __name__ == "__main__":
    main()

