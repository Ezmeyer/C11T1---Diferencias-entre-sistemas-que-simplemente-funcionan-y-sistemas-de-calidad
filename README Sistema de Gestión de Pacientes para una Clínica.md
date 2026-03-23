🏥 Sistema de Clínica Simple en Python

Este proyecto es un sistema básico de gestión clínica desarrollado en Python que funciona desde la consola. Permite administrar pacientes, citas médicas, historial clínico y facturación.

🚀 Funcionalidades

El sistema incluye:

👤 Registro de pacientes
📅 Programación de citas médicas
🧾 Gestión de historial clínico
💰 Generación de facturas
📋 Visualización de pacientes registrados
🧠 Estructura del Sistema
👤 Pacientes

Se almacenan en un diccionario donde:

La clave es la cédula
El valor contiene:
nombre
edad
historial (lista de registros médicos)
📅 Citas

Lista que almacena citas con:

Cédula del paciente
Doctor
Fecha
Hora
💰 Facturas

Lista que contiene:

Cédula del paciente
Monto a pagar
⚙️ Funciones Principales
registrar_paciente(cedula, nombre, edad)

Registra un nuevo paciente si no existe previamente.

programar_cita(cedula, doctor, fecha, hora)

Permite agendar una cita:

Verifica que el paciente exista
Evita conflictos de horario del doctor
agregar_historial(cedula, registro)

Añade un diagnóstico o registro al historial del paciente.

generar_factura(cedula, monto)

Crea una factura asociada a un paciente.

mostrar_pacientes()

Lista todos los pacientes registrados.

▶️ Ejecución
Asegúrate de tener Python 3 instalado
Ejecuta el archivo:
python nombre_del_archivo.py
🖥️ Menú del Sistema
1. Registrar paciente
2. Programar cita
3. Agregar historial
4. Generar factura
5. Ver pacientes
6. Salir
📌 Ejemplo de uso
Opción: 1
Cédula: 123456789
Nombre: María López
Edad: 30

Opción: 2
Cédula: 123456789
Doctor: Dr. Pérez
Fecha: 2026-03-25
Hora: 10:00

Opción: 3
Cédula: 123456789
Diagnóstico: Gripe común

Opción: 4
Cédula: 123456789
Monto: 50
⚠️ Limitaciones

Este sistema es una versión básica y presenta algunas limitaciones:

❌ No guarda datos de forma persistente
❌ No hay validación avanzada de entradas
❌ No se gestionan múltiples usuarios con autenticación
❌ No hay interfaz gráfica
🛠️ Posibles mejoras
💾 Integración con base de datos (SQLite, PostgreSQL)
🔐 Sistema de autenticación de usuarios
📊 Reportes médicos y financieros
🌐 Interfaz web (Flask / Django)
⏰ Validación avanzada de fechas y horarios
