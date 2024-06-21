import pytest
from Ejercicio1 import Usuario, Libro

# Pruebas para la clase Usuario

def test_crear_usuario():
    usuario = Usuario("Juan Pérez", "Calle Falsa 123", "123456789", "juan@example.com", "01/01/1990")
    assert usuario.nombre == "Juan Pérez"
    assert usuario.direccion == "Calle Falsa 123"
    assert usuario.telefono == "123456789"
    assert usuario.email == "juan@example.com"
    assert usuario.fecha_nacimiento == "01/01/1990"

def test_cambiar_datos_usuario():
    usuario = Usuario("Juan Pérez", "Calle Falsa 123", "123456789", "juan@example.com", "01/01/1990")
    usuario.cambiar_nombre("Juan P.")
    usuario.cambiar_direccion("Avenida Siempre Viva 742")
    usuario.cambiar_telefono("987654321")
    usuario.cambiar_email("juanp@example.com")
    usuario.cambiar_fecha_nacimiento("02/02/1990")
    assert usuario.nombre == "Juan P."
    assert usuario.direccion == "Avenida Siempre Viva 742"
    assert usuario.telefono == "987654321"
    assert usuario.email == "juanp@example.com"
    assert usuario.fecha_nacimiento == "02/02/1990"

def test_recibir_mensaje():
    usuario = Usuario("Juan Pérez", "Calle Falsa 123", "123456789", "juan@example.com", "01/01/1990")
    usuario.recibir_mensaje("Bienvenido a la biblioteca, Juan!")
    usuario.recibir_mensaje("Tienes un libro prestado.")
    assert usuario.mostrar_mensajes() == ["Bienvenido a la biblioteca, Juan!", "Tienes un libro prestado."]

# Pruebas para la clase Libro

def test_crear_libro():
    libro = Libro("Python para Todos", "2da Edición", "2022-01-01", "Una guía completa para aprender Python.")
    assert libro.nombre == "Python para Todos"
    assert libro.edicion == "2da Edición"
    assert libro.fecha_publicacion == "2022-01-01"
    assert libro.sinopsis == "Una guía completa para aprender Python."

def test_cambiar_datos_libro():
    libro = Libro("Python para Todos", "2da Edición", "2022-01-01", "Una guía completa para aprender Python.")
    libro.cambiar_nombre("Python para Todos y Todas")
    libro.cambiar_edicion("3ra Edición")
    libro.cambiar_fecha_publicacion("2023-01-01")
    libro.cambiar_sinopsis("Una guía completa y actualizada para aprender Python.")
    assert libro.nombre == "Python para Todos y Todas"
    assert libro.edicion == "3ra Edición"
    assert libro.fecha_publicacion == "2023-01-01"
    assert libro.sinopsis == "Una guía completa y actualizada para aprender Python."

if __name__ == "__main__":
    pytest.main()
