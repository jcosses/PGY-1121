# EJEMPLO DE USO DE GITHUB
print("INGRESO DE DATOS")
print("----------------\n")
vNom = input("Ingrese su Nombre: ")

while True:
    try:
        vEdad = int(input("Ingrese su Edad: "))
        break
    except:
        print("Error de Ingreso")

print("-------------------------")
print(f"Su Nombres es {vNom}")
print(f"Su Edad es {vEdad}")
print("Prgama Finalizado..")
