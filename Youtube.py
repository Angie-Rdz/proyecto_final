from abc import ABC, abstractmethod


class Video():
    def __init__(self, nombre, duracion, canal, fecha, likes, vistas, descripcion, id=None, categorias=None):
        self.Id = id
        self.Nombre = nombre
        self.Duracion = duracion
        self.Canal = canal
        self.Categorias = categorias
        self.Fecha = fecha
        self.Likes = likes
        self.Vistas = vistas
        self.Descripcion = descripcion


class Categoria():
    def __init__(self, id, nombre):
        self.Id = id
        self.Nombre = nombre


class AbstractRepo(ABC):
    @abstractmethod
    def GuardarVideo(self, video):
        pass

    @abstractmethod
    def MostrarLista(self):
        pass

    @abstractmethod
    def MostrarVideo(self, id):
        pass

    @abstractmethod
    def ModificarVideo(self, video):
        pass

    @abstractmethod
    def BorrarVideo(self, id):
        pass


class AbstractYoutube(ABC):
    @abstractmethod
    def InfoVideo(self, url):
        pass


if __name__ == "__main__":
    cat = Categoria(24, "algo")
    print(cat.Nombre)
