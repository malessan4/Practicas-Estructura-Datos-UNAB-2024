class Usuario:
    def __init__(self, nombre_usuario, direccion_usuario, telefono_usuario, email_usuario, fecha_nacimiento_usuario):
        self.nombre_usuario = nombre_usuario
        self.direccion_usuario = direccion_usuario
        self.telefono_usuario = telefono_usuario
        self.email_usuario = email_usuario
        self.fecha_nacimiento_usuario = fecha_nacimiento_usuario

    
    def cambiar_nombre_usuario (self, nuevo_nombre_usuario):
        self.nombre_usuario = nuevo_nombre_usuario
    
    def cambiar_direccion_usuario (self, nueva_direccion_usuario):
        self.direccion_usuario = nueva_direccion_usuario
    
    def cambiar_telefono_usuario (self, nuevo_telefono_usuario):
        self.telefono_usuario = nuevo_telefono_usuario
    
    def cambiar_email_usuario (self, nuevo_email_usuario):
        self.email_usuario = nuevo_email_usuario
    
    def cambiar_fecha_nacimiento_usuario (self, nueva_fecha_nacimiento_usuario):
        self.fecha_nacimiento_usuario = nueva_fecha_nacimiento_usuario

    def recibir_mensaje (self, mensaje):
        print(f"Mensaje recibido para {self.nombre_usuario}: {mensaje}")
        


class Libro:
    def __init__(self, nombre_libro, edicion, fecha_publicacion, sinopsis):
        self.nombre_libro = nombre_libro
        self.edicion = edicion
        self.fecha_publicacion = fecha_publicacion
        self.sinopsis = sinopsis
    
    def cambiar_nombre_libro (self, nuevo_nombre_libro):
        self.nombre_libro = nuevo_nombre_libro

    def cambiar_edicion (self, nueva_edicion):
        self.edicion = nueva_edicion

    def cambiar_fecha_publicacion (self, nueva_fecha_publicacion):
        self.fecha_publicacion = nueva_fecha_publicacion
    
    def cambiar_sinopsis (self, nueva_sinopsis):
        self.sinopsis = nueva_sinopsis


# Puesta a prueba 

usuario1 = Usuario("Matias Alessandrello", "Av.Libertad 1234", 1536690663, "mati@correo.com.ar", "31/01/1967")
usuario2 = Usuario("Daniel Leso", "Av.Corrientes 1234", 1536690754, "dani@correo.com.ar", "10/05/1988")

libro1 = Libro ("El señor de los anillos", "D&D", "1969", "Pelar por el Anillo del Poder")
libro2 = Libro ("Teoria de La Estetica del Arte", "Alianza", "1969", "Libro de la Estetica del Arte")

mensaje = "Hola Matias"
usuario1.recibir_mensaje(mensaje)

mensaje = "Hola dani"
usuario2.recibir_mensaje(mensaje)
