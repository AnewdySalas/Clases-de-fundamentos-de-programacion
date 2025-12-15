import os

def crear_archivo():
    nombre_archivo = input("Ingrese el nombre del archivo (sin extensión): ")
    nombre_archivo += ".txt"
    
    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write("")
        print(f"\n Archivo '{nombre_archivo}' creado exitosamente\n")
    except Exception as e:
        print(f"\n Error al crear el archivo: {e}\n")

def guardar_registros():
    
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    if not nombre_archivo.endswith('.txt'):
        nombre_archivo += ".txt"
    
    if not os.path.exists(nombre_archivo):
        print(f"\n El archivo '{nombre_archivo}' no existe\n")
        return
    
    print("\n--- Ingrese los datos del registro ---")
    nombre = input("NOMBRE: ")
    matricula = input("MATRICULA: ")
    correo = input("CORREO: ")
    telefono = input("TELEFONO: ")
    
    try:
        with open(nombre_archivo, 'a', encoding='utf-8') as archivo:
            archivo.write(f"NOMBRE: {nombre}\n")
            archivo.write(f"MATRICULA: {matricula}\n")
            archivo.write(f"CORREO: {correo}\n")
            archivo.write(f"TELEFONO: {telefono}\n")
            archivo.write("-" * 40 + "\n")
        print(f"\n✓ Registro guardado exitosamente\n")
    except Exception as e:
        print(f"\n✗ Error al guardar el registro: {e}\n")

def leer_archivo():
    """Lee y muestra el contenido del archivo"""
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    if not nombre_archivo.endswith('.txt'):
        nombre_archivo += ".txt"
    
    if not os.path.exists(nombre_archivo):
        print(f"\n✗ El archivo '{nombre_archivo}' no existe\n")
        return
    
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
            if contenido.strip():
                print("\n" + "=" * 40)
                print("CONTENIDO DEL ARCHIVO")
                print("=" * 40)
                print(contenido)
            else:
                print("\n⚠ El archivo está vacío\n")
    except Exception as e:
        print(f"\n Error al leer el archivo: {e}\n")

def actualizar_nombre():
   
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    if not nombre_archivo.endswith('.txt'):
        nombre_archivo += ".txt"
    
    if not os.path.exists(nombre_archivo):
        print(f"\n El archivo '{nombre_archivo}' no existe\n")
        return
    
    nombre_buscar = input("Ingrese el nombre a buscar: ")
    nombre_nuevo = input("Ingrese el nuevo nombre: ")
    
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()
        
        encontrado = False
        for i, linea in enumerate(lineas):
            if linea.startswith("NOMBRE: ") and nombre_buscar in linea:
                lineas[i] = f"NOMBRE: {nombre_nuevo}\n"
                encontrado = True
        
        if encontrado:
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                archivo.writelines(lineas)
            print(f"\n Nombre actualizado exitosamente\n")
        else:
            print(f"\n No se encontró el nombre '{nombre_buscar}'\n")
    except Exception as e:
        print(f"\n Error al actualizar el archivo: {e}\n")

def mostrar_menu():
 
    print("=" * 40)
    print("  SISTEMA DE GESTIÓN DE ARCHIVOS")
    print("=" * 40)
    print("1. Crear archivo")
    print("2. Guardar registros")
    print("3. Leer archivo")
    print("4. Actualizar nombre")
    print("5. Cerrar")
    print("=" * 40)

def main():
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            crear_archivo()
        elif opcion == "2":
            guardar_registros()
        elif opcion == "3":
            leer_archivo()
        elif opcion == "4":
            actualizar_nombre()
        elif opcion == "5":
            print("\n¡Hasta luego! \n")
            break
        else:
            print("\n Opción inválida. Intente de nuevo.\n")

if __name__ == "__main__":
    main()