import math
from scipy.spatial import Delaunay
import numpy as np
from py3d.core_ext.mesh import Mesh
from py3d.geometry.sphere import SphereGeometry
from py3d.geometry.box import BoxGeometry
class Collision:
    def check(self,camera,objectlist):
        for index,object in enumerate(objectlist):
            if isinstance(object,Mesh):
                if isinstance(object.geometry,BoxGeometry):
                    if (abs(self.distance(object.global_position, camera.global_position)) < self.get_length(object.geometry.vertices[0]*3)):
                            PL = np.array(camera.global_position)
                            OL = np.array(object.global_position)
                            OV = np.array(object.geometry.vertices)*1.25
                            result = (OL + OV)
                            if(self.is_point_in_3d_object(result,PL)):
                                return True
                if isinstance(object.geometry,SphereGeometry):
                    if (abs(self.distance(object.global_position, camera.global_position)) < object.geometry.radius*3):
                            point = np.array(camera.global_position)
                            center = np.array(object.global_position)
                            radius = object.geometry.radius
                            if (self.is_point_in_sphere(center,radius+0.15,point)):
                                return True
        return False




    def get_length(self,vertice):
        return math.sqrt(vertice[0] ** 2 + vertice[1] ** 2 + vertice[2] ** 2)
    def distance(self,coord1,coord2):
        return math.sqrt(coord1[0]**2+coord1[1]**2+coord1[2]**2)-math.sqrt(coord2[0]**2+coord2[1]**2+coord2[2]**2)

    def is_point_in_3d_object(self,vertices, point):
        tri = Delaunay(vertices)
        simplex = tri.find_simplex(point)
        return simplex >= 0

    def is_point_in_sphere(self,center, radius, point):
        distance = np.linalg.norm(center - point)
        return distance <= radius