# POO

# Todo es un objeto

# Ejemplo modelar una app para un club - club Pepi -  ejemplo a puro diccionarios

club_pepi = {
    # Propiedades o atributos
    "nombre": "Club Pepi",
    "miembros": [],
    "eventos": []
    # Métodos o funciones
    "agregar_miembro": lambda miembro: club_pepi["miembros"].append(miembro),
    "agregar_evento": lambda evento: club_pepi["eventos"].append(evento)
}

socio = {
    "nombre": "Juan Perez",
    "edad": 30,
    "membresia": "Premium",
    "actividades": [],
    # Métodos o funciones
    "mostrar_info": lambda: print(f"Nombre: {socio['nombre']},
    Edad: {socio['edad']}, Membresía: {socio['membresia']}") 
    
}

actividades = {
    "nombre": "Yoga",
    "fecha": "2024-10-15",
    "hora": "18:00"
    # Métodos o funciones
    "mostrar_detalles": lambda: print(f"Actividad: {actividades['nombre']},
                                    
    