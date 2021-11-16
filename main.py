from raytracer import *

mirror = Material(diffuse=color(255, 255, 255), albedo=(0, 10, 0.8, 0), spec=1425)
glass = Material(diffuse=color(150, 180, 200), albedo=(0, 0.5, 0.1, 0.8), spec=125, refractive_index=1.5)
blue1 = Material(diffuse=color(8, 16, 94), albedo=(0.9,  0.9, 0, 0), spec=10)
blue2 = Material(diffuse=color(27, 37, 102), albedo=(0.9,  0.9, 0, 0), spec=10)
blue3 = Material(diffuse=color(21, 31, 102), albedo=(0.9,  0.9, 0, 0), spec=10)
white = Material(diffuse=color(250, 250, 250), albedo=(0.9,  0.9, 0, 0), spec=10)
edificio1 = Material(texture=Texture('./materiales/textura1.bmp'))
edificio2 = Material(texture=Texture('./materiales/textura2.bmp'))
edificio3 = Material(texture=Texture('./materiales/textura3.bmp'))
edificio4 = Material(texture=Texture('./materiales/textura4.bmp'))
edificio5 = Material(texture=Texture('./materiales/textura5.bmp'))
edificio6 = Material(texture=Texture('./materiales/textura6.bmp'))
edificio7 = Material(texture=Texture('./materiales/textura7.bmp'))

r = Raytracer(1024, 1024)

r.light = Light(position=V3(-20, 10, 20), intensity=1.5)
r.background_color = color(50, 50, 200)

r.scene = [

  #edificio1
  Cube(V3(-1.8, -1.8, -21), 1.4, edificio1),
  Cube(V3(-1.8, -2.2, -21), 1.4, edificio1),
  Cube(V3(-1.8, -2.6, -21), 1.4, edificio1),
  Cube(V3(-1.8, -3.0, -21), 1.4, edificio1),
  Cube(V3(-1.8, -3.4, -21), 1.4, edificio1),
  Cube(V3(-1.8, -3.8, -21), 1.4, edificio1),
  Cube(V3(-1.8, -4.2, -21), 1.4, edificio1),
  Cube(V3(-1.8, -4.6, -21), 1.4, edificio1),
  Cube(V3(-1.8, -5.0, -21), 1.4, edificio1),
  Cube(V3(-1.8, -5.4, -21), 1.4, edificio1),
  Cube(V3(-1.8, -5.7, -21), 1.4, edificio1),

  #edificio2
  Cube(V3(0, -2.9, -20), 1.9, edificio2),
  Cube(V3(0, -3.3, -20), 1.9, edificio2),
  Cube(V3(0, -3.7, -20), 1.9, edificio2),
  Cube(V3(0, -4.1, -20), 1.9, edificio2),
  Cube(V3(0, -4.5, -20), 1.9, edificio2),
  Cube(V3(0, -4.9, -20), 1.9, edificio2),
  Cube(V3(0, -5.3, -20), 1.9, edificio2),
  Cube(V3(0, -5.6, -20), 1.9, edificio2),

  #edificio3
  Cube(V3(1.5, -0.8, -22), 1.9, edificio3),
  Cube(V3(1.5, -1.2, -22), 1.9, edificio3),
  Cube(V3(1.5, -1.6, -22), 1.9, edificio3),
  Cube(V3(1.5, -2.0, -22), 1.9, edificio3),
  Cube(V3(1.5, -2.4, -22), 1.9, edificio3),
  Cube(V3(1.5, -2.8, -22), 1.9, edificio3),
  Cube(V3(1.5, -3.2, -22), 1.9, edificio3),
  Cube(V3(1.5, -3.6, -22), 1.9, edificio3),
  Cube(V3(1.5, -4.0, -22), 1.9, edificio3),
  Cube(V3(1.5, -4.4, -22), 1.9, edificio3),
  Cube(V3(1.5, -4.8, -22), 1.9, edificio3),
  Cube(V3(1.5, -5.2, -22), 1.9, edificio3),
  Cube(V3(1.5, -5.6, -22), 1.9, edificio3),

  #edificio4
  Cube(V3(-3.3, -1.1, -19), 1.7, edificio4),
  Cube(V3(-3.3, -1.5, -19), 1.7, edificio4),
  Cube(V3(-3.3, -1.9, -19), 1.7, edificio4),
  Cube(V3(-3.3, -2.3, -19), 1.7, edificio4),
  Cube(V3(-3.3, -2.7, -19), 1.7, edificio4),
  Cube(V3(-3.3, -3.1, -19), 1.7, edificio4),
  Cube(V3(-3.3, -3.4, -19), 1.7, edificio4),
  Cube(V3(-3.3, -3.8, -19), 1.7, edificio4),
  Cube(V3(-3.3, -4.2, -19), 1.7, edificio4),
  Cube(V3(-3.3, -4.6, -19), 1.7, edificio4),
  Cube(V3(-3.3, -5.0, -19), 1.7, edificio4),
  Cube(V3(-3.3, -5.4, -19), 1.7, edificio4),
  Cube(V3(-3.3, -5.8, -19), 1.7, edificio4),

  #edificio5
  Cube(V3(2.4, -2.9, -20), 2, edificio5),
  Cube(V3(2.4, -3.3, -20), 2, edificio5),
  Cube(V3(2.4, -3.7, -20), 2, edificio5),
  Cube(V3(2.4, -4.1, -20), 2, edificio5),
  Cube(V3(2.4, -4.5, -20), 2, edificio5),
  Cube(V3(2.4, -4.9, -20), 2, edificio5),
  Cube(V3(2.4, -5.3, -20), 2, edificio5),
  Cube(V3(2.4, -5.6, -20), 2, edificio5),

  #edificio 6
  Cube(V3(-5.3, -2.0, -24), 2, edificio6),
  Cube(V3(-5.3, -2.4, -24), 2, edificio6),
  Cube(V3(-5.3, -2.8, -24), 2, edificio6),
  Cube(V3(-5.3, -3.2, -24), 2, edificio6),
  Cube(V3(-5.3, -3.6, -24), 2, edificio6),
  Cube(V3(-5.3, -4.0, -24), 2, edificio6),
  Cube(V3(-5.3, -4.4, -24), 2, edificio6),
  Cube(V3(-5.3, -4.8, -24), 2, edificio6),
  Cube(V3(-5.3, -5.2, -24), 2, edificio6),
  Cube(V3(-5.3, -5.6, -24), 2, edificio6),

  Cube(V3(-6.1, -2.0, -24), 2, edificio6),
  Cube(V3(-6.1, -2.4, -24), 2, edificio6),
  Cube(V3(-6.1, -2.8, -24), 2, edificio6),
  Cube(V3(-6.1, -3.2, -24), 2, edificio6),
  Cube(V3(-6.1, -3.6, -24), 2, edificio6),
  Cube(V3(-6.1, -4.0, -24), 2, edificio6),
  Cube(V3(-6.1, -4.4, -24), 2, edificio6),
  Cube(V3(-6.1, -4.8, -24), 2, edificio6),
  Cube(V3(-6.1, -5.2, -24), 2, edificio6),
  Cube(V3(-6.1, -5.6, -24), 2, edificio6),

  #edificio 7
  Cube(V3(4.9, -0.5, -21), 1.6, edificio7),
  Cube(V3(4.9, -0.9, -21), 1.6, edificio7),
  Cube(V3(4.9, -1.3, -21), 1.6, edificio7),
  Cube(V3(4.9, -1.7, -21), 1.6, edificio7),
  Cube(V3(4.9, -2.1, -21), 1.6, edificio7),
  Cube(V3(4.9, -2.5, -21), 1.6, edificio7),
  Cube(V3(4.9, -2.9, -21), 1.6, edificio7),
  Cube(V3(4.9, -3.3, -21), 1.6, edificio7),
  Cube(V3(4.9, -3.7, -21), 1.6, edificio7),
  Cube(V3(4.9, -4.1, -21), 1.6, edificio7),
  Cube(V3(4.9, -4.5, -21), 1.6, edificio7),
  Cube(V3(4.9, -4.9, -21), 1.6, edificio7),
  Cube(V3(4.9, -5.3, -21), 1.6, edificio7),
  Cube(V3(4.9, -5.6, -21), 1.6, edificio7),

  #lago
  Cube(V3(0, -17, -9), 20, blue1),

  #edificio en lago
  Sphere(V3(-3.5, -7.5, -17), 2, mirror),

  #ramiel
  Triangulo(V3(1, 3.5, -10), V3(0, 5, -10), V3(-2, 3.5, -10), blue2),
  Triangulo(V3(1, 3.5, -10), V3(0, 5, -10), V3(1.8, 3.5, -10), glass),
  Triangulo(V3(0, 5, -10), V3(1.8, 3.5, -10), V3(-2, 3.5, -10), glass),
  Triangulo(V3(0, 5, -10), V3(1.8, 3.5, -10), V3(-2, 3.5, -10), glass),

  Triangulo(V3(-2, 3.5, -10), V3(0, 2, -10), V3(1, 3.5, -10), blue3),
  Triangulo(V3(1.8, 3.5, -10), V3(0, 2, -10),V3(1, 3.5, -10), blue3),
  Triangulo(V3(0, 2, -10), V3(-2, 3.5, -10), V3(1.8, 3.5, -10), blue3),
  Triangulo(V3(0, 2, -10), V3(-2, 3.5, -10), V3(1.8, 3.5, -10), blue3),
]

r.envmap = Envmap('./materiales/envmap.bmp')
r.render()
r.write('out.bmp')