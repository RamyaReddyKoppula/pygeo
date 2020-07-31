from pygeo.objects import Ray, Sphere, Triangle, Point
import numpy as np


def intersect(first_object, second_object):
    if isinstance(first_object,Ray) and isinstance(second_object,Sphere):
        return _intersect_ray_with_sphere(first_object,second_object)
    return NotImplemented

def _intersect_ray_with_sphere(Ray, Sphere):
    l=Ray.direction-Ray.origin     
    a=l*l
    so=(Sphere.center-Ray.origin)
    b=(l*so)*2
    c=((so*so))-((Sphere.radius)**2)
    Delta = (b**2)-4*a*c
    if Delta<0:
        return 0,[0]
    elif Delta>0:
        d1=(-2*b+(np.sqrt(Delta)))/(2*a)
        d2=(-2*b-(np.sqrt(Delta)))/(2*a)
        intercept1=Ray.origin+((Ray.direction-Ray.origin)*d1)
        intercept2=Ray.origin+((Ray.direction-Ray.origin)*d2)
        intercepts=[intercept1,intercept2]
        d=2
        return d,intercepts
    else :
        d1=(-2*b+(np.sqrt(Delta)))/2*a
        intercepts=Ray.origin+((Ray.direction-Ray.origin)*d1)
        d=1
        return d,intercepts



def _intersect_ray_with_triangle(ray, triangle):
    ...
