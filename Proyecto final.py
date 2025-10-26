
from abc import ABC, abstractmethod

# Base abstracta para las entidades principales
class Base(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def necesita_donacion(self):
        pass


# Clases relacionadas con las escuelas
# Podemos pones ademas de clases rurales, indigenas, ehh jodidas, urbanas etc 
class Escuela(Base):
    def __init__(self, nombre, localidad, clave_escuela):
        self.nombre = nombre
        self.localidad = localidad
        self.clave_escuela = clave_escuela
        self.utiles_recibidos = []
        self.recibio_donacion = False

    def necesita_donacion(self):
        pass

    def __str__(self):
        pass


class EscuelaRural(Escuela):
    def __init__(self, nombre, localidad, clave_escuela):
        super().__init__(nombre, localidad, clave_escuela)

    def necesita_donacion(self):
        pass

    def __str__(self):
        pass


# Clases de útiles 
# aqui pones un chorro de todos los utiles y esta pelao
class Util:
    def __init__(self, nombre, tipo, cantidad):
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad

    def __str__(self):
        pass
class libro(Util):
    def __init__(self, nombre, tipo, cantidad,grado):
        super.__init__(self,nombre, tipo, cantidad)
        self.grado = grado
    def __str__(self):
        pass
    


class UtilEscolar(Util):
    def __init__(self, nombre, tipo, cantidad):
        super().__init__(nombre, tipo, cantidad)

    def __str__(self):
        pass


# Clases de donaciones
# subclases del tipo de donacion/descartable
class Donacion:
    def __init__(self, escuela, fecha, donador,donacion):
        self.escuela = escuela
        self.donacion = donacion
        self.fecha = fecha
        self.donador = donador

    def registrar_envio(self):
        pass

    def __str__(self):
        pass
class DonacionTecnologica(Donacion):
    def __init__(self, escuela, lista_utiles, fecha, donador,donacion):
        pass


# Clases de gestión
class Inventario:
    def __init__(self):
        self.lista_utiles = []

    def agregar_util(self, util):
        pass

    def eliminar_util(self, nombre_util):
        pass

    def buscar_util(self, nombre_util):
        pass

    def __str__(self):
        pass


class GestorDonaciones(ABC):
    def __init__(self, inventario):
        self.inventario = inventario
        self.historial_donaciones = []

    def crear_donacion(self, escuela, lista_utiles, donador):
        pass

    def buscar_donaciones_por_escuela(self, nombre_escuela):
        pass

    def __str__(self):
        pass
class GestorRegional(GestorDonaciones):
    def __init__(self, inventario, region):
        super().__init__(inventario)
        self.region = region

    def crear_donacion(self, escuela, lista_utiles, donador):
        pass

    def buscar_donaciones_por_escuela(self, nombre_escuela):
        pass

    def __str__(self):
        pass
# Envios y maneras de entrrega

class Transporte(ABC):
    def __init__(self, donacion, tipo_transporte):
        self.donacion = donacion
        self.tipo_transporte = tipo_transporte

    @abstractmethod
    def entregar(self):
        pass


class Terrestre(Transporte):
    def __init__(self, donacion):
        super().__init__(donacion, "Terrestre")

    def entregar(self):
        pass






