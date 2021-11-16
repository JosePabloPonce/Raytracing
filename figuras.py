from lib import *
from dataclasses import dataclass
from materiales import *
from math import *

class Plane(object):
  def __init__(self, position, normal, material):
    self.position = position
    self.normal = norm(normal)
    self.material = material

  def ray_intersect(self, orig, direction):
    d = dot(direction, self.normal)
    epsilon = 0.0001

    if abs(d) > epsilon:
      t = dot(self.normal, sub(self.position, orig)) / d
      if t > 0:
        hit = sum(orig, mul(direction, t))

        return Intersect(distance = t,
                         point = hit,
                         normal = self.normal)

    return None

class Sphere(object):
  def __init__(self, center, radius, material):
    self.center = center
    self.radius = radius
    self.material = material

  def ray_intersect(self, orig, direction):
    L = sub(self.center, orig)
    tca = dot(L, direction)
    l = length(L)
    d2 = l**2 - tca**2
    if d2 > self.radius**2:
      return None
    thc = (self.radius**2 - d2)**1/2
    t0 = tca - thc
    t1 = tca + thc
    if t0 < 0:
      t0 = t1
    if t0 < 0:
      return None

    hit = sum(orig, mul(direction, t0))
    normal = norm(sub(hit, self.center))

    return Intersect(
      distance=t0,
      point=hit,
      normal=normal
    )

class Cube(object):
  def __init__(self, position, size, material):
    self.position = position
    self.size = size
    self.material = material
    self.planes = []
    half = size / 2

    self.planes = [
     Plane( sum(position, V3(half,0,0)), V3(1,0,0), material),
     Plane( sum(position, V3(-half,0,0)), V3(-1,0,0), material),
     Plane( sum(position, V3(0,half,0)), V3(0,1,0), material),
     Plane( sum(position, V3(0,-half,0)), V3(0,-1,0), material),
     Plane( sum(position, V3(0,0,half)), V3(0,0,1), material),
     Plane( sum(position, V3(0,0,-half)), V3(0,0,-1), material)
    ]

  def ray_intersect(self, orig, direction):

    epsilon = 0.001
    Bounds_Min = [0,0,0]
    Bounds_Max = [0,0,0]

    for i in range(3):
      Bounds_Min[i] = self.position[i] - (epsilon + self.size / 2)
      Bounds_Max[i] = self.position[i] + (epsilon + self.size / 2)

    t = float('inf')
    intersect = None

    for plane in self.planes:
      planeIntersection = plane.ray_intersect(orig, direction)

      if planeIntersection is not None:
        if planeIntersection.point[0] >= Bounds_Min[0] and planeIntersection.point[0] <= Bounds_Max[0]:
          if planeIntersection.point[1] >= Bounds_Min[1] and planeIntersection.point[1] <= Bounds_Max[1]:
            if planeIntersection.point[2] >= Bounds_Min[2] and planeIntersection.point[2] <= Bounds_Max[2]:
              if planeIntersection.distance < t:
                t = planeIntersection.distance
                intersect = planeIntersection

                if abs(plane.normal[0]) > 0:
                    t1 = (planeIntersection.point[1] - Bounds_Min[1]) / (Bounds_Max[1] - Bounds_Min[1])
                    t2 = (planeIntersection.point[2] - Bounds_Min[2]) / (Bounds_Max[2] - Bounds_Min[2])

                elif abs(plane.normal[1]) > 0:
                    t1 = (planeIntersection.point[0] - Bounds_Min[0]) / (Bounds_Max[0] - Bounds_Min[0])
                    t2 = (planeIntersection.point[2] - Bounds_Min[2]) / (Bounds_Max[2] - Bounds_Min[2])

                elif abs(plane.normal[2]) > 0:
                    t1 = (planeIntersection.point[0] - Bounds_Min[0]) / (Bounds_Max[0] - Bounds_Min[0])
                    t2 = (planeIntersection.point[1] - Bounds_Min[1]) / (Bounds_Max[1] - Bounds_Min[1])

                textures = [t1, t2]

    if intersect is not None:
      return Intersect(distance = intersect.distance,
                      point = intersect.point,
                      texture=textures,
                      normal = intersect.normal)
    else:
      return None


#referencia
#https://www.scratchapixel.com/lessons/3d-basic-rendering/ray-tracing-rendering-a-triangle/ray-triangle-intersection-geometric-solution

class Triangulo(object):
  def __init__(self, vertice0, vertice1, vertice2, material):
    self.vertice0 = vertice0
    self.vertice1 = vertice1
    self.vertice2 = vertice2
    self.material = material

  def ray_intersect(self, origin, direction):
    epsilon = 0.001
    vertice01 = sub(self.vertice1, self.vertice0)
    vertice02 = sub(self.vertice2, self.vertice0)
    normal = mul(cross(vertice01, vertice02),1)
    tca = dot(normal, direction)

    if abs(tca) < epsilon:
        return None
    
    dis = dot(normal, self.vertice0)
    t = (dot(normal, origin) + dis)/tca
    pointinterseccion = sum(origin, mul(direction, t))

    edge = sub(self.vertice1, self.vertice0)
    vp = sub(pointinterseccion, self.vertice0)

    if dot(normal, cross(edge, vp)) < 0:
      return None

    edge = sub(self.vertice2, self.vertice1)
    vp = sub(pointinterseccion, self.vertice1)

    if dot(normal, cross(edge, vp)) < 0:
      return None

    edge = sub(self.vertice0, self.vertice2)
    vp = sub(pointinterseccion, self.vertice2)
    
    if dot(normal,  cross(edge, vp)) < 0:
      return None    


    return Intersect(distance =dis,
                     point = pointinterseccion,
                     normal = norm(normal)
                     )