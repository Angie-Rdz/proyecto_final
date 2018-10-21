from Youtube import *
from base_de_datos import SQlite
from dos_youtube import AppYoutube
from time import sleep

def GuardarVideo(AppYoutube, equipoRepo, url, categorias):
    # Buscar video en youtube
    video = AppYoutube.InfoVideo(url)
    # Agregar las categorias
    video.Categorias = categorias
    # Guardar
    new_video = equipoRepo.GuardarVideo(video)
    # Mostrar el id con el que se guardó
    return new_video.Id


def MostrarLista(equipoRepo):
    #regresar datos
    lista = equipoRepo.MostrarLista()
    return lista

def MostrarVideo(equipoRepo,id):
    # recibiendo el ID del video, te debe mostrar el video con sus demás datos
    muestra_video=equipoRepo.MostrarVideo(id)
    return muestra_video

def ModificarVideo(equipoRepo,id):
    modificar = equipoRepo.ModificarVideo(video)
    return modificar

def BorarVideo(equipoRepo,id):
    borrar = equipoRepo.BorrarVideo(id)
    return borrar


def main():
    BD = SQlite()
    YT= AppYoutube()
    while True:
        bienvenido = "------------- Bienvenido ------------"
        opcion = int(input("-----Menu----- 1... Guardar \n2... Ver Lista \n3... Ver Video \n4...  modificar \n5... Borrar \n0... Salir\n"))
        if opcion == 1:
            if MostrarLista() == None:
                print("No hay videos guardados")
            urll = int(input("Ingresa URL para guardar un video :"+"\n"))
            categ = str(input("Ingresa CATEGORIA :"+"\n"))
            print("Se creo el video con el ID: "+GuardarVideo(YT,BD,urll,x))
            continue

        elif opcion == 2:
            if MostrarLista() == None:
                print("No hay videos agregados, regresando al menú...")
                sleep(1)
                continue
            else :
                w=MostrarLista()
                for x in w:
                    print(x)
                F=input("Presiona cualquier tecla para continuar...")
                continue


        elif opcion == 3:
            preg=str(input("Para ver un VIDEO ingresa el ID:"))
            print(MostrarVideo(preg))
            F=input("Presiona cualquier tecla para continuar...")
            continue

        elif opcion == 4:

            print("Escribe el ID del video a MODIFICAR \n\n")

            mod=int(input())
            print(AppYoutube.InfoVideo(mod)+"\n")
            ed=int(input("¿ Qué te gustaria editar ?\n---Descripción, ingresa 1\n---Categoria, ingresa 2\n"))
            #vd = Video()
            if ed == 1:
                vd.Descripcion=str(input("ingresa la nueva descripción :"))
                print("descripción editada")
            elif ed == 2:
                f=str(input("ingresa nueva categoria"))
                vd.Categorias = f
                print("Categoria editada")
                #vid_ed=equipoRepo.ModificarVideo(vd)
            else:
                print("Teclea sólo 1 o 2, regresando al menú...")
                sleep(1)
            continue


        elif opcion == 5:
            MostrarLista()
            eliminar1 = int(input("Ingrese el ID del video a eliminar: "))
            vid = AppYoutube.InfoVideo(eliminar1)
            eliminar2=int(input("Reingrese ID para confirmar que quieres borrar este video: "))
            if eliminar2 == eliminar1:
                BorrarVideo(eliminar2)
            else :
                print("Los ID no coinciden, regresando al menú...")
                sleep(1)
                continue
        elif opcion == 0:
            print("Saliendo del menú...")
            sleep(1)
            break

if __name__ == '__main__':
    main()
