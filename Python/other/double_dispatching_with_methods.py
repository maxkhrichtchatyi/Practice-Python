from functools import singledispatch
from math import sqrt


class Shape:

    def __init__(self, solid, *args, **kwargs):
        self.solid = solid


class Circle(Shape):

    def __init__(self, center, radius, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.center = center
        self.radius = radius

    def intersects(self, shape):
        # Delegate to the generic function, swapping arguments
        return intersects_with_circle(shape, self)


class Triangle(Shape):

    def __init__(self, pa, pb, pc, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pa = pa
        self.pb = pb
        self.pc = pc

    def intersects(self, shape):
        # Delegate to the generic function, swapping arguments
        return intersects_with_triangle(shape, self)


@singledispatch
def intersects_with_circle(shape, circle):
    raise TypeError(f'Don\'t know how to compute intersection of {circle} with {shape}')


@singledispatch
def intersects_with_triangle(shape, triangle):
    raise TypeError(f'Don\'t know how to compute intersection of {triangle} with {shape}')


@intersects_with_circle.register(Triangle)
def _(shape, circle):
    print('I don\'t know how to check that a triangle intersects with a circle!')
    return False


@intersects_with_circle.register(Circle)
def _(shape, circle):
    dx, dy = shape.center[0] - circle.center[0], shape.center[1] - circle.center[1]
    d = sqrt(dx * dx + dy * dy)

    if d > shape.radius + circle.radius:
        print("No solutions, the circles are separate")
        return False

    if d < abs(shape.radius - circle.radius):
        print("No solutions because one circle is contained within the other")
        return False

    if d == 0 and shape.radius == circle.radius:
        print("Circles are coincident and there are an infinite number of solutions")
        return False

    print('The circle intersects with another circle')
    return True


@intersects_with_triangle.register(Circle)
def _(shape, triangle):
    print('I don\'t know how to check that a circle intersects with a triangle!')


if __name__ == '__main__':
    shapes = [Circle(center=(5, 5), radius=1, solid=False), Triangle(pa=5, pb=5, pc=5, solid=True)]

    for shape in shapes:
        shape.intersects(Circle(center=(5, 6), radius=1, solid=False))
        shape.intersects(Circle(center=(10, 10), radius=2, solid=False))
