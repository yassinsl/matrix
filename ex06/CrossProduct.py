rom ex00 import Vector
 
 
def cross_product(u: Vector, v: Vector) -> Vector:
    if u.size() != 3 or v.size() != 3:
        raise ValueError("Cross product is only defined for 3D vectors.")
    # v = [ u₂·v₃ − u₃·v₂ , u₃·v₁ − u₁·v₃ , u₁·v₂ − u₂·v₁ ]
    return Vector([
        round(u.data[1] * v.data[2] - u.data[2] * v.data[1], 1),
        round(u.data[2] * v.data[0] - u.data[0] * v.data[2], 1),
        round(u.data[0] * v.data[1] - u.data[1] * v.data[0], 1)
    ])
def main():
    u = Vector([0., 0., 1.])
    v = Vector([1., 0., 0.])
    print(cross_product(u, v))

    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print(cross_product(u, v))

    u = Vector([4., 2., -3.])
    v = Vector([-2., -5., 16.])
    print(cross_product(u, v))

if __name__ == "__main__":
    main()
 