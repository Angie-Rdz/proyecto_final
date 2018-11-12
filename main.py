from Youtube import *
from base_de_datos import SQlite
from dos_youtube import AppYoutube
from dos_youtube import videos
from time import sleep
import sqlite3
import random
conexion = sqlite3.connect('Youtube.db')
cursor = conexion.cursor()

def GuardarVideo(AppYoutube):
    def InfoVideo(self, url):
        ID=random.randrange(100)
        y = AppYoutube()
        vid = y.InfoVideo()
        #cursor.execute("INSERT INTO VIDEO (ID,NOMBRE,DURACION,CANAL,FECHA,LIKES,VISTAS,DESCRIPCION,COMPARTIDAS)VALUES(?,?,?,?,?,?,?,?,?)",(ID,vid.Titulo,vid.Duracion,vid.NombreCanal,vid.Fecha,vid.Likes,vid.Descripcion,150))
        #conexion.commit()#guarda cambios
        Guardar_Video=cursor.execute("INSERT INTO VIDEO (ID,NOMBRE,DURACION,CANAL,FECHA,LIKES,VISTAS,DESCRIPCION,COMPARTIDAS)VALUES(?,?,?,?,?,?,?,?,?)",(ID,vid.Titulo,vid.Duracion,vid.NombreCanal,vid.Fecha,vid.Likes,vid.Descripcion,150))
        conexion.commit()#guarda cambios)
        return Guardar_Video.fetchall()
        cursor.close()


def MostrarLista():
    #cursor.execute("SELECT * from VIDEO")
    #conexion.commit()
    MostrarLista=cursor.execute("SELECT * from VIDEO")
    return MostrarLista.fetchall()
    cursor.close()

def MostrarVideo(AppYoutube):
    X=input("Para ver un VIDEO ingresa el ID:")
    cursor.execute("SELECT * from VIDEO WHERE ID=?",(X,))
    conexion.commit()
    MostrarVideo=cursor.execute("SELECT * from VIDEO WHERE ID=?",(X,))
    return MostrarVideo.fetchall()
    cursor.close()

def ModificarVideo():
    X=input("Ingrese el id del video que desea modificar:")
    Compartidas=int(input("ingrese el numero de veces compartido"))
    cursor.execute("Update VIDEO SET Compartidas=? WHERE ID=?",(Compartidas,X))
    conexion.commit()
    ModificarVideo=cursor.execute("Update VIDEO SET Compartidas=? WHERE ID=?",(Compartidas,X))
    return ModificarVideo.fetchall()
def BorarVideo(equipoRepo,id):
    X=input("Ingrese el id del video que desea eliminar:")
    cursor.execute("DELETE FROM VIDEO WHERE ID=?",(X,))
    conexion.commit()
    BorrarVideo=cursor.execute("DELETE VIDEO WHERE ID=?",(X,))
    return BorrarVideo.fetchall()


def main():
    BD = SQlite()
    YT= AppYoutube()
    while True:
        bienvenido = "------------- Bienvenido ------------"
        opcion = int(input("-----Menu----- \n1.Guardar video \n2.Ver Lista de videos guardados \n3.Ver Video \n4.Modificar video \n5.Borrar video \n0.Salir\n"))
        if opcion == 1:
            if MostrarLista() == None:
                print("No hay videos guardados")
            else:
                ID=random.randrange(100000)
                y = AppYoutube()
                url=input("Ingrese url: ")
                Compartidas=int(input("Ingrese numero de veces compartido: "))
                vid = y.InfoVideo(url)
                #cursor.execute("INSERT INTO VIDEO (ID,NOMBRE,DURACION,CANAL,FECHA,LIKES,VISTAS,DESCRIPCION,COMPARTIDAS) VALUES(?,?,?,?,?,?,?,?,?)",(ID,vid.Titulo,vid.Duracion,vid.NombreCanal,vid.Fecha,vid.Likes,vid.Vistas,vid.Descripcion,Compartidas))
                #conexion.commit()#guarda cambios
                Guardar_Video=cursor.execute("INSERT INTO VIDEO (ID,NOMBRE,DURACION,CANAL,FECHA,LIKES,VISTAS,DESCRIPCION,COMPARTIDAS) VALUES(?,?,?,?,?,?,?,?,?)",(ID,vid.Titulo,vid.Duracion,vid.NombreCanal,vid.Fecha,vid.Likes,vid.Vistas,vid.Descripcion,Compartidas))
                print("Se creo el video")
                conexion.commit()#guarda cambios
                F=input("Presiona cualquier tecla para continuar...")
                continue
                #return Guardar_Video.fetchall()
                #cursor.close()

                #continue

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

            print(MostrarVideo(AppYoutube))
            F=input("Presiona cualquier tecla para continuar...")
            continue

        elif opcion == 4:

            X=input("Ingrese el id del video que desea modificar:")
            Compartidas=int(input("ingrese el numero de veces compartido: "))
            #cursor.execute("Update VIDEO SET Compartidas=? WHERE ID=?",(Compartidas,X))
            ModificarVideo=cursor.execute("Update VIDEO SET Compartidas=? WHERE ID=?",(Compartidas,X))
            print("Video modificado correctamente")
            conexion.commit()
            F=input("Presiona cualquier tecla para continuar...")
            #return ModificarVideo.fetchall()
            continue


        elif opcion == 5:
            X=input("Ingrese el id del video que desea eliminar:")
            BorrarVideo=cursor.execute("DELETE FROM VIDEO WHERE ID=?",(X,))
            print("Video eliminado")
            conexion.commit()
            F=input("Presiona cualquier tecla para continuar...")
            continue
            #return BorrarVideo.fetchall()

        elif opcion == 0:
            print("Saliendo del menú...")
            sleep(1)
            break

if __name__ == '__main__':
    main()
