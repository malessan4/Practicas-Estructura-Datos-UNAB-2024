import pytest
from datetime import datetime, timedelta
from Ejercicio1 import Usuario, Libro
from Ejercicio2 import Biblioteca

@pytest.fixture
def biblioteca():
    return Biblioteca("Biblioteca Central", "Avenida Principal 123", "987654321", "contacto@biblioteca.com", "Lunes a Viernes, 9am a 6pm")

@pytest.fixture
def usuario1():
    return Usuario("Juan Pérez", "Calle Falsa 123", "123456789", "juan@example.com", "01/01/1990")

@pytest.fixture
def libro1():
    return Libro("Python para Todos", "2da Edición", "2022-01-01", "Una guía completa para aprender Python.")

@pytest.fixture
def libro2():
    return Libro("Machine Learning Avanzado", "1ra Edición", "2021-05-15", "Todo sobre machine learning.")

def test_ingresar_usuario(biblioteca, usuario1):
    biblioteca.ingresar_usuario(usuario1)
    assert any(u.nombre == usuario1.nombre for u in biblioteca.usuarios)

def test_prestar_libro(biblioteca, usuario1, libro1):
    biblioteca.libros_disponibles.insertar(libro1)
    biblioteca.ingresar_usuario(usuario1)
    biblioteca.prestar_libro(usuario1, libro1)
    assert any(l.nombre == libro1.nombre for l in usuario1.libros_prestados)

def test_devolver_libro(biblioteca, usuario1, libro1):
    biblioteca.libros_disponibles.insertar(libro1)
    biblioteca.ingresar_usuario(usuario1)
    biblioteca.prestar_libro(usuario1, libro1)
    biblioteca.devolver_libro(usuario1, libro1)
    assert not any(l.nombre == libro1.nombre for l in usuario1.libros_prestados)
    assert any(l.nombre == libro1.nombre for l in biblioteca.libros_disponibles)

def test_verificar_prestamos_vencidos(biblioteca, usuario1, libro2):
    biblioteca.libros_disponibles.insertar(libro2)
    biblioteca.ingresar_usuario(usuario1)
    biblioteca.prestar_libro(usuario1, libro2)
    # Simular que el libro ya está vencido
    for i, prestamo in enumerate(biblioteca.libros_prestados):
        libro, usuario, fecha_vencimiento = prestamo
        if libro.nombre == libro2.nombre:
            biblioteca.libros_prestados.eliminar(prestamo)
            biblioteca.libros_prestados.insertar((libro, usuario, datetime.now() - timedelta(days=1)))
    biblioteca.verificar_prestamos_vencidos()
    assert "El préstamo del libro Machine Learning Avanzado ha vencido." in usuario1.mostrar_mensajes()

def test_guardar_y_cargar_listas(biblioteca, libro1, libro2):
    biblioteca.libros_disponibles.insertar(libro1)
    biblioteca.libros_disponibles.insertar(libro2)
    biblioteca.guardar_listas()
    biblioteca_cargada = Biblioteca("Biblioteca Central", "Avenida Principal 123", "987654321", "contacto@biblioteca.com", "Lunes a Viernes, 9am a 6pm")
    assert any(l.nombre == libro1.nombre for l in biblioteca_cargada.libros_disponibles)
    assert any(l.nombre == libro2.nombre for l in biblioteca_cargada.libros_disponibles)
