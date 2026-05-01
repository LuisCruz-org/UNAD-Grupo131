#SOFTWARE FJ
from abc import ABC, abstractmethod  # importar para clases abstractas

class Entidad(ABC):
    def __init__(self, codigo):
        self._codigo = codigo  # atributo para identificar objetos

    @abstractmethod
    def mostrar_info(self):
        pass  


class Cliente(Entidad):
    def __init__(self, codigo, nombre, correo, telefono):
        super().__init__(codigo)  # clase heredada

        if not nombre:
            raise ValueError("El nombre no puede estar vacío")  # valida nombre

        if "@" not in correo:
            raise ValueError("Correo inválido")  # valida correo

        if not telefono.isdigit():
            raise ValueError("El teléfono debe tener solo números")  # valida teléfono

        self.__nombre = nombre  
        self.__correo = correo  
        self.__telefono = telefono  

    def get_nombre(self):
        return self.__nombre  # devuelve nombre

    def get_correo(self):
        return self.__correo  # devuelve correo

    def get_telefono(self):
        return self.__telefono  # devuelve teléfono

    def mostrar_info(self):
        print(f"Código: {self._codigo} | Cliente: {self.__nombre} | Correo: {self.__correo} | Tel: {self.__telefono}")  # muestra datos