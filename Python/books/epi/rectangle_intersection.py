import collections

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))


def intersect_rectangle(rectangle_1: 'Rectangle', rectangle_2: 'Rectangle') -> 'Rectangle':
    def is_intersect(rectangle_1: 'Rectangle', rectangle_2: 'Rectangle') -> bool:
        condition_1 = rectangle_1.x <= (rectangle_2.x + rectangle_2.width)
        condition_2 = (rectangle_1.x + rectangle_1.width) >= rectangle_2.x
        condition_3 = rectangle_1.y <= (rectangle_2.y + rectangle_2.height)
        condition_4 = (rectangle_1.y + rectangle_1.height) >= rectangle_2.y

        if all([condition_1, condition_2, condition_3, condition_4]):
            return True
        else:
            return False

    if not is_intersect(rectangle_1, rectangle_2):
        return Rectangle(x=0, y=0, width=-1, height=-1)

    x = max([rectangle_1.x, rectangle_2.x])
    y = max([rectangle_1.y, rectangle_2.y])
    width = max([rectangle_1.x + rectangle_1.width, rectangle_2.x + rectangle_2.width]) - x
    height = max([rectangle_1.y + rectangle_1.height, rectangle_2.y + rectangle_2.height]) - y

    return Rectangle(x=x, y=y, width=width, height=height)


print(intersect_rectangle(Rectangle(x=1, y=2, width=3, height=4), Rectangle(x=3, y=1, width=1, height=2)))
