# 📦 Importamos la clase Menu desde el archivo menu.py
from menu import Menu

# 📋 Definimos las opciones del menú con emojis para mejorar la experiencia visual
opciones_menu = [
    '1. ✍️  Crear',       # ✍️ Permite al usuario agregar un nuevo registro
    '2. 📄 Leer',         # 📄 Muestra todos los registros existentes
    '3. ✏️  Actualizar',  # ✏️ Modifica un registro existente
    '4. 🗑️  Borrar',      # 🗑️ Elimina un registro por ID
    '0. 🚪 Salir'         # 🚪 Finaliza el programa
]

# 📱 Creamos una instancia de la clase Menu
# 📏 Le pasamos el ancho en caracteres del menú (45), el título 'CRUD', y la lista de opciones
mostrar_menu = Menu(45, 'CRUD', opciones_menu)

# 📢 Mostramos el menú al usuario y gestionamos la navegación
mostrar_menu.imprimir_menu()