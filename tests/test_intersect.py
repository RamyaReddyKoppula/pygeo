from pygeo.intersect import (
    intersect,
    _intersect_ray_with_sphere,
    _intersect_ray_with_triangle,
)
from pygeo.objects import Point, Ray, Sphere, Triangle


# intersect


# _intersect_ray_with_sphere
def test_intersect_ray_with_sphere_true():
    ray = Ray(Point((-2,0,0)),Point((1,0,0)))
    sphere = Sphere(Point((0,0,0)),1.0)
    d,intercepts = intersect(ray, sphere)
    intercepts_test = [Point([-5.0,0.0,0.0]),Point([-7.0,0.0,0.0])]
    d_analytical = 2
    assert ((intercepts == intercepts_test) and (d_analytical==d) )is True

def test_intersection__ray_with_sphere_that_intersects_at_no_points__return_true():
    ray = Ray(Point((-2,0,0)),Point((1,0,0)))
    sphere = Sphere(Point((10,10,200)),1.0)
    d,intercepts = (intersect(ray, sphere))
    intercepts_test = [0]
    d_analytical = 0
    assert ((intercepts == intercepts_test) and (d_analytical==d) )is True

def test_intersection__ray_with_sphere__inside_sphere__return_true():
    ray = Ray(Point((-10,0,0)),Point((1,0,0)))
    sphere = Sphere(Point((10,50,100)),1.0)
    d,intercepts = (intersect(ray, sphere))
    intercepts_test = [Point([-5.0,0.0,0.0]),Point([-7.0,0.0,0.0])]
    d_analytical = 2
    assert ((intercepts == intercepts_test) and (d_analytical==d) )is False

def test_intersect_ray_with_sphere_origin__given_tangent__return_true():
    ray = Ray(Point((-3,1,0)),Point((1,0,0)))
    sphere = Sphere(Point((0,0,0)),1.0)
    d,intercepts = (intersect(ray, sphere))
    intercepts_test = Point([0.0,1.0,0.0])
    d_analytical = 2
    assert ((intercepts == intercepts_test) and (d_analytical==d) )is False
# _intersect_ray_with_triangle
