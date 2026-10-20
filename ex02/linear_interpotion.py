from typing import TypeVar

from ex00.geometric_object import Matrix, Vector

V = TypeVar("V")  # float, Vector or Matrix


def lerp(u: V, v: V, t: float) -> V:
    # ALGO : (1 - t) *u + t * v 
    if isinstance(u, (float, int)) and isinstance(v, (float, int)):
        return round((1 - t) * u + t * v, 1)
    return u.scl(1 - t).add(v.scl(t)) 

def main():
    print(lerp(0., 1., 0.))
    # 0.0

    print(lerp(0., 1., 1.))
    # 1.0

    print(lerp(0., 1., 0.5))
    # 0.5

    print(lerp(21., 42., 0.3))
    # 27.3

    print(lerp(Vector([2., 1.]), Vector([4., 2.]), 0.3))
    # [2.6]
    # [1.3]

    print(lerp(Matrix([[2., 1.], [3., 4.]]), Matrix([[20., 10.], [30., 40.]]), 0.5))
    # [[11., 5.5]
    # [16.5, 22.]]


if __name__ == "__main__":
    main()