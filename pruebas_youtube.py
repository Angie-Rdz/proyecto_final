import unittest
from unittest.mock import Mock
from dos_youtube import AppYoutube
from base_de_datos import SQlite
from Youtube import Video, AbstractRepo, AbstractYoutube

class TestYTapp(unittest.TestCase):

    def setUp(self):

        self.yt = AppYoutube()
        self.videomock = Mock(Id = 5, Nombre = "MIRANDA.-PERFECTA", Duracion = "PT3M45S", Canal = "Xaxiri Castro",  Fecha= "2008-03-28T21:54:50.000Z", Likes = self.yt.InfoVideo("https://www.youtube.com/watch?v=dDmhThqxDw0").Likes, Vistas = self.yt.InfoVideo("https://www.youtube.com/watch?v=dDmhThqxDw0").Vistas, Descripcion = "BUENA ROLA DE ESTE GRUPO ARGENTINO!!!")
        self.video = Video(self.videomock.Nombre,self.videomock.Duracion,self.videomock.Canal,self.videomock.Fecha,self.videomock.Likes,self.videomock.Vistas,self.videomock.Descripcion)
        self.sql = SQlite()
        self.sql.GuardarVideo(self.video)

        ################################
        self.video2 = Video('video1',12,'El video', "25 feb 2018", 2500, 10000,'video')

    #Hace las pruebas de guardar un video y que todos sus atributos estén almacenados correctamente
    def test_Video(self):

        print("test_Video")
        self.assertEqual(self.video2.Nombre, ('video1'))
        self.assertEqual(self.video2.Duracion, 12 )
        self.assertEqual(self.video2.Canal, 'El video' )
        self.assertEqual(self.video2.Fecha, "25 feb 2018" )
        self.assertEqual(self.video2.Likes, 2500 )
        self.assertEqual(self.video2.Vistas, 10000 )
        self.assertEqual(self.video2.Descripcion, 'video' )

        #Revisando el tipo de dato
        self.assertNotEqual(self.video2.Duracion, '12')
        self.assertNotEqual(self.video2.Likes, '2500' )
        self.assertNotEqual(self.video2.Vistas, '10000' )


    def test_modVideo(self):

        print("test_modVideo")
        self.assertTrue(self.sql.ModificarVideo(self.video))

    def test_borrar(self):

        print("test_borrar")
        self.assertTrue(self.sql.BorrarVideo(5))




    def test_infoVideo(self):

        print("test_infoVideo")
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=dDmhThqxDw0").Nombre, self.video.Nombre)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=dDmhThqxDw0").Duracion, self.video.Duracion)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=dDmhThqxDw0").Canal, self.video.Canal)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=dDmhThqxDw0").Fecha, self.video.Fecha)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=dDmhThqxDw0").Likes, self.video.Likes)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=dDmhThqxDw0").Vistas, self.video.Vistas)
        self.assertEqual(self.yt.InfoVideo("https://www.youtube.com/watch?v=dDmhThqxDw0").Descripcion, self.video.Descripcion)


if __name__ == '__main__':
    unittest.main()
