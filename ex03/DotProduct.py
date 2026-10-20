from ex00.geometric_object import Vector

#{u\cdot v=\sum_{i=1}^{n}u_iv_i}

def main():
    u = Vector([0., 0.])
    v = Vector([1., 1.])
    print(u.dot(v))

    u = Vector([1., 1.])
    v = Vector([1., 1.])
    print(u.dot(v))

    u = Vector([-1., 6.])
    v = Vector([3., 2.])
    print(u.dot(v))
if __name__ == "__main__":
    main()