from ex00.geometric_object import Vector

def angle_cos(u: Vector, v: Vector) -> float:
    #dots = U * V 
    #norms = ||U|| * ||V||
    #cos = dots / norms
    return round(u.dot(v) /(u.norm() * v.norm()), 1)
 
def main():
    u = Vector([1., 0.])
    v = Vector([1., 0.])
    print(angle_cos(u, v))
    # 1.0
 
    u = Vector([1., 0.])
    v = Vector([0., 1.])
    print(angle_cos(u, v))
    # 0.0
 
    u = Vector([-1., 1.])
    v = Vector([1., -1.])
    print(angle_cos(u, v))
    # -1.0
 
    u = Vector([2., 1.])
    v = Vector([4., 2.])
    print(angle_cos(u, v))
 
    u = Vector([1., 2., 3.])
    v = Vector([4., 5., 6.])
    print(angle_cos(u, v))
 
 
if __name__ == "__main__":
    main()