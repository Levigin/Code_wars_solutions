import math


def tankvol(h, d, vt):
    r = d / 2
    h_cylinder = vt / (math.pi * r ** 2)
    alpha = 2 * math.acos(1 - h / r)
    s = (0.5 * (r ** 2) * (alpha - math.sin(alpha))) * h_cylinder
    return int(s)


print(tankvol(2, 7, 3848))
print(tankvol(5, 7, 3848))