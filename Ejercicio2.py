from Ejercicio1 import Usuario
from Ejercicio1 import Libro

class Bibloteca:
    def __init__(self, nombre_biblo, direccion_biblo, telefono_biblo, email_biblo, horario_atencion):
        self.nombre_biblo = nombre_biblo
        self.direccion_biblo = direccion_biblo
        self.telefono_biblo = telefono_biblo
        self.email_biblo = email_biblo
        self.horario_atencion = horario_atencion
        self.libros_disponibles = []
        self.usuarios = {}
        self.prestamos = {}
        
        
    def ingresar_usuario(self, nombre, direccion, telefono, email, fecha_nacimiento):
        if nombre not in self.usuarios: #para no ingresar nombres duplicados
            nuevo_usuario = Usuario(nombre, direccion, telefono, email, fecha_nacimiento)
            self.usuarios[nombre] = nuevo_usuario
            print(f"Usuario '{nombre}' registrado correctamente.")
        else:
            print(f"El usuario '{nombre}' ya está registrado.")
            
    def solicitar_libro(self, nombre_usuario, nombre_libro):
    if nombre_usuario in self.usuarios and nombre_libro in self.libros_disponibles:
        usuario = self.usuarios[nombre_usuario]
        libro = Libro(nombre_libro, None, None, None)  # Crea un objeto Libro temporal para la búsqueda
        if libro not in usuario.libro_prestado_usuario:  # Verifica si el libro está disponible para el usuario
            print(f"El usuario {nombre_usuario} desea solicitar el libro '{nombre_libro}'.")
            # Implementar lógica para procesar la solicitud (por ejemplo, agregar a una cola de espera, notificar al bibliotecario, etc.)
        else:
            print(f"El usuario {nombre_usuario} ya tiene prestado el libro '{nombre_libro}'.")
    else:
        if nombre_usuario not in self.usuarios:
            print(f"El usuario '{nombre_usuario}' no está registrado en la biblioteca.")
        elif nombre_libro not in self.libros_disponibles:
            print(f"El libro '{nombre_libro}' no está disponible para préstamo.")
        
        
            

bibloteca1 = Bibloteca ("Biblioteque La Rosa", "La Rosa 547", 154236789, "biblo@larosa.com", "Lun - Vie 12:00 - 18:00")

bibloteca1.ingresar_usuario("Juan Perez", "Av. Corrientes 4657", 1536690663, "juan@perez.com", "24/10/1979")
bibloteca1.ingresar_usuario("Matias Alessandrello", "Av.Libertad 1234", 1536690663, "mati@correo.com.ar", "31/01/1967")


