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

    def __str__(self):
        return (f'Biblioteca: {self.nombre}\n'
                f'Dirección: {self.direccion}\n'
                f'Teléfono: {self.telefono}\n'
                f'Email: {self.email}\n'
                f'Horarios: {self.horarios}\n'
                f'Libros disponibles: {len(self.libros_disponibles)}\n'
                f'Usuarios registrados: {len(self.usuarios)}\n'
                f'Libros prestados: {len(self.prestamos)}')

    def agregar_libro(self, nombre_libro, edicion, fecha_publicacion, sinopsis):
        nuevo_libro = Libro(nombre_libro, edicion, fecha_publicacion, sinopsis)
        self.libros_disponibles.append(nombre_libro)
        print(f'Libro "{nombre_libro}" agregado a la biblioteca.')
    
    def ingresar_usuario(self, nombre_usuario, direccion_usuario, telefono_usuario, email_usuario, fecha_nacimiento_usuario):
        if email_usuario in self.usuarios:
            print(f'El usuario con el email "{email_usuario}" ya está registrado.')
        else:
            nuevo_usuario = Usuario(nombre_usuario, direccion_usuario, telefono_usuario, email_usuario, fecha_nacimiento_usuario)
            self.usuarios[email_usuario] = nuevo_usuario
            print(f'Usuario "{nombre_usuario}" registrado con éxito.')

"""
    def prestar_libro(self, usuario_id, libro):
        if usuario_id not in self.usuarios:
            print(f'El usuario con ID {usuario_id} no está registrado.')
            return
        if libro not in self.libros_disponibles:
            print(f'El libro "{libro}" no está disponible.')
            return
        self.libros_disponibles.remove(libro)
        self.prestamos[libro] = usuario_id
        print(f'Libro "{libro}" prestado a usuario "{self.usuarios[usuario_id]}".')

    def aceptar_devolucion(self, libro):
        if libro not in self.prestamos:
            print(f'El libro "{libro}" no está prestado.')
            return
        usuario_id = self.prestamos.pop(libro)
        self.libros_disponibles.append(libro)
        print(f'Libro "{libro}" devuelto por usuario "{self.usuarios[usuario_id]}".')
"""

# Ejemplo de uso
bibloteca = Bibloteca('Bibloteca Central', 'Calle Falsa 123', '123-4567', 'info@biblioteca.com', 'Lun-Vie 9:00-18:00')
libro1 = Libro ("El señor de los anillos", "D&D", "1969", "Una guerra épica por el Anillo del Poder")

bibloteca.agregar_libro("El señor de los anillos", "D&D", "1969", "Pelar por el Anillo del Poder")
bibloteca.agregar_libro("Teoria de La Estetica del Arte", "Alianza", "1969", "Libro de la Estetica del Arte")

bibloteca.ingresar_usuario("Matias Alessandrello", "Av.Libertad 1234", 1536690663, "mati@correo.com.ar", "31/01/1967")

