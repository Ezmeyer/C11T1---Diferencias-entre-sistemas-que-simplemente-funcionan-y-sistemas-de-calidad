# ==============================
# SISTEMA DE CLÍNICA SIMPLE
# ==============================

# Estructuras de datos
pacientes = {}   # cedula -> datos del paciente
citas = []       # lista de citas
facturas = []    # lista de facturas


# ------------------------------
# Registro de pacientes
# ------------------------------
def registrar_paciente(cedula, nombre, edad):
    if cedula in pacientes:
        print("Paciente ya registrado.")
        return

    pacientes[cedula] = {
        "nombre": nombre,
        "edad": edad,
        "historial": []
    }


# ------------------------------
# Programar citas
# ------------------------------
def programar_cita(cedula, doctor, fecha, hora):
    if cedula not in pacientes:
        print("Paciente no existe.")
        return

    # Verificar si el doctor está ocupado
    for cita in citas:
        if cita["doctor"] == doctor and cita["fecha"] == fecha and cita["hora"] == hora:
            print("Horario ocupado.")
            return

    citas.append({
        "cedula": cedula,
        "doctor": doctor,
        "fecha": fecha,
        "hora": hora
    })


# ------------------------------
# Historial médico
# ------------------------------
def agregar_historial(cedula, registro):
    if cedula in pacientes:
        pacientes[cedula]["historial"].append(registro)
    else:
        print("Paciente no encontrado.")


# ------------------------------
# Facturación
# ------------------------------
def generar_factura(cedula, monto):
    if cedula not in pacientes:
        print("Paciente no existe.")
        return

    facturas.append({
        "cedula": cedula,
        "monto": monto
    })


# ------------------------------
# Mostrar datos
# ------------------------------
def mostrar_pacientes():
    for cedula, datos in pacientes.items():
        print(cedula, "-", datos["nombre"])


# ------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------
def main():
    while True:
        print("\n1. Registrar paciente")
        print("2. Programar cita")
        print("3. Agregar historial")
        print("4. Generar factura")
        print("5. Ver pacientes")
        print("6. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            cedula = input("Cédula: ")
            nombre = input("Nombre: ")
            edad = int(input("Edad: "))
            registrar_paciente(cedula, nombre, edad)

        elif opcion == "2":
            cedula = input("Cédula: ")
            doctor = input("Doctor: ")
            fecha = input("Fecha: ")
            hora = input("Hora: ")
            programar_cita(cedula, doctor, fecha, hora)

        elif opcion == "3":
            cedula = input("Cédula: ")
            registro = input("Diagnóstico: ")
            agregar_historial(cedula, registro)

        elif opcion == "4":
            cedula = input("Cédula: ")
            monto = float(input("Monto: "))
            generar_factura(cedula, monto)

        elif opcion == "5":
            mostrar_pacientes()

        elif opcion == "6":
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()